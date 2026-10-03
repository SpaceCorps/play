<!-- wiki-i18n source: d888495e0809faa2 -->
<!-- wiki-i18n title: Hangar im Flug -->
# Der Hangar im Flug {#the-hangar-in-flight}

Du musst nicht zur Basis zurückkehren, um dein Schiff zu ändern. Aus einer Schutzzone heraus kannst du das Fenster **Hangar** öffnen (die Lagerhaus-Schaltfläche in der Symbolleiste oben links) und ändern, was ausgerüstet ist, zur anderen Konfiguration wechseln oder ein anderes Schiff fliegen, das du besitzt, ohne das Spiel zu verlassen. Das Fenster ist die Hangar-Seite der Station, mit denselben Slots, Werten und demselben Inventar, in einem Fenster über dem Spiel. Siehe [Inventar & Ausrüstung](/wiki/03-Mechanics/Inventory.md) dazu, wie Gegenstände passen.

## Wann er offen ist {#when-it-is-open}

Eine Änderung ist nur erlaubt, solange all das zutrifft:

- **Eine Schutzzone schützt dich.** Jede Station und jedes Portal hat einen Schutzring (siehe [Kampf](/wiki/03-Mechanics/Combat.md)). Darin bist du geschützt, sobald seit deinem letzten Treffer 5 Sekunden und seit deinem letzten Schuss 15 Sekunden vergangen sind.
- **Du warst noch ein paar Sekunden länger nicht im Kampf**: standardmäßig **10**. Das spielt eine Rolle, wenn du durch ein Portal sofort geschützt ankommst und ein Kampf hinter dir liegt.
- Du bist nicht getarnt, nicht im Fenster deines eigenen EMP und nicht in der Nähe des [Schwarzen Lochs](/wiki/03-Mechanics/Black-Hole.md), und keine Rakete von dir ist noch in der Luft.

Laufende Reparaturen halten dich nicht auf. Überall sonst öffnet sich das Hangar-Fenster trotzdem, ist aber schreibgeschützt. Ein bernsteinfarbenes Banner sagt, warum, und zählt die Sekunden herunter, wenn es eine Wartezeit ist („Du warst gerade noch im Kampf. Warte 6 s, um dein Schiff zu ändern.“). Der Server setzt es ebenfalls durch, sodass im Feld kein Schiff verändert werden kann.

## Was du ändern kannst {#what-you-can-change}

- **Alles ausrüsten und ablegen**, in jeder Art von Slot: Laser, Generatoren (Schilde, Triebwerke, adaptive Kerne), Extras, Fähigkeits-Slots und Drohnen-Slots sowie die Verstärker, Zellen und Schubdüsen darin. Ziehe Gegenstände auf Slots oder klicke sie an, genau wie in der Station. Dein Schiff folgt sofort: Werte, Laser, Fähigkeiten und die Aktionsleiste.
- **Beide Konfigurationen.** Du kannst Konfig 2 vorbereiten, während du Konfig 1 fliegst, und dann mit der Taste Konfig wechseln tauschen. Eine Schaltfläche **Konfig 1 fliegen** bzw. **Konfig 2 fliegen** im Hangar macht denselben Wechsel.
- **Jedes Schiff.** Aktiviere ein anderes Schiff, und du fliegst es von dort aus, wo du bist. Das Modell deines Schiffs wechselt vor den Augen aller in der Nähe.
- **Ein neuer Schild, ein neues Triebwerk oder ein neuer adaptiver Kern startet leer**, wie in der Station: Die Schildladung seiner Konfiguration ist leer, bis sie sich auflädt.

## Das Schiff wechseln {#changing-ship}

Das Schiff, zu dem du wechselst, hat **die Hülle und die Schilde, die es hatte**, als du es zuletzt geflogen bist, genau so, als hättest du es gestartet. Der Ring repariert nicht, also heilt ein Schiffswechsel dich nie: Das Schiff, das du verlässt, behält seinen Schaden und kommt damit zurück. Ein zerstörtes Schiff lässt sich erst fliegen, wenn du es wiederherstellst; das ist kostenlos und bringt es wie ein Respawn mit höchstens 10.000 Hülle und ohne Schild zurück.

Was dir gehört, bleibt dir: deine Munition, deine Raketen und ihr Timer, die Abklingzeiten deiner Fähigkeiten, deine Booster, deine EP und deine Slave Drones. Was zum Schiff gehörte, endet: ein laufender Shield Surge oder Afterburner, Reparaturen, deine Zielerfassung, dein Angriff und der Kurs, den du geflogen bist. Ausrüstung bleibt auf dem Schiff, auf dem sie ausgerüstet ist.

## Anfragen von anderen Tools {#requests-from-other-tools}

Der Hangar lässt sich auch auf dem Server nur aus einer Schutzzone ändern: Wenn du, während du fliegst, einen Gegenstand ausrüstest, ablegst oder löschst, ein Schiff wiederherstellst oder das aktive Schiff festlegst, lautet die Antwort „Du kannst dein Schiff nur in einer Schutzzone ändern.“ Der Konfigurationswechsel ist die Ausnahme und funktioniert überall (einmal alle 5 Sekunden).
