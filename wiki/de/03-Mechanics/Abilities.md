<!-- wiki-i18n source: d8bf989776a71cb4 -->
<!-- wiki-i18n title: Fähigkeiten -->
# Aktive Schiffsfähigkeiten {#active-ship-abilities}

Fähigkeiten sind die Schaltflächen, die du in der Hitze des Gefechts drückst: ein Schild, der zurückkommt, ein Geschwindigkeitsschub, um außer Reichweite zu kommen, eine Reparatur, wenn deine Hülle fast aufgebraucht ist. Sie kommen von einem Gegenstand, den du in die **Fähigkeits-Slots** deines Schiffs einsetzt: einem **Schild, einem Triebwerk oder einer Repair Drone**. Je besser dieser Gegenstand ist, desto besser ist die Fähigkeit. Sie sind für den Moment gemacht, in dem du sie brauchst, nicht dafür, sie jedes Mal zu drücken, sobald die Abklingzeit vorbei ist: Jede läuft etwa zehn Sekunden und ruht dann eineinhalb bis zwei Minuten.

Ein neuer Pilot beginnt mit einer: Die **Repair Drone I** der Startausrüstung steckt bereits im Fähigkeits-Slot der Protos, also ist die Schaltfläche Emergency Repair (`E`) von der ersten Minute an da.

## Fähigkeits-Slots {#ability-slots}

Jedes Schiff hat im Hangar eine feste Anzahl an Fähigkeits-Slots:

- **Protos** (Startschiff): 1 Slot
- **Kitefin**: 1 Slot
- **Ostirion**: 2 Slots
- **Paragon**: 3 Slots
- **Ironclad**: 3 Slots
- **Wraith**: 3 Slots

Ein Fähigkeits-Slot nimmt einen **Schild**, ein **Triebwerk** oder eine **Repair Drone** auf, und jedes davon erzeugt seine eigene Fähigkeit. Ziehe den Gegenstand auf den Slot. Konfiguration 1 und Konfiguration 2 haben jeweils eigene Slots.

- **Schildzellen und Schubdüsen passen nicht in einen Fähigkeits-Slot.** Sie sind Module für Schilde, Triebwerke und adaptive Kerne.
- **Ein Gegenstand in einem Fähigkeits-Slot bringt sonst nichts.** Er gibt weder Schildkapazität, Aufladung, Absorption noch Tempo, und auch die Verlangsamung, die ein Schild sonst mit sich bringt, entfällt. Derselbe Heavy Shield Core sitzt entweder in einem Generator-Slot und liefert in jedem Moment seinen Schild, oder in einem Fähigkeits-Slot für seinen Surge. Du entscheidest.
- Ein Schild oder Triebwerk, das Schildzellen oder Schubdüsen enthält, gibt sie an dein Inventar zurück, wenn du es auf einen Fähigkeits-Slot ziehst.
- Eine Repair Drone in einem Fähigkeits-Slot erzeugt Emergency Repair und repariert die Hülle nicht von selbst. Die langsame Drohne (**REP**) braucht eine Repair Drone in einem Extra-Slot.

## Mehrere Module einer Art {#several-modules-of-one-kind}

Du kannst **mehrere Schilde, Triebwerke oder Repair Drones** in die Fähigkeits-Slots einer Konfiguration einsetzen. Sie bleiben eine Fähigkeit, eine Schaltfläche und eine Abklingzeit, aber eine stärkere:

- **Das Modul mit dem schlechtesten Rang bestimmt die Basis.** Sein Rang legt Stärke und Abklingzeit fest. Ein Heavy Shield Core neben einem Light Shield Core verhält sich wie zwei Module von Rang I: Ein besseres zweites Modul bringt den Bonus, aber nie eine bessere Stärke oder eine kürzere Abklingzeit.
- **Jedes weitere Modul fügt 50 % der Basis hinzu**, addiert, nicht multipliziert. Triebwerke verlängern die **Dauer** des Afterburners: 10 s, mit zwei Triebwerken 15 s, mit drei 20 s (Tempobonus und Abklingzeit ändern sich nicht). Schilde lassen den Shield Surge **mehr wiederherstellen**, und Repair Drones lassen Emergency Repair **mehr heilen**, in denselben zehn Sekunden: 100 %, 150 % und 200 % des Gesamtwerts bei einem, zwei und drei Modulen.
- **Die zusätzlichen Module kosten Slots.** Ein Schiff mit drei Fähigkeits-Slots kann drei von einer Art haben, oder je eines, oder zwei und eines. Eine Protos oder eine Kitefin hat nur einen Slot und kann nicht stapeln; eine Ostirion kann zwei von einer Art haben.
- Gleiche Ränge sind einfach dieser Rang. Von zwei Modulen desselben Rangs bestimmt das mit der schwächeren Verzauberung die Basis.

