<!-- wiki-i18n source: 6b964707b3b7ca22 -->
<!-- wiki-i18n title: Riesenbagger -->
# Riesenbagger {#giant-excavator}

<!-- wiki-search: excavator; giant excavator; pulsar; mining; fuel; excavator fuel; control panel; overheat; radiation; slumbering void; voids; wave; ds-1; ds-2; ds-3; riesenbagger; bagger; treibstoff; strahlung; überhitzung; bedienfeld -->

Ab dem ersten Tag der Saison leuchtet in den Gefahrensektoren `DS-1`, `DS-2` und `DS-3` je ein **Pulsar**, und ab Saisontag 11 steht ein **Riesenbagger** neben ihm. Der Bagger baut den Pulsar nach **Thulium und seltenen Erzen** ab und verbrennt dafür [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md). Jeder darf ihn betanken, wählen, was er abbaut, und ihn starten, und alles, was er ausspuckt, liegt in Kisten um ihn herum, die jeder nehmen darf. Ein Durchlauf ist allerdings laut: Die ganze Welt erfährt, wenn er beginnt, **Slumbering Voids** kommen in Wellen auf ihn zu, und ein Bagger, der zu lange gearbeitet wird, überhitzt und verstrahlt die ganze Umgebung. Diese Seite sagt, wie ein Durchlauf abläuft, was er liefert und wie du ihn überlebst. Die Sektoren stehen in [Gefahrensektoren](/wiki/01-General/Danger-Sectors.md); die Voids in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

![The giant excavator's sheet: the fuel tank, the heat, the resource to mine, the excavator's hull and the Voids of the next wave](../../img/wiki-img/shots/excavator-sheet.jpg)

## Auf einen Blick {#at-a-glance}

<!-- excavator-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Wo**: Ein Pulsar mit einem Riesenbagger in jedem der Sektoren `DS-1`, `DS-2` und `DS-3`, in jeder Welt
- **Erscheint**: Der Pulsar ab dem ersten Tag der Saison, der Bagger ab Saisontag 11 bis zum Wipe
- **Treibstoff**: Dark Matter. Eines brennt 10 min lang; der Tank fasst 3, das sind 30 min Abbau. Jeder darf eines nach dem anderen aus der eigenen Fracht hinzufügen
- **Bedienfeld**: Das Fenster funktioniert im Umkreis von 600 Einheiten um den Bagger, sein Schriftzug erscheint ab 1.400 Einheiten. Jeder darf betanken, wählen und starten; die Wahl ist gesperrt, solange er läuft
- **Kisten**: Alle 20 s eine Kiste, 450 bis 900 Einheiten vom Bagger entfernt, ab dem ersten Moment für jeden frei. Sie liegt 5 min, und höchstens 24 liegen gleichzeitig auf einer Karte
- **Hitze**: 30 min Abbau, in so vielen Durchläufen wie nötig, und der Bagger überhitzt für 1 h. Die Hitze bleibt zwischen den Durchläufen erhalten und ist nach der Ruhezeit weg
- **Strahlung**: Solange er überhitzt oder zerstört ist, verbrennen der Bagger (im Umkreis von 1.100 Einheiten) und sein Pulsar (im Umkreis von 1.300 Einheiten) jedes Schiff darin: 10 % seiner gesamten HP pro Sekunde
- **Hülle**: 200.000 HP in Alpha, 300.000 in Beta und 400.000 in Gamma. Nur Slumbering Voids können ihn beschädigen, und nur wenn kein Pilot mehr da ist, der ihn verteidigt
- **Voids**: 2 Slumbering Voids alle 2 min, solange er abbaut, die ersten 1 min nach dem Start; höchstens 8 lebend auf einer Karte
- **Meldungen**: Die Piloten der ganzen Welt erfahren, wann ein Durchlauf startet, wann der Bagger überhitzt und wann er zerstört wird; der Rest geht an die Piloten seines Sektors. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats und im Spielprotokoll, nicht in **Global** oder **Lokal**.

<!-- excavator-glance:end -->

## So läuft ein Durchlauf {#how-a-run-goes}

