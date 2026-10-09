<!-- wiki-i18n source: 9aea6ae5901fd4d6 -->
<!-- wiki-i18n title: Hangar im Flug -->
# Der Hangar im Flug {#the-hangar-in-flight}

Du musst nicht zur Basis zurückkehren, um dein Schiff zu ändern. Aus einer Schutzzone heraus kannst du das Fenster **Hangar** öffnen (die Lagerhaus-Schaltfläche in der Symbolleiste oben links) und ändern, was ausgerüstet ist, zur anderen Konfiguration wechseln oder ein anderes Schiff fliegen, das du besitzt, ohne das Spiel zu verlassen. Das Fenster ist die Hangar-Seite der Station, mit denselben Slots, Werten und demselben Inventar, in einem Fenster über dem Spiel. Siehe [Inventar & Ausrüstung](/wiki/03-Mechanics/Inventory.md) dazu, wie Gegenstände passen.

![The Hangar window in flight, opened at the station on its Drones view: the drones, the list of drone formations and the inventory](../../img/wiki-img/shots/hangar-window.jpg)

## Wann er offen ist {#when-it-is-open}

Eine Änderung ist nur erlaubt, solange all das zutrifft:

- **Eine Schutzzone schützt dich.** Jede Station und jedes Portal hat einen Schutzring (siehe [Kampf](/wiki/03-Mechanics/Combat.md)). Darin bist du geschützt, sobald seit deinem letzten Treffer 5 Sekunden und seit deinem letzten Schuss 15 Sekunden vergangen sind.
- **Du warst noch ein paar Sekunden länger nicht im Kampf**: standardmäßig **10**. Das spielt eine Rolle, wenn du durch ein Portal sofort geschützt ankommst und ein Kampf hinter dir liegt.
- Du bist nicht getarnt, nicht im Fenster deines eigenen EMP und nicht in der Nähe des [Schwarzen Lochs](/wiki/03-Mechanics/Black-Hole.md), und keine Rakete von dir ist noch in der Luft.

Laufende Reparaturen halten dich nicht auf. Überall sonst öffnet sich das Hangar-Fenster trotzdem, ist aber schreibgeschützt. Ein bernsteinfarbenes Banner sagt, warum, und zählt die Sekunden herunter, wenn es eine Wartezeit ist („Du warst gerade noch im Kampf. Warte 6 s, um dein Schiff zu ändern.“). Der Server setzt es ebenfalls durch, sodass im Feld kein Schiff verändert werden kann.

## Was du ändern kannst {#what-you-can-change}

