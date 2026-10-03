<!-- wiki-i18n source: 30354846186e8ea9 -->
<!-- wiki-i18n title: Drohnen -->
# Drohnenmechanik {#drone-mechanics}

Drohnen sind autonome Unterstützungseinheiten, die neben deinem Schiff fliegen. Sie liefern zusätzliche Ausrüstungs-Slots und tragen direkt zur Kampfleistung deines Schiffs bei. Eine Slave Drone wächst außerdem: Sie sammelt jedes Mal Erfahrung, wenn du ein Alien zerstörst, und steigt durch **acht Level** auf, von einer kleinen gepanzerten Kugel zu einem Kanonenboot mit Sichelflügeln. In der Montage lässt sich eine Slave Drone zu einer **Master Drone** aufrüsten, deren Level wieder von vorn beginnen (siehe Master Drone weiter unten).

## Drohnen bekommen {#getting-drones}

Jede Drohne, die du besitzt, eine **Slave Drone** oder eine Master Drone, schaltet ihre Drohnen-Slots frei (einen für eine Slave Drone, zwei für eine Master Drone), bis zu **8** Drohnen. Der Shop verkauft Slave Drones für Credits, ab der vierten auch für Thulium. Jede kostet mehr als die letzte: Die Preise stehen unter [Drohnen](/wiki/06-Items/Drones.md).

## Formation & Bewegung {#formation-movement}

Drohnen fliegen in einer Standard-**„Wingman“-Formation (2-2-4)**:

- **2 Drohnen** neben dem Schiff, eine auf jeder Flanke.
- **2 Drohnen** neben und knapp hinter ihm.
- **4 Drohnen** dahinter.

Sie nutzen einen flüssigen Folgealgorithmus, der ihre Position an Tempo und Drehung deines Schiffs anpasst und die Formation bei scharfen Manövern enger zieht. Niemand fliegt vor dir.

Drohnen sind klein und bleiben nah: Eine Drohne auf Level 8 ist etwa 19,5 Einheiten breit (eine Protos 50), und eine Drohne auf Level 1 ist eine Kugel von etwa 8, sodass die ganze Formation in etwa 135 Einheiten um dein Schiff Platz findet. Die Drohne, die du zuerst gekauft hast, hat die meiste Erfahrung und fliegt auf deiner linken Flanke, die zweite auf deiner rechten, und die neuesten fliegen hinterher.

## Ausrüstung & Werte {#equipment-stats}

Drohnen dienen als zusätzliche Ausrüstungsgestelle für dein Schiff.

- Eine Slave Drone hat **1 Slot** und eine Master Drone **2**, bis zu **8 Drohnen**.
- In diese Slots kannst du **Laser** und **Schilde** einsetzen, bei einer Master Drone in jeden der beiden Slots. Sonst passt nichts hinein: keine Triebwerke, keine adaptiven Kerne.
- **Laser zählen voll.** Ein Laser auf einer Drohne feuert, wenn du feuerst, addiert seinen Schaden zu deiner Salve und verbraucht Munition wie jeder andere Laser (jeder Laser verbraucht pro Salve eine Einheit Munition). Die zwei Laser einer Master Drone sind zwei Laser.
- **Schilde zählen ebenfalls voll.** Ein Schild auf einer Drohne zählt wie einer in einem Kern-Slot, in jedem der beiden Slots: seine Kapazität und Aufladung mit seinen Zellen, seine Absorption im Durchschnitt deines Schiffs, sein Schildbonus und sein Tempoabzug. Er wird mit den eigenen Schilden deines Schiffs nach Kapazität eingereiht (die vier größten zählen voll, der fünfte und alle weiteren weniger, siehe [Schildmechanik](/wiki/03-Mechanics/Shields.md)), und Schmiede-Buffs, die Buffs des Saison-Shops und die Schilddurchdringung eines Angreifers wirken auf ihn wie auf jeden Schild. Das Level der Drohne verstärkt nur ihren Laser, nie ihren Schild. Während eine Drohne aufgerüstet wird, sind ihre Slots offline, der Schild ebenso wie der Laser. Vor 0.4.7 brachte ein Schild auf einer Drohne nichts.
- **Laser oder Schild?** Ein Slot nimmt das eine oder das andere: Ein Laser bringt einen Laser in deine Salve, ein Schild bringt seine Schildpunkte. Auf einem kleinen Schiff mit guten Schilden bringen die zusätzlichen Punkte wenig, weil zuerst die Hülle aufgebraucht ist; auf einer großen Hülle lassen sie dich viel mehr einstecken.