## Die drei Fähigkeiten {#the-three-abilities}

### Shield Surge (Schilde), Taste `Q` {#shield-surge-shields-key-q}

Zehn Sekunden lang wird der Schild deines Schiffs **repariert**: Der Surge stellt einen Anteil deines maximalen Schilds gleichmäßig wieder her, bis zum Maximum und nie darüber. Er ist keine Barriere und ändert nicht, wie Treffer aufgeteilt werden; er bringt Schild zurück, und was er zurückgebracht hat, bleibt. Er endet nicht, wenn du getroffen wirst (die normale Aufladung wartet nach einem Treffer 15 Sekunden; der Surge nicht). Ein Schiff mit vollem Schild hat wenig davon: Drücke ihn also, wenn der Schild schwindet. Der Gesamtwert ist nie kleiner als die eigene Kapazität des Shield Core, daher bekommt auch ein Schiff mit wenig Schild eine echte Reparatur (bis zu seinem Maximum).

- Wird innerhalb des Schutzes einer Schutzzone und auf einem Schiff ganz ohne Schild abgelehnt, damit ein Fehlklick den Surge nicht vergeudet.
- Raketen mit Schilddurchdringung umgehen die Schilde weiterhin teilweise, wie sie es schon immer taten.

### Afterburner (Triebwerke), Taste `W` {#afterburner-engines-key-w}

Dein Endtempo wird für die Dauer mit dem Bonus des Rangs multipliziert. Er ändert nichts an Wenden, Anvisieren oder erlittenem Schaden: Er macht aus Zeit Strecke. Nutze ihn, um einen Kampf zu verlassen, um den Stationsring oder Portalring zu erreichen oder um ein fliehendes Ziel einzuholen. Er funktioniert überall, auch in Schutzzonen. Mehr Triebwerke verlängern ihn, machen ihn aber nicht schneller.

### Emergency Repair (Repair Drones), Taste `E` {#emergency-repair-repair-drones-key-e}

Heilt einen Anteil deiner **maximalen Hülle gleichmäßig über zehn Sekunden**, nie über das Maximum. Treffer unterbrechen sie nicht: Es ist eine Notfallfähigkeit, und sie wirkt unter Beschuss, in der Strahlung des Schwarzen Lochs, unter einer Tarnung und innerhalb eines EMP-Fensters. Sie endet, wenn die Zeit um ist oder wenn dein Schiff zerstört wird. Sie berührt deinen Schild nicht, zählt nicht als Treffer und lässt die langsame REP-Reparatur, wie sie war. Bei voller Hülle wird sie abgelehnt.

## Ränge {#ranks}

Die Stärke einer Fähigkeit ist ein **Anteil an einem Wert deines eigenen Schiffs** (maximaler Schild, Tempo, maximale Hülle), sie wächst also mit dem Schiff. Der Rang kommt vom Gegenstand: Ein besseres Modell gibt eine bessere Fähigkeit. Ein verzauberter Gegenstand fügt seinen Verzauberungsbonus zur Stärke hinzu, höchstens 15 %. Die Tabelle gilt für ein Modul; der Stapel steht darunter.

<!-- abilities:begin -->
<!-- Generated from server/Resources/AbilityConfig.json and the items' stats by scripts/abilities-wiki.sh: don't edit by hand. -->

| Fähigkeit | Rang | Gegenstand | Stärke (ein Modul) | Dauer | Abklingzeit | Aktiv |
| :--- | :---: | :--- | :--- | --: | --: | --: |
| **Shield Surge** | I | Light Shield Core | stellt 30 % deines maximalen Schilds wieder her | 10 s | 120 s | 8,3 % |
| **Shield Surge** | II | Basic Shield Core | stellt 60 % deines maximalen Schilds wieder her | 10 s | 105 s | 9,5 % |
| **Shield Surge** | III | Heavy Shield Core | stellt 100 % deines maximalen Schilds wieder her | 10 s | 90 s | 11,1 % |
| **Afterburner** | I | Engine I | +30 % Tempo | 10 s | 120 s | 8,3 % |
| **Afterburner** | II | Engine II | +45 % Tempo | 10 s | 105 s | 9,5 % |
| **Afterburner** | III | Engine III | +60 % Tempo | 10 s | 90 s | 11,1 % |
| **Emergency Repair** | I | Repair Drone I | heilt 20 % deiner maximalen Hülle | 10 s | 120 s | 8,3 % |
| **Emergency Repair** | II | Repair Drone II | heilt 25 % deiner maximalen Hülle | 10 s | 105 s | 9,5 % |
| **Emergency Repair** | III | Repair Drone III | heilt 32 % deiner maximalen Hülle | 10 s | 90 s | 11,1 % |
| **Emergency Repair** | IV | Repair Drone IV | heilt 40 % deiner maximalen Hülle | 10 s | 75 s | 13,3 % |

