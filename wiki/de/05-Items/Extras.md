<!-- wiki-i18n source: 46436d9c65bc6c7e -->
<!-- wiki-i18n title: Extras -->
# Extras {#extras}

Extras sind die Gadgets in den **Extra-Slots** eines Schiffs (drei auf jedem Schiff, pro Konfiguration). Du schaltest eines über die Extras-Auswahl der Aktionsleiste ein oder über einen Slot der Aktionsleiste, dem du es zugewiesen hast. Sie wirken nur in der Konfiguration, die du fliegst: Setzt du eines in die andere Konfiguration ein, wartet es, bis du wechselst.

| Extra | Wirkung | Nutzungen | Preis |
| :---- | :------ | :-------- | :---- |
| **Repair Drone I bis IV** | Repariert deine Hülle, 1,5 %, 2,25 %, 3,5 % und 5 % des Maximums pro Sekunde | unbegrenzt | 5.000 / 15.000 / 35.000 Credits, 2.000 Thulium |
| **Cloaking CPU S** | Verbirgt dein Schiff | 10 | 5.000 Thulium |
| **Cloaking CPU M** | Verbirgt dein Schiff | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Verbirgt dein Schiff | 50 | 20.000 Thulium |
| **EMP Charge** | 3 Sekunden lang kann dich niemand anvisieren, jede Zielerfassung auf dich bricht ab, und jede Tarnung in deiner Nähe endet | 1 | 500 Thulium |

Die Cloaking CPUs und die EMP Charge gibt es nur im Shop. Sie lassen sich nicht zusammenführen, und nichts verschenkt sie.

## Repair Drones {#repair-drones}

Schalte eine Repair Drone ein (REP), und sie repariert die Hülle, bis sie voll ist. Sie startet erst nach 10 Sekunden ohne Treffer, und jeder Treffer schaltet sie wieder aus. Sind mehrere ausgerüstet, arbeitet die beste. Die Raten stehen unter [Kampf](/wiki/03-Mechanics/Combat.md).

## Cloaking CPU {#cloaking-cpu}

Drücke den CLK-Slot, um dich zu tarnen. **Ein Druck ist eine Nutzung**, egal welches Paket, und die übrigen Nutzungen siehst du am Slot und im Hangar. Eine Tarnung hat **kein Zeitlimit**: Sie bleibt an, bis du sie ausschaltest oder etwas sie unterbricht.