## Level {#levels}

Jede Slave Drone beginnt auf Level 1 und bekommt Erfahrung (EP), wenn du ein Alien zerstörst. Auch eine Master Drone beginnt auf Level 1, ohne EP, und steigt genauso auf. Jedes Level verlangt mehr als das vorige, und mit ihm ändert sich das Aussehen, sodass du siehst, wie weit eine Drohne gekommen ist. Die Tabelle nennt für jedes Level die EP, die nötig sind, um vom vorigen Level dorthin aufzusteigen, und wie vielen Abschüssen einer einzelnen Alien-Art das für sich genommen entspricht (in der Welt Alpha: Beta braucht etwa halb so viele, Gamma etwa ein Drittel):

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **Level 1, Keim:** eine kleine gepanzerte Kugel mit einer cyanfarbenen Linse.
- **Level 2, Halo:** die Kugel in einem schwebenden Ring.
- **Level 3, Scheibe:** eine flache Scheibe unter einer Glaskuppel.
- **Level 4, Untertasse:** eine Untertasse mit Panzerplatten und Lufteinlässen.
- **Level 5, Kanonenboot:** ein Bug und zwei Kanonen kommen an die Untertasse.
- **Level 6, Flügelknospen:** Kanonen und kurze Flügelklingen an Pylonen.
- **Level 7, Halbflügel:** längere Flügelklingen mit goldenen Spitzen.
- **Level 8, Sichel:** das fertige Kanonenboot: volle Sichelflügel mit cyanfarbenen Leuchtstreifen.

| Level | EP bis dahin | EP für das Level | Laserschaden | Abschüsse Seeker | Abschüsse Bulwark | Abschüsse Goombah |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +1 % | 550 | 69 | 23 |
| 4 | 2.000 | 1.100 | +2 % | 1.100 | 138 | 46 |
| 5 | 3.700 | 1.700 | +3 % | 1.700 | 213 | 71 |
| 6 | 6.000 | 2.300 | +4 % | 2.300 | 288 | 96 |
| 7 | 9.500 | 3.500 | +5 % | 3.500 | 438 | 146 |
| 8 | 14.000 | 4.500 | +7 % | 4.500 | 563 | 188 |

| Alien | EP für jede Drohne |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Goombah | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### So sammeln Drohnen EP {#how-drones-earn-xp}

- **Jede Drohne, die du besitzt, bekommt dieselben EP** für jeden Alien-Abschuss, für den du bezahlt wirst: die ersten 8 Drohnen, egal ob sie einen Laser tragen oder nicht. Eine Drohne, die du später kaufst, beginnt auf Level 1 ohne EP, deshalb haben deine ersten Drohnen immer das höchste Level.
- **Härtere Aliens sind mehr wert.** Die EP, die ein Alien gibt, stehen in der zweiten Tabelle oben (ein Crystalys ist 72 Seeker wert). Jedes andere Alien gibt 1.
- **Welten zahlen mehr.** Beta verdoppelt die EP, Gamma verdreifacht sie (die Aliens dort haben auch mehr Trefferpunkte). Booster und Premium ändern sie nicht.
- **Abschüsse zählen, wenn sie dir etwas einbringen.** Ein Alien, das du erledigst, während ein anderer Pilot seinen Anspruch hält, bringt deinen Drohnen nichts, ebenso wenig wie dir. Abschüsse von Spielern, Quests und die eigenen Abschüsse von Konzernpiloten geben keine Drohnen-EP.
- **Level 8 ist das letzte Level.** EP werden danach weitergezählt.

### Was ein Level bringt {#what-a-level-gives}

Der **Laser im Slot einer Drohne** richtet mehr Grundschaden an, wenn seine Drohne aufsteigt: auf Level 1 und 2 nichts, dann +1 % auf Level 3, bis zu **+7 % auf Level 8**. Der Bonus multipliziert den eigenen Schaden dieses Lasers (nach seiner Verzauberung); die darin eingesetzten Verstärker werden obendrauf addiert und nicht multipliziert. Der Hangar zeigt Level, EP-Balken und die Abschüsse, die das nächste Level verlangt, jeder Drohne, und seine Schadenswerte enthalten den Bonus bereits. Steigt eine Drohne auf, sagt es das Spielprotokoll („Drohne 2 hat Level 4 erreicht.“), und die Drohne blitzt mit einem Lichtring auf.