1. **Finde einen.** Ab Saisontag 11 hat jeder der drei Gefahrensektoren mit einem Pulsar einen Bagger, in jeder Welt. Ein Schriftzug, **Bagger**, schwebt über ihm, wenn du in der Nähe bist, und die Sternensystem-Karte markiert jeden Gefahrensektor, der einen hat: Die Farbe der Markierung ist der Zustand seines Baggers, ihr Tooltip nennt die Zeit bis zur nächsten Änderung.
2. **Öffne das Bedienfeld.** Klicke auf den Schriftzug. Das Fenster **Riesenbagger** funktioniert, solange dein Schiff in Reichweite des Bedienfelds ist (die Liste *Auf einen Blick* nennt sie). Auch ein getarntes Schiff kann es benutzen, und das Benutzen beendet die Tarnung nicht.
3. **Betanke ihn.** **Dark Matter hinzufügen** legt ein Dark Matter aus deiner Fracht in den Tank. Das kann jeder. Der Tank nimmt nie mehr auf, als der Bagger noch verbrennen kann, bevor er überhitzt, sodass kein Treibstoff verschwendet wird.
4. **Wähle, was abgebaut wird,** aus der Liste und drücke dann **Abbau starten**. Dafür braucht es mindestens ein Dark Matter im Tank und eine Ressource. Bis zum Start kann jeder die Wahl ändern; sobald er läuft, ist die Ressource gesperrt. Der Start wird jedem Piloten der Welt gemeldet, mit deinem Namen, dem Sektor und der Ressource.
5. **Halte ihn.** Solange er abbaut, fällt alle paar Sekunden eine Kiste rund um den Bagger, und kurz nach dem Start treffen die ersten Slumbering Voids ein. Verteidige den Bagger und nimm die Kisten.
6. **Behalte die Hitze im Blick.** Die Hitzeleiste füllt sich, solange der Bagger abbaut, und leert sich nie, solange er wartet. An ihrer Grenze überhitzt der Bagger. Geh vorher: Das Spiel warnt die Karte zweimal.
7. **Er ruht.** Überhitzt oder zerstört, sind der Bagger und sein Pulsar verstrahlt, bis die Ruhezeit vorbei ist; dann ist er wieder bereit, mit leerer Hitze und voller Hülle.

Das Fenster zeigt außerdem den Sektor, den Tank (eine Zelle für jedes Dark Matter, die brennende teilweise gefüllt), wie viel Dark Matter du trägst, die Hülle des Baggers, was jede Ressource in deiner Welt pro Minute liefert und, solange er abbaut, die Zeit bis zur nächsten Welle und die lebenden Voids. Wird etwas abgelehnt, liest du den Grund in Rot: Du bist zu weit vom Bedienfeld entfernt, du hast kein Dark Matter, der Tank ist voll, es gibt noch keinen Treibstoff oder keine gewählte Ressource, die Ressource ist gesperrt, solange er läuft, oder der Bagger ist heiß.

| Zustand | Was das ist | Was du tun kannst |
| :--- | :--- | :--- |
| **Bereit** | Kein Treibstoff, oder Treibstoff und nicht gestartet. Die bisherige Hitze bleibt. | Dark Matter hinzufügen, wählen, starten. |
| **Abbau läuft** | Er verbrennt Dark Matter und sammelt Hitze; die Ressource ist gesperrt. | Weiteres Dark Matter bis zum freien Platz hinzufügen, die Voids bekämpfen, die Kisten nehmen. |
| **Überhitzt** | Die Hitze hat ihre Grenze erreicht. Der Tank ist geleert; die schon gelegten Kisten bleiben. | Nichts. Das Gebiet ist verstrahlt: Bleib draußen. |
| **Zerstört** | Voids haben die Hülle auf null gebracht. Der Treibstoff ist verloren, die Hülle sofort wieder voll. | Nichts. Das Gebiet ist verstrahlt: Bleib draußen. |

Geht der Treibstoff vor der Grenze aus, kehrt der Bagger mit behaltener Hitze zu **Bereit** zurück, und die übrigen Voids verschwinden nach einer Weile, sofern sie nicht kämpfen.

