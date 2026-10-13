<!-- wiki-i18n source: 6be933cc7ba8434b -->
<!-- wiki-i18n title: Frachtkisten -->
# Frachtkisten {#cargo-boxes}

Zerstörte Aliens hinterlassen ihre Beute im Weltraum als leuchtende Frachtkisten. Flieg hin und sammle sie ein, bevor es jemand anderes tut.

![Picking up a cargo box: the channel bar fills while the ship stays near](../../img/wiki-img/shots/cargo-pickup.jpg)

## Was Kisten hinterlässt {#what-drops}

- **Aliens** lassen ihre Beute als eine Kiste dort fallen, wo sie explodiert sind: die Ressourcen und Teile, die bei jedem Alien unter *Beute* aufgeführt sind (siehe die Artikel zu den [Aliens](/wiki/04-Aliens/Phantasm.md)). Credits, Thulium, EP und Ehre werden weiterhin in dem Moment ausgezahlt, in dem du den Abschuss machst. Ein Alien, dessen Beute nichts auswürfelt (ein Seeker in vier von fünf Fällen), hinterlässt keine Kiste.
- **Konzernpiloten** hinterlassen keine Kiste, wenn sie zerstört werden, egal wer oder was sie zerstört. Siehe [Konzernpiloten](/wiki/03-Mechanics/Company-Pilots.md).
- **Schiffe von Spielern** hinterlassen weder Wrack noch Kiste, wenn sie zerstört werden, egal wer oder was sie zerstört, und dem Piloten wird nichts aus dem Inventar genommen.
- **Das Schwarze Loch** legt für eine hineingeschossene N.I.K.E.-Rakete Kisten mit **Dark Matter** an den Rand seiner Zone (siehe [Das Schwarze Loch](/wiki/03-Mechanics/Black-Hole.md)). Sie sind die einzige Art von Kiste, die innerhalb des Rings des Lochs liegt.
- **Die Anführer der [Schwärme](/wiki/05-Swarms/Swarms.md) und die Dormant Pulses** lassen eine eigene Kiste mit Munition, Raketen und Ressourcen fallen. Sie ist für den Piloten reserviert, der dem Schiff den meisten Schaden zugefügt hat (und für dessen Clan), nicht für den, der es als Erster getroffen hat.
- **Ein [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot)** lässt keine solche Kiste fallen: Jeder Pilot, der mindestens 5 % des Schadens verursacht hat, bekommt eine eigene [private Kiste](#private-boxes) mit seinem Anteil an der Beute.
- **[Asteroiden](/wiki/03-Mechanics/Asteroid-Mining.md)** hinterlassen **Brocken** statt einer Kiste: kleine Nuggets und Kristalle mit Credits und Thulium und einen Stein mit Erz. Die Credits und das Thulium werden beim Einsammeln eines Brockens ausgezahlt, nicht beim Zerbrechen des Asteroiden, und es gilt ein Limit je 24 Stunden. Ein Brocken wird eingesammelt wie eine Kiste, und er ist für die Piloten reserviert, die ihn verdient haben, und dann frei, wie eine Kiste.

Ein Alien, das ein Konzernpilot erledigt, lässt seine Beute für den Piloten fallen, dem der Abschuss zählt (den, der seinen Anspruch hält, sonst den Piloten seines Konzerns, der es bekämpft); ein Alien, gegen das ein Konzernpilot allein gekämpft hat, lässt nichts fallen, da Konzernpiloten nie einsammeln.

Die Lichter der Kiste nehmen die Farbe des seltensten Gegenstands darin an: Türkis für gewöhnliche Beute, dann Grün, Blau, Violett, Rosa, Gold und Orangerot von ungewöhnlich bis ewig.

## Einsammeln {#collecting}

- **Linksklick** auf eine Kiste: Dein Schiff fliegt hin und nimmt sie auf, sobald sie in Reichweite ist (200 Einheiten). Ein Klick auf eine Kiste zählt nie als Bewegungsbefehl; jeder andere Bewegungsbefehl (ein Klick in den Weltraum, auf die Minikarte) bricht das Einsammeln ab. Liegt auch ein Schiff oder Alien direkt unter dem Mauszeiger, geht der Klick an das, was dem Mauszeiger näher ist, damit ein Gefecht, das über eine Kiste hinwegzieht, seine Ziele behält.
- **Das Einsammeln dauert eine halbe Sekunde.** Sobald dein Schiff in Reichweite ist und die Kiste nehmen darf, beginnt es: Ein Balken über deiner Aktionsleiste („Einsammeln…“) füllt sich, und ein Strahl scannt die Kiste. Dein Schiff fliegt weiter, und die Kiste gehört dir, wenn der Balken voll ist. Fliegst du aus der Reichweite oder verlierst die Kiste an einen anderen Piloten, wird das Einsammeln abgebrochen. Angegriffen zu werden unterbricht es nirgends.
- Du tust immer nur eins auf einmal: Während du [springst](/wiki/01-General/Spacemap%20Travel.md), kannst du nichts einsammeln, und ein Sprung, den du startest, gibt das Einsammeln auf. Dieselbe Kiste noch einmal anzufordern, während du sie schon einsammelst, ändert nichts.
- Zeige auf eine Kiste, um zu sehen, was darin ist, für wen sie reserviert ist und, in ihrer letzten Minute, wie lange sie noch da ist.
- Beim Einsammeln einer Kiste ertönt dort, wo sie lag, ein kurzer Aufnahmeton; auch das Einsammeln anderer Piloten in der Nähe hörst du, leiser.
- Was du einsammelst, geht direkt in dein Hangar-Inventar, auf deinen losen Stapel dieses Gegenstands (nie auf Ausrüstung oder etwas im Transport-Cache). Eine Toast-Meldung zeigt dir, was du bekommen hast; Kisten, die du nacheinander einsammelst, addieren sich in derselben Meldung.
- Was du einsammelst, ist **handelbar**: Du kannst es in der [Auktion](/wiki/03-Mechanics/Auction.md#marketable-items) verkaufen.
- Gehört dir ein Brocken eines [Asteroiden](/wiki/03-Mechanics/Asteroid-Mining.md), fliegt dein Schiff von selbst zum nächsten Brocken in Reichweite, den du nehmen darfst; jeder Bewegungsbefehl von dir stoppt das.
- **Ein Retriever sammelt für dich ein.** Ein angedocktes [Retriever](/wiki/03-Mechanics/Pets.md#the-retriever)-P.E.T. nimmt Kisten ohne Klick auf, in einer eigenen Reichweite (von 255 Einheiten beim schwächsten bis 880 bei einem Legendary auf Level 20, gegenüber den 200 deines eigenen Einsammelns), die nächste zuerst und **eine nach der anderen, jede eine halbe Sekunde**: nie schneller als eine Hand. Er nimmt nur, was du selbst nehmen darfst: Eine für einen anderen Piloten reservierte Kiste wartet, bis die Zeit um ist, und die [private Kiste](#private-boxes) eines anderen Piloten rührt er nie an. Er arbeitet, solange du außerhalb einer Schutzzone fliegst, untätig oder nicht, aber nicht, solange du getarnt bist oder springst, also beendet er nie eine Tarnung. Er ist kein Kanal: Kein Balken füllt sich, und er blockiert nie dein eigenes Einsammeln oder deine Sprünge, und eine Kiste, die du gerade von Hand einsammelst, überlässt er dir. Erreichen deine Hand und dein Retriever eine Kiste zugleich, bekommt sie genau einer. Ein Einsammeln durch einen Retriever spielt statt des Aufnahmetons einen eigenen kleinen Piepton.

## Wer sie bekommt {#who-gets-it}

- Der Pilot, dem der Abschuss ausgezahlt wird, und die Mitglieder seines **Clans** haben die Kiste **30 Sekunden** lang für sich allein. Bei einem Alien ist das der Pilot, der den Anspruch hält, also der, der es als Erster getroffen hat (siehe [Kampf](/wiki/03-Mechanics/Combat.md)), egal wer es erledigt hat. Andere Piloten sehen sie abgedunkelt und können sie noch nicht nehmen; ein Schiff, das zu ihr geschickt wurde, wartet in der Nähe, bis die Zeit um ist.
- Danach darf **jeder** auf der Karte sie nehmen.
- Nur ein Schiff auf der Karte der Kiste kann sie nehmen: Wirst du auf dem Weg (oder in der halben Sekunde, die das Einsammeln dauert) zerstört, springst du oder loggst du dich aus, bleibt die Kiste für die anderen liegen.
- Sammeln zwei Piloten dieselbe Kiste gleichzeitig ein, bekommt sie der, dessen Einsammeln zuerst fertig ist, genau einmal; der andere erfährt, dass sie weg ist.
- Eine Kiste, die niemand nimmt, treibt nach **3 Minuten** davon (in den letzten 10 Sekunden blinkt sie). Eine Karte fasst höchstens 64 Kisten; würde eine neue diese Zahl überschreiten, verschwindet die älteste. Asteroiden-Brocken haben innerhalb der 64 einen eigenen Pool: Sie verdrängen keine andere Kiste, und keine andere Kiste verdrängt einen Brocken ([die Regeln](/wiki/03-Mechanics/Asteroid-Mining.md#the-rules)). Dark-Matter-Kisten halten 4 Minuten und gehören in der ersten Minute dir allein. Die Kisten eines [Riesenbaggers](/wiki/03-Mechanics/Giant-Excavator.md) sind ab dem ersten Moment für jeden frei, halten länger als eine Kiste sonst und haben einen eigenen Pool, sie verdrängen also nie eine andere Kiste.

## Private Kisten {#private-boxes}

Die Beute eines [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) ist nicht eine Kiste für einen Piloten: **Jeder Pilot, der mindestens 5 % des Schadens verursacht hat, bekommt eine eigene Kiste**, ausgewürfelt für seinen Anteil (für 20 % des Schadens etwa ein Fünftel jeder Menge; [die Einzelheiten](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot)).

- **Nur du siehst sie, und nur du kannst sie einsammeln.** Dein Clan und deine Gruppe sehen sie nicht und können sie nicht nehmen; für alle anderen ist sie schlicht nicht da. Auf deinem Bildschirm hat sie einen dünnen Ring unter sich.
- **Sie liegt 10 Minuten** ab dem Abschuss, und die ganze Zeit gehört sie dir: Es gibt keine Wartezeit von 30 Sekunden. Danach treibt sie davon wie jede Kiste. Das Spielprotokoll nennt dir deinen Anteil an der Beute, wenn der Wächter fällt.
- **Sie verdrängt keine anderen Kisten.** Private Kisten haben einen eigenen Pool neben den 64 einer Karte (höchstens 32), sodass der Abschuss eines Wächters nie den Platz einer anderen Kiste einnimmt und eine volle Karte dich nie deine Kiste kostet.
- Das Einsammeln ist wie bei jeder Kiste ([oben](#collecting)): Dein Schiff fliegt hin, und das Einsammeln dauert eine halbe Sekunde. Dein Retriever nimmt auch deine privaten Kisten auf, und niemandes sonst.

## Booster {#boosters}

- **Loot Luck Booster** (und der dauerhafte Buff Glücks-Boost sowie das Glück deiner angedockten [P.E.T.s](/wiki/03-Mechanics/Pets.md)) erhöhen die Chance jedes Beute-Eintrags, wenn der Schütze den Abschuss macht.
- **Resource Magnet Booster** fügt den Ressourcen in jeder Kiste, die du einsammelst, **25 %** hinzu, von Hand oder mit einem Retriever, egal wer den Abschuss gemacht hat. Dark Matter ist die Ausnahme: Der Magnet fügt ihm nichts hinzu, daher sind fünf N.I.K.E.s für alle zehn Dark Matter.