### Wie lange es dauert {#how-long-it-takes}

Die Kurve ist so gesetzt, dass eine neue Drohne in etwa einer Stunde normalen Spiels (Jagd auf Bulwarks und Goombahs) Level 2 erreicht und Level 8 nach grob 27 Spielstunden. Diese Stunden gelten für einen Piloten, der die erste Drohne etwa bei den Missionen von Level 7 kauft; mit schwächerer Ausrüstung dauert es länger (bis zu etwa 4 Stunden für Level 2 und 150 Stunden für Level 8). Nur eine einzige Alien-Art zu jagen ist bestenfalls etwa um die Hälfte schneller als eine normale Mischung. Drohnen bleiben beim Saison-Wipe mit ihren Leveln und ihrer Erfahrung erhalten, deshalb werden diese Stunden nur einmal aufgewendet, über so viele Saisons, wie es dauert: Ein Pilot, der eine halbe Stunde am Tag spielt, schafft es in ein paar Saisons.

### Master Drone {#master-drone}

Eine Slave Drone wird zur **Master Drone**, wenn du sie in der Montage aufrüstest. Das Rezept kostet 40.000 Thulium und 100 Ship Fragments und dauert 60 Sekunden, und es verbraucht keine Drohne: **Du wählst, welche Slave Drone es ist** (die Auswahl zeigt Level und EP jeder einzelnen), und genau diese Drohne, mit ihrer Nummer, ihrem Drohnen-Slot und allem, was darin eingesetzt ist, wird zur Master Drone, sobald der Auftrag fertig ist, mit einem zweiten Slot, der leer ist. Nichts landet in deinem Inventar, und es gibt nichts abzuholen: Das Spielprotokoll sagt dir, wann es fertig ist, auch bei einer Aufrüstung, die fertig wurde, während du weg warst.

**Level und EP werden auf 0 zurückgesetzt, wenn die Aufrüstung fertig ist.** Eine Master Drone beginnt wieder auf Level 1, ohne EP, und steigt so auf wie eine Slave Drone (siehe Tabelle oben); der Laserbonus des Levels, das sie hatte, geht damit verloren. Die Montage sagt dir das, bevor du anfängst, und lässt dich bestätigen, unter Nennung der Drohne, wenn sie EP hat. Vorgewählt ist die Drohne mit den wenigsten EP.

Solange die Aufrüstung läuft, ist die Drohne gesperrt: Du kannst sie nicht noch einmal aufrüsten oder löschen, und ihr Slot ist **offline**, der Laser darin feuert also nicht, bis der Auftrag fertig ist (bis dahin ist sie noch eine Slave Drone mit einem Slot). Sie wird wie jede Herstellung hinter deinen anderen Aufträgen eingereiht.

Eine Master Drone ist eine deiner 8 Drohnen: Sie zählt für das Drohnenlimit und für den Preis der nächsten Slave Drone, die Aufrüstung ändert also keines von beiden, und sie bleibt beim Saison-Wipe mit Level und EP erhalten. Im Flug ist sie das fertige Kanonenboot in Gold. Eine Master Drone hat **zwei Ausrüstungs-Slots**, wo eine Slave Drone einen hat: Jeder nimmt einen Laser oder einen Schild auf, und der Levelbonus gilt für den Laser in beiden. Sonst ist sie eine Slave Drone: dieselben acht Level und derselbe Laserbonus. Master Drones, die du hergestellt hast, bevor es den zweiten Slot gab, haben ihn jetzt, wobei das, was sie trugen, an seinem alten Platz geblieben ist. Master Drones, die hergestellt wurden, bevor es Aufrüstungen an Ort und Stelle gab, sind gewöhnliche Gegenstände in deinem Inventar und fliegen nicht.

## Kampfverhalten {#combat-behavior}

- **Laser**: Drohnen feuern ihre ausgerüsteten Laser auf dein anvisiertes Ziel.
- **Schaden**: Drohnen können Schaden nehmen (sofern eine eigene Entitätslogik existiert; derzeit teilen sie sich meist den Pool des Schiffs, sind aber optisch eigenständig). _Hinweis: Derzeit sind Drohnen unzerstörbare Erweiterungen des Schiffs._