- **Alles ausrüsten und ablegen**, in jeder Art von Slot: Laser, Generatoren (Schilde, Triebwerke, adaptive Kerne), Extras, Fähigkeits-Slots, Drohnen-Slots und Panzerungs-Slots sowie die Verstärker, Zellen und Schubdüsen darin. Ziehe Gegenstände auf Slots oder klicke sie an, genau wie in der Station. Dein Schiff folgt sofort: Werte, Laser, Fähigkeiten und die Aktionsleiste.
- **Alles ablegen.** Die Schaltfläche **Alles ablegen** in der Symbolleiste des Hangars leert in einem Zug die Konfiguration, die in der Ansicht **Raumschiff** gezeigt wird: die Laser, Schilde, Triebwerke, adaptiven Kerne, Extras und Fähigkeits-Slots **und die Laser und Schilde in den Slots deiner Drohnen**, samt den Verstärkern, Zellen und Schubdüsen darin. Alles wandert zurück in dein Inventar, ganz oder gar nicht. Deine **Drohnen bleiben dir** (eine Drohne wird nie an ein Schiff angelegt, an ihr gibt es also nichts abzulegen), und die **Drohnenformation**, die du trägst, bleibt an. Die andere Konfiguration wird nicht angerührt. Im Flug gelten die Regeln jeder Änderung: aus einer Schutzzone, außerhalb eines Kampfes. Die Ansicht **Drohnen** hat eine eigene Schaltfläche, die nur die Slots der Drohnen leert.
- **Beide Konfigurationen.** Du kannst Konfig 2 vorbereiten, während du Konfig 1 fliegst, und dann mit der Taste Konfig wechseln tauschen. Eine Schaltfläche **Konfig 1 fliegen** bzw. **Konfig 2 fliegen** im Hangar macht denselben Wechsel.
- **Jedes Schiff.** Aktiviere ein anderes Schiff, und du fliegst es von dort aus, wo du bist. Das Modell deines Schiffs wechselt vor den Augen aller in der Nähe.
- **Ein neuer Schild, ein neues Triebwerk oder ein neuer adaptiver Kern startet leer**, wie in der Station: Die Schildladung seiner Konfiguration ist leer, bis sie sich auflädt.
- **Drohnenformationen.** Die Drohnen-Ansicht listet unter deinen Drohnen die Formationen auf, die du besitzt. Sie werden nicht angelegt: Im Flug ziehst du eine aus der Formationenliste der Aktionsleiste auf einen Slot, und Klick oder Taste dieses Slots trägt sie, mit denselben 2 Sekunden Wartezeit wie überall, auch in einer Schutzzone ([Drohnenformationen](/wiki/03-Mechanics/Formations.md)).
- **Extras.** Die vier regulären Schiffe, Protos, Kitefin, Ostirion und Nomad (die, mit denen du startest oder die du kaufst), haben in jeder Konfiguration 2 Extra-Slots; die vier Schiffe, die du in der Montage baust, Paragon, Ironclad, Wraith und Storm, haben 3. Die Extra Slots CPUs deines Skylabs geben 3, 5 oder 7 obendrauf: 5, 7 oder 9 bei den regulären Schiffen und 6, 8 oder 10 bei den gebauten ([Extras](/wiki/06-Items/Extras.md#extra-slots-cpus)). Mit 0.4.10 wurde ein dritter Extra auf einem regulären Schiff ins Inventar abgelegt: Nichts wurde gelöscht, und du hast eine Chatmeldung bekommen.
- **Hüllenpanzerung.** Die vier Schiffe, die du baust, haben [Panzerungs-Slots](/wiki/06-Items/Hull-Plating.md#hull-plate-slots) für Hüllenpanzerung, jeder gesperrt, bis du ihn im Skylab erforschst. Eine Panzerung, die du einbaust oder ablegst, lässt deinen Hüllenanteil unverändert, und sie bleibt dran, wenn du die Konfiguration wechselst.

Verkaufen gehört nicht zum Fenster: Der Hammer, der die [Auktion](/wiki/03-Mechanics/Auction.md) öffnet, gehört zum Hangar der Station, und die Auktion selbst ist eine Seite der Station.

## Das Schiff wechseln {#changing-ship}

Das Schiff, zu dem du wechselst, hat **die Hülle und die Schilde, die es hatte**, als du es zuletzt geflogen bist, genau so, als hättest du es gestartet. Der Ring repariert nicht, also heilt ein Schiffswechsel dich nie: Das Schiff, das du verlässt, behält seinen Schaden und kommt damit zurück. Ein zerstörtes Schiff lässt sich erst fliegen, wenn du es wiederherstellst; das ist kostenlos und bringt es wie ein Respawn mit höchstens 10.000 Hülle und ohne Schild zurück.

Was dir gehört, bleibt dir: deine Munition, deine Raketen und ihr Timer, die Abklingzeiten deiner Fähigkeiten, deine Booster, deine EP und deine Slave Drones. Was zum Schiff gehörte, endet: ein laufender Shield Surge oder Afterburner, Reparaturen, deine Zielerfassung, dein Angriff und der Kurs, den du geflogen bist. Ausrüstung bleibt auf dem Schiff, auf dem sie ausgerüstet ist.

## Anfragen von anderen Tools {#requests-from-other-tools}

Der Hangar lässt sich auch auf dem Server nur aus einer Schutzzone ändern: Wenn du, während du fliegst, einen Gegenstand ausrüstest, ablegst oder löschst, ein Schiff wiederherstellst oder das aktive Schiff festlegst, lautet die Antwort „Du kannst dein Schiff nur in einer Schutzzone ändern.“ Der Konfigurationswechsel ist die Ausnahme und funktioniert überall (einmal alle 5 Sekunden).