## Was er abbaut {#what-it-mines}

Ein voller Tank liefert ungefähr so viel, wie fünf Piloten in einer halben Stunde bestem Thulium-Farmen verdienen würden. Beta und Gamma liefern mehr, so wie sie für jeden Abschuss mehr zahlen. Du wählst eine Ressource pro Durchlauf. Eine Kiste ist für alle gleich, und eine Thulium-Kiste ist Bargeld, das beim Aufnehmen ausgezahlt wird, wie das Thulium der Asteroiden.

<!-- excavator-resources:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Ein voller Tank (3 Dark Matter, 30 min Abbau) liefert die Mengen unten, in 90 Kisten.

| Ressource | Alpha | Beta | Gamma | Eine Minute, in Alpha | Eine Kiste, in Alpha |
| :--- | ---: | ---: | ---: | ---: | ---: |
| [Thulium](/wiki/06-Items/Resources.md#thulium) | 9.643 | 15.429 | 19.286 | 321,4 | 107,1 |
| [Cataclysite](/wiki/06-Items/Resources.md#cataclysite) | 2.314 | 3.703 | 4.629 | 77,1 | 25,7 |
| [Quorvium](/wiki/06-Items/Resources.md#quorvium) | 1.029 | 1.646 | 2.057 | 34,3 | 11,4 |
| [Velkonite](/wiki/06-Items/Resources.md#velkonite) | 640 | 640 | 640 | 21,3 | 7,1 |
| [Orvium](/wiki/06-Items/Resources.md#orvium) | 320 | 320 | 320 | 10,7 | 3,6 |

- Ein Durchlauf mit Velkonite oder Orvium liefert höchstens 8 Stunden eines Sammlers der Stufe 20 des [Skylab](/wiki/03-Mechanics/Skylab.md) für dieses Erz (640 Velkonite, 320 Orvium), in jeder Welt: Es sind die Erze des Skylab, und ein Durchlauf beschleunigt dessen Tempo nie um mehr als das.
- Eine Kiste enthält etwa die Menge der letzten Spalte, 15 % mehr oder weniger. Eine Thulium-Kiste ist Bargeld: Das Aufnehmen zahlt es aus. Eine Erzkiste enthält den Gegenstand.

<!-- excavator-resources:end -->

Die eigenen Booster des Piloten wirken wie bei jeder Fracht: Der Bonus des Resource Magnet Booster erhöht eine Erzkiste. Es gibt kein Tageslimit für die Kisten: Treibstoff und Zeit begrenzen einen Durchlauf.

**Wofür das Erz gut ist.** Das Erz einer Kiste kommt wie jeder Gegenstand in deine Fracht. Cataclysite und Quorvium werden in der Montage und in der Schmiede gebraucht ([Ressourcen](/wiki/06-Items/Resources.md)). Die Schmiede und das Forschungszentrum des Skylab nehmen Velkonite und Orvium nur aus dem Ressourcenlager, das die Sammler füllen; das Erz einer Kiste nützt in deiner Fracht also nichts: Parke dein Schiff, dann verlädt die [Erzbucht](/wiki/03-Mechanics/Skylab.md#ore-bay) deines Skylab (Kern-Level 10) es ins Lager, bis zu ihrem Kontingent pro Stunde, und von dort nehmen es die Schmiede und das [Forschungszentrum](/wiki/03-Mechanics/Research.md#fuel).

## Die Slumbering Voids {#the-slumbering-voids}

Ein Durchlauf zieht **Slumbering Voids** an, Jäger der verlorenen Zivilisation, die vom Kartenrand heranfliegen, um den Pulsar vor jedem zu schützen, der ihn leeren will. Sie jagen die Piloten in der Nähe des Baggers, und wenn niemand mehr zu jagen ist, gehen sie auf den Bagger los. Die Zahlen des Voids und seine Bezahlung stehen in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).

<!-- excavator-voids:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Wellen.** 2 Slumbering Voids alle 2 min; die ersten 1 min nach dem Start, und keine in den letzten 1 min eines Durchlaufs. Höchstens 8 leben gleichzeitig auf einer Karte: Eine Welle, die die Karte voll vorfindet, fällt aus.
- **Anflug.** Eine Welle erscheint am Kartenrand, 900 Einheiten innerhalb und mindestens 2.500 Einheiten von jedem Torring entfernt, und fliegt in etwa 20 s zum Bagger. Die Meldung nennt die Seite der Karte, von der sie kommt.
- **Jagd.** Ein Void jagt den nächsten Piloten, den er im Umkreis von 2.500 Einheiten sehen kann, und bleibt im Umkreis von 7.000 Einheiten um den Bagger.
- **Belagerung.** Ist 15 s lang kein Pilot, den sie sehen können, im Umkreis von 7.000 Einheiten um den Bagger, greifen die Voids den Bagger an, und jeder Laser richtet 25 % seines üblichen Schadens an. Bei null ist der Bagger zerstört: Sein Treibstoff ist verloren, seine Hülle sofort wieder voll, und er ruht 1 h.
- **Abzug.** Endet ein Durchlauf, bleiben die übrigen Voids noch 90 s und kämpfen weiter, wenn man gegen sie kämpft; dann ziehen sie ab.

<!-- excavator-voids:end -->

- **Ein Void ist eine Glaskanone.** Sein Schild ist groß, nimmt aber 80 % eines Treffers auf, sodass die Hülle dahinter nach wenigen Malen ihrer Größe an Schaden weg ist, und mit Schildpenetration viel früher. Zwei oder drei gut ausgerüstete Piloten halten einen Durchlauf in Alpha; Beta und Gamma brauchen größere Gruppen, wie bei jedem Alien.
- **Eine Tarnung schützt den Ort nicht.** Die Voids sehen getarnte Schiffe nicht, ein Pilot, der sich versteckt, hält sie also nicht vom Bagger fern; und ein Pilot, der sich in einem Torring versteckt, ist nicht erreichbar und zählt ebenfalls nicht.
- **Jeder Void zahlt** nach dem Schaden, den du ihm zugefügt hast, und lässt eine Kiste fallen ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Ihre Abschüsse zählen für deine PvE-Rangpunkte wie die eines Schwarmschiffs.

## Hitze und Strahlung {#heat-and-radiation}

Der Abbau erzeugt Hitze, Sekunde für Sekunde. Die Hitze **summiert sich und kühlt nie ab, solange der Bagger wartet**: Ein Durchlauf, der früh endet, hinterlässt dem nächsten Piloten einen kürzeren. Erreicht sie die Grenze, **überhitzt** der Bagger, und wird seine Hülle auf null gebracht, wird er **zerstört**; in beiden Fällen strahlen der Bagger und sein Pulsar, bis die Ruhezeit vorbei ist.

<!-- excavator-radiation:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Kreis | Radius | Gesamte HP pro Sekunde | Ein volles Schiff hält |
| :--- | ---: | ---: | ---: |
| Der Riesenbagger | 1.100 | 10 % | 10 s |
| Der Pulsar | 1.300 | 10 % | 10 s |

- **Die Dosis.** 10 % der gesamten maximalen HP eines Schiffs (Hülle plus Schild) pro Sekunde, ein volles Schiff hält also 10 s, egal welcher Klasse. Der Schild nimmt sie zuerst auf, und seine Absorption zählt nicht.
- **Wen.** Jedes Schiff in den Kreisen, auch getarnte; keine Aliens. Es ist erlittener Schaden: Eine Reparaturdrohne stoppt und der Schild lädt nicht nach, wie beim Schwarzen Loch.
- **Gutschrift.** Ein Pilot, der verbrennt, wird dem letzten Feind gutgeschrieben, der ihn in den 15 s davor getroffen hat.
- **Warnungen.** Die Karte wird 1 min und 15 s vor der Überhitzung informiert.

<!-- excavator-radiation:end -->

- **Die Warnung.** Zweimal vor der Überhitzung (die Zeiten stehen in der Liste oben) wird die Karte informiert, ein Schiff in den Kreisen sieht eine Warnung, und die Kreise werden im Flug auf den Boden und auf die Minikarte gezeichnet. Wenn sie strahlen, sind die Kreise rot, und die Strahlungsanzeige zeigt die Dosis.
- **Verlassen.** Jedes Serienschiff kann vom Rand des Bedienfelds oder von der entferntesten noch liegenden Kiste aus herausfliegen, außer der langsamen Ironclad: Sie verlässt das Gebiet während der Warnung, oder sie verlässt es nicht. Steh nicht auf einer Kiste, wenn die Hitze ausgeht.
- **Beute in den Kreisen.** Kisten, die vor der Überhitzung gelegt wurden, bleiben in der Strahlung liegen: Eine Kiste, die dort liegt, wenn sie beginnt, kostet beim Aufnehmen die Dosis.
- **Ein Neustart des Servers** pausiert einen Durchlauf: Treibstoff und Hitze kommen zurück, wie sie waren, die Ruhezeit läuft nach der Uhr weiter, und die erste Welle nach dem Neustart kommt eine Minute später.

## Um einen Durchlauf kämpfen {#fighting-over-a-run}

Der Bagger hat **keinen besonderen Ring**: Es gelten die normalen Regeln deiner Welt, Rivalen können also kommen, auf dich schießen und die Kisten nehmen (eine Kiste ist vom ersten Moment an für jeden frei). Stehlen und Hinterhalte gehören zum Event. Worauf du dich einstellen solltest:

- **Wer betankt, gewinnt nicht automatisch.** Jeder darf betanken, wählen und starten; ein Rivale kann die Ressource ändern, bevor du auf Start drückst. Prüfe die Wahl, bevor du drückst.
- **Der Treibstoff ist in Gefahr.** Wird der Bagger zerstört, ist das Dark Matter in seinem Tank verloren, und niemand bekommt es zurück. Verlieren kannst du höchstens den vollen Tank.
- **Bring eine Gruppe mit** und sprecht ab, wer beim Bagger bleibt und wer die Kisten nimmt, und behalte die Hitze im Auge: Die Piloten, die die letzten Kisten nehmen, erwischt die Strahlung.
- **Die Voids kommen zum Bagger, nicht zu den Kisten.** Eine Gruppe, die den Bagger hält, beschäftigt die Voids; wer abwandert, überlässt ihn der Belagerung.

## Was die Welt erfährt {#what-the-world-is-told}

Das sind Systemzeilen (sie erscheinen im Tab **System** des Chats und im Spielprotokoll, nicht in **Global** oder **Lokal**). Die ersten drei gehen an die ganze Welt; die letzte an die Piloten im Sektor des Baggers.

- An dem Tag, an dem Event 2 beginnt: Die Gefahrensektoren haben sich verändert.
- Ein Pilot **startet** einen Bagger, mit Sektor, Ressource und den Minuten an Treibstoff.
- Der Bagger **überhitzt** oder wird **zerstört**.
- Der Treibstoff geht aus; der Bagger überhitzt gleich (zweimal gemeldet); eine **Welle** von Voids kommt, mit ihrer Nummer und der Seite der Karte, von der sie kommt; kein Pilot ist mehr da, also greifen die Voids den Bagger an.

Jede Aktion am Bedienfeld und jede Warnung hat einen eigenen leisen Ton auf der Effektlautstärke.

## Weiterlesen {#where-to-read-more}

- [Gefahrensektoren](/wiki/01-General/Danger-Sectors.md): wo die Pulsare stehen und was sonst neu ist.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): der Slumbering Void, die Inert Mass und der Unwakened.
- [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md) und [Das Schwarze Loch](/wiki/03-Mechanics/Black-Hole.md): woher der Treibstoff kommt.
- [Ressourcen](/wiki/06-Items/Resources.md): die Erze, die der Bagger liefert.
- [Frachtkisten](/wiki/03-Mechanics/Cargo.md): Kisten, Aufnehmen und der Resource Magnet Booster.
- [Ränge](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points): die PvE-Punkte eines Voids.