- **Wer dich nicht sehen kann.** Piloten anderer Konzerne und Aliens sehen dein Schiff überhaupt nicht: Es ist weder auf ihrem Bildschirm noch in ihrer Zielliste, und niemand kann es anvisieren. Konzernpiloten anderer Konzerne ignorieren es ebenfalls.
- **Der Radarpunkt.** Jeder andere Pilot auf der Karte, außer denen deines eigenen Konzerns, sieht auf der Minikarte dort, wo du bist, einen schlichten **roten Punkt** und weiß daher, dass jemand Getarntes in der Nähe ist. Der Punkt hat weder Namen noch Schiff, Konzern oder ID und lässt sich nicht anklicken oder anvisieren; fährt man mit der Maus darüber, steht dort nur „Hier ist etwas getarnt“. Er ist rund, innerhalb eines Rings (Schiffe auf der Minikarte sind Quadrate), und der Ring „atmet“ langsam oder steht still, wenn du „Bewegung reduzieren“ aktiviert hast. Der Server aktualisiert ihn etwa zweimal pro Sekunde, und dein Spiel bewegt ihn dazwischen fließend. Er sagt, dass jemand da ist und wo, nicht wer: Ein Pilot, der gesehen hat, wie du dich getarnt hast, kann dem Punkt folgen, und die **Explosion einer Rakete**, die auf ihn gerichtet ist, trifft dich trotzdem.
- **Wer dich sehen kann.** Du siehst dein eigenes Schiff blass und mit Umriss. Piloten deines Konzerns sehen dich als blassen Geist; Clanmitglieder anderer Konzerne tun das nicht, weil ein Clan jeden aufnimmt, der sich bewirbt. Den Geist kann niemand anvisieren, nicht einmal dein Konzern.
- **Nicht tarnen kannst du dich** in einer Schutzzone, solange sich die CPU auflädt, oder innerhalb von **10 Sekunden** nach einem Treffer oder Schuss.
- **Was sie beendet.** Erneutes Drücken des Slots, deine erste Salve oder Rakete (sie trifft, und du wirst gesehen), das Betreten einer Schutzzone, das Ausscheiden der CPU aus der Konfiguration, die du fliegst, ein **EMP, der im Umkreis von 1.500 Einheiten** von dir ausgelöst wird, egal wer ihn eingesetzt hat (auch einer deines eigenen Konzerns, aber nicht einer aus deiner Gruppe), und der Flächenschaden einer Rakete, die dich trifft. Die Zeit beendet sie nicht, das Einsammeln von Fracht nicht (eine Kiste, die du nimmst, ist für alle weg, sie erfahren also, dass etwas in Reichweite dieser Stelle war, nicht wer), Fähigkeiten nicht, und die Strahlung des Schwarzen Lochs schadet einem getarnten Schiff, beendet aber seine Tarnung nicht. Ausloggen oder Sterben beendet sie, denn ein Schiff, das nicht geflogen wird, ist nicht getarnt.
- **Aufladung.** Nachdem eine Tarnung endet, egal wie, lädt sich die CPU **60 Sekunden** lang auf. Die Aufladung gehört dir, nicht dem Schiff: Sie läuft weiter, wenn du durch ein Portal springst, dich ausloggst oder stirbst. Jeder Druck kostet trotzdem eine Nutzung.
- **Aliens**, die hinter dir her waren, verlieren dich. Deine Abschussansprüche werden freigegeben, sobald du dich tarnst.
- **Raketen.** Niemand kann eine gelenkte Rakete auf dich aufschalten, und eine geradeaus fliegende Einzelziel-Rakete fliegt durch dich hindurch. Ein **Flächenschaden** trifft ein Schiff in seinem Bereich trotzdem und beendet dessen Tarnung, und die Piloten, die den Ort des Schiffs sehen können, bekommen ihn angezeigt, bevor die Schadenszahl erscheint. Das Abfeuern einer Rakete ist ein Schuss: Es beendet deine eigene Tarnung wie eine Salve (die CPU lädt sich dann die oben genannten 60 Sekunden auf) und hindert dich, ob getarnt oder nicht, 10 Sekunden danach daran, dich zu tarnen.
- **Das Schwarze Loch** verschluckt ein getarntes Schiff wie jedes andere, und die Karte bekommt es mit.
- **Was du siehst.** Dein Schiff wird durchsichtig und bekommt einen gestrichelten violetten Umriss, und ein Chip oben auf dem Bildschirm sagt „Getarnt“ mit den übrigen Nutzungen (keine Sekunden: Es gibt keinen Timer). Der CLK-Slot zeigt die übrigen Nutzungen; solange du getarnt bist, leuchtet er violett und zeigt AN, und wenn die Tarnung endet, egal wie, dunkelt er ab und zählt die 60 Sekunden Aufladung herunter. Ein Druck, den der Server ablehnt (Aufladung, Schutzzone, ein Treffer oder Schuss in den letzten 10 Sekunden), lässt den Slot rot aufblitzen, und eine Meldung sagt dir, warum. Ein Verbündeter erscheint als blasser Geist mit einem Geistersymbol vor seinem Namen, und ein Pilot, der sich in deiner Nähe tarnt, verschwindet in einer Welle. Ziehe CLK aus den Extras der Aktionsleiste auf einen Slot, um es zu nutzen, wie REP.
- **Nutzungen** werden mit der CPU gespeichert. Ausloggen, Sterben oder ein Neustart des Spiels geben keine zurück, und eine Aktivierung, die du abbrichst, ist trotzdem verbraucht. Wenn die letzte Nutzung eines Pakets weg ist, ist es aufgebraucht, und sein Slot wird aus einer Reserve derselben CPU in deinem Inventar aufgefüllt, falls du eine besitzt.
- **Mehrere CPUs** in einer Konfiguration addieren sich nicht. Die mit den wenigsten verbleibenden Nutzungen wird zuerst benutzt.