Mehrere Module einer Art in einer Konfiguration: Das mit dem niedrigsten Rang bestimmt Stärke und Abklingzeit wie oben, jedes weitere fügt 50 % davon hinzu.

| Module einer Art | Afterburner hält | Shield Surge stellt wieder her | Emergency Repair heilt |
| :---: | --: | --: | --: |
| 1 | 10 s | 100 % | 100 % |
| 2 | 15 s | 150 % | 150 % |
| 3 | 20 s | 200 % | 200 % |

<!-- abilities:end -->

Schilde und Triebwerke von Rang III (der Heavy Shield Core, Engine III) werden nicht verkauft: Du stellst sie in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) aus einem Basic Shield Core und einem Engine II her, mit Thulium, Beute und Velkonite Reinforced Plates aus der Schmiede deines [Skylab](/wiki/03-Mechanics/Skylab.md). Emergency Repair hat einen vierten Rang, die Repair Drone IV.

## Abklingzeiten und Grenzen {#cooldowns-and-limits}

- **Die Abklingzeit beginnt, wenn du die Fähigkeit drückst**, und schließt ihre Dauer ein. Ein Surge von 10 Sekunden mit 90 Sekunden Abklingzeit ist also höchstens 11 % der Zeit aktiv und nach seinem Ende 80 Sekunden lang nicht verfügbar. Mehrere Module verkürzen sie nicht (es zählt die des Moduls mit dem schlechtesten Rang); selbst drei Afterburner sind höchstens 22 % der Zeit aktiv.
- **Abklingzeiten gehören dir, nicht dem Gegenstand.** Konfiguration wechseln, den Gegenstand tauschen, in einen anderen Sektor springen und sich ausloggen setzen sie nicht zurück. Ein zerstörtes Schiff beginnt den nächsten Flug mit allen Fähigkeiten bereit.
- **Jede Fähigkeit hat ihre eigene Abklingzeit.** Wenn du eine einsetzt, sperrt das die anderen nicht.
- **Ein laufender Effekt behält die Werte, mit denen er gestartet ist.** Den Gegenstand abzulegen oder die Konfiguration zu wechseln ändert oder beendet ihn nicht. Auch ein Sprung oder ein erneutes Verbinden beendet ihn nicht; Ausloggen schon, und seine Abklingzeit bleibt.
- Andere Piloten sehen die Timer deiner Fähigkeiten auf der Karte, wie schon immer: Ein verbrauchter Surge verrät ihnen, dass die nächsten Minuten offen sind.

## Tasten und Schaltflächen {#keys-and-buttons}

`Q` Shield Surge, `W` Afterburner, `E` Emergency Repair (alle in den Einstellungen anpassbar). Jede Schaltfläche erscheint neben der Aktionsleiste nur, wenn deine Konfiguration diese Fähigkeit hat, daher ist das `E` eines neuen Piloten von der ersten Minute an da. Der Ring um ihr Symbol zeigt, wo die Fähigkeit gerade steht: ganz in der Farbe der Fähigkeit, wenn sie bereit ist, mit den verbleibenden Sekunden leerlaufend, solange sie läuft (auch bei Emergency Repair, jetzt, da sie über zehn Sekunden heilt), und sich wieder füllend, während die Abklingzeit läuft, mit den verbleibenden Sekunden in der Mitte. Ein Stapel mehrerer Module trägt sein Zeichen (`x2`, `x3`) in der Ecke der Schaltfläche. Die Schaltfläche von Emergency Repair ist abgedunkelt, solange deine Hülle voll ist, und die von Shield Surge auf einem Schiff ganz ohne Schild. Zeige auf eine Schaltfläche, um die Werte auf deinem Schiff zu sehen, den Stapel eingerechnet (zum Beispiel *Afterburner II x2: +45 % Tempo für 15 s*), und, während ein Surge oder eine Reparatur läuft, wie viel sie pro Sekunde gibt und wie viel noch aussteht.

## Im Hangar {#in-the-hangar}