S, M und L verhalten sich gleich: Die größeren Pakete sind nur pro Nutzung günstiger (500, 450 und 400 Thulium).

## EMP Charge {#emp-charge}

Drücke den EMP-Slot im Kampf. **3 Sekunden** lang kann dich niemand anvisieren, und **jeder, der dich anvisiert hatte, verliert die Zielerfassung** sofort, wo auch immer er ist: Piloten, Aliens und Konzernpiloten. Einem Piloten, dessen Zielerfassung abbricht, wird „Zielerfassung verloren: Das Ziel hat einen EMP eingesetzt“ gemeldet. Wer in diesen 3 Sekunden versucht, dich anzuvisieren, wird abgewiesen.

- **Er macht dich nicht unverwundbar.** Er stoppt, was eine Zielerfassung braucht: Laser, gelenkte Raketen und die Berührung einer geradeaus fliegenden Einzelziel-Rakete, die durch dich hindurchfliegt. Ein **Flächenschaden** braucht keine Zielerfassung, er trifft dich also weiterhin, wenn du darin stehst, und das Schwarze Loch ist überhaupt kein Schuss.
- **Du kannst weiter handeln.** Feuern beendet ihn nicht. Du kannst dich tarnen (wenn die eigenen Regeln der Tarnung es zulassen) und andere Extras benutzen.
- **Er beendet Tarnungen in deiner Nähe.** Jedes Schiff, das im Moment des Impulses im Umkreis von **1.500 Einheiten** um dich getarnt ist, wird sofort sichtbar, und seine CPU beginnt ihre 60 Sekunden Aufladung, egal zu welchem Konzern es gehört, deinem eigenen eingeschlossen; die Schiffe deiner eigenen [Gruppe](/wiki/03-Mechanics/Groups.md) sind die Ausnahme: Sie behalten ihre Tarnung. Dem Piloten wird „Tarnung unterbrochen: In der Nähe wurde ein EMP ausgelöst.“ gemeldet, er sieht sein Schiff mit derselben Welle wieder auftauchen wie bei jeder Enttarnung, und der Slot beginnt seine Aufladung. Du kannst keinen EMP einsetzen, während du selbst getarnt bist.
- **Er verbirgt nichts.** Alle sehen dich weiterhin, 3 Sekunden lang mit einem knisternden elektrischen Mantel.
- **Einsetzen kannst du ihn nicht**, solange dich eine Schutzzone schützt, solange du getarnt bist oder innerhalb von **30 Sekunden** nach dem letzten. Überall sonst funktioniert er, auch in den ersten Tagen einer Saison (dem Friedensprotokoll): Aliens jagen dann weiterhin.
- Ein Alien, das du in diesen 3 Sekunden triffst, wendet sich erst nach deren Ablauf gegen dich. Deine Abschussansprüche und die Regeln des Ersttreffers ändern sich nicht.
- **Was du siehst.** Ein Impuls gekrümmten Raums rast vom Piloten nach außen, so weit, wie der Impuls Tarnungen beendet (1.500 Einheiten), alle in Reichweite sehen ihn, und ein knisternder elektrischer Mantel umgibt das Schiff 3 Sekunden lang, mit einem Ring um dein eigenes Schiff und einem Chip oben auf dem Bildschirm, die die Zeit mitzählen. Der Zielring von allen, die dich ausgewählt hatten, bricht mit einem kurzen Knacken auseinander. Der EMP-Slot zeigt die Ladungen, die du besitzt, leuchtet blau, solange der Mantel steht, und dunkelt ab, während er sich auflädt.
- **Eine Ladung, eine Nutzung.** Der Slot wird aus deinem Inventar aufgefüllt, wenn du mehr besitzt. Die **30 Sekunden** Aufladung werden nicht gespeichert: Ausloggen oder ein Sprung durch ein Portal löscht sie, und der nächste Impuls kostet eine Ladung.