Ziehe einen Schild, ein Triebwerk oder eine Repair Drone auf einen Fähigkeits-Slot, oder klicke in deinem Inventar mit der rechten Maustaste auf den Gegenstand, um ihn in den ersten freien Slot zu setzen. Ein zweiter und ein dritter Gegenstand derselben Art kommen in die nächsten freien Slots und stapeln sich. Name und Rang der Fähigkeit stehen unter jedem belegten Slot, zusammen mit dem Stapelzeichen und den Werten aller seiner Module (*Afterburner II x2*, *x2 · 15 s*; bei einer Repair Drone II auf einer Wraith *+81.000 Hülle*), und wenn du auf einen Slot zeigst, siehst du, was er auf deinem Schiff wert ist, den Stapel eingerechnet, und welches Modul des Stapels den Rang bestimmt. Jedes Modul einer Art zeigt dieselbe Fähigkeit, weil sie eine sind. Zeigst du anderswo auf den Gegenstand, siehst du die Fähigkeit mit den Anteilen deines eigenen Schiffs und einem Satz dazu, was ein weiteres Modul bringt.

## Was alle sehen {#what-everyone-sees}

Ein Shield Surge ist eine Blase um das Schiff, solange er läuft; sie flackert in seinen letzten zwei Sekunden und zieht sich zusammen, wenn er endet. Die Schildbalken (deiner im Schiffsfenster, der eines Ziels im Zielfenster) füllen sich einfach, während der Surge Schild zurückbringt, und der Balken pulsiert leicht, solange noch Platz dafür ist. Ein Afterburner lässt die Triebwerke heißer brennen, solange er läuft, 10, 15 oder 20 Sekunden, und schickt beim Start einen Ring vom Schiff aus, bei einem Stapel breiter. Eine Emergency Repair schickt beim Start einen grünen Impuls aus, hüllt dann für ihre zehn Sekunden die Hülle in ein sanftes grünes Leuchten, aus dem ein paar Pluszeichen aufsteigen, blendet die Hülle, die sie jede Sekunde heilt, als schwebende Zahl über deinem eigenen Schiff ein und endet mit einem letzten Aufblitzen. Während sie läuft, umkreisen kleine Reparaturdrohnen das Schiff und bessern es aus: eine bei einer Repair Drone I, zwei bei einer II, drei bei einer III oder IV und eine mehr für jede weitere Repair Drone in einem Stapel (nie mehr als drei). Sie verlassen die Hülle, richten sanfte grüne Strahlen auf deren Platten, schicken ab Stufe II Impulse an den Strahlen entlang und fliegen zum Andocken zurück, wenn die zehn Sekunden um sind; ein Shield Surge hat bis zu zwei blaue Drohnen in seiner Blase. Jeder Pilot auf der Karte sieht alle drei Fähigkeiten, auch die Drohnen (auf dem Schiff eines anderen Piloten kleiner und auf den niedrigeren Grafikeinstellungen weniger, wobei Niedrig Strahlen und Leuchten ohne Drohnenmodelle zeigt, und ein Strahl, der mit jedem Rang der Drohne etwas breiter wird), ein verbrauchter Surge ist also ebenso ein Signal an den Feind wie an dich. Die Drohnen machen drei leise Geräusche für sich, weit leiser als der Glockenton der Reparatur: ein sanftes Blip, wenn sie die Hülle verlassen, eines beim Andocken und einen schwachen Ton unter ihren Strahlen, solange sie arbeiten (die Drohnen eines Surge etwas höher); du hörst sie von Schiffen auf deinem Bildschirm, höchstens ein paar gleichzeitig, und die Lautstärke der Soundeffekte regelt sie herunter. Mit eingeschaltetem *Bewegung reduzieren* bleibt das Leuchten gleichmäßig, die Pluszeichen entfallen, das letzte Aufblitzen wird zu einem Ausblenden, und die Drohnen bleiben mit einem gleichmäßigen Strahl neben dem Schiff geparkt (die Geräusche bleiben).

## Was sich geändert hat {#what-changed}

Vor dem Update 0.4.3 nahmen die Fähigkeits-Slots Schildzellen (Schildregeneration) und Schubdüsen (Tempo-Boost) auf. Schildzellen und Schubdüsen, die in Fähigkeits-Slots saßen, gingen beim Update des Spiels zurück in dein Inventar, und du behältst sie: Sie sind weiterhin Module für Schilde, Triebwerke und adaptive Kerne. Seitdem gibt der Shield Surge keine Überschild-Barriere mehr, sondern repariert deinen Schild über zehn Sekunden, Emergency Repair heilt über zehn Sekunden statt auf einmal, und du kannst mehrere Module einer Art einsetzen, für einen längeren Afterburner, einen größeren Surge oder eine größere Reparatur.
