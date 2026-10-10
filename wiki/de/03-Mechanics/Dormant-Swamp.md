<!-- wiki-i18n source: ee049111031a8060 -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; sumpf; geschütz; geschütze; turm; türme -->

Vor langer Zeit lebte mitten in der Galaxie eine fortgeschrittene Zivilisation. Sie baute in violettschwarzem Kristall mit leuchtenden violetten Adern, und aus einem Grund, den niemand kennt, ist sie untergegangen. Der **Dormant Swamp** ist ihr Außenposten, in der oberen linken Ecke von `DS-4`. Ab Saisontag 11 regt er sich: Geschütze in der Mitte feuern auf jedes Schiff, das sie sehen, **Inert Masses** bewachen ihn, und ganz in der Mitte schläft **der Unwakened**. Es ist ein Ort, den Piloten **noch nicht besuchen sollen**. Unter Tarnung kannst du bis zum Unwakened fliegen, und mehr kann dort vorerst nicht getan werden: Die Basis und ihre Geschütze können nicht beschädigt, betreten, geentert oder mit ihnen gehandelt werden.

Am Sumpf erscheint ab Tag 11 auch der [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md), und **Slumbering Voids** patrouillieren um ihn herum. Dieselben Voids kommen in Wellen zu den [Riesenbaggern](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). Die Sektoren stehen in [Gefahrensektoren](/wiki/01-General/Danger-Sectors.md).

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## Auf einen Blick {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Wo**: Die obere linke Ecke von `DS-4`: Die Mitte liegt bei 5.000 / 5.000
- **Erscheint**: Ab Saisontag 11 bis zum Wipe
- **Die Zone**: 4.300 Einheiten um die Mitte: so weit reichen die Geschütze höchstens, und der Ort, den noch niemand besuchen soll
- **Der Hinweis**: Ein Schiff, das den Ring 4.800 Einheiten von der Mitte überquert, erhält eine Systemzeile
- **Tarnung**: Kein Geschütz sieht je ein getarntes Schiff oder eines im Fenster eines EMP
- **Die Aliens**: 5 Inert Masses bleiben im Umkreis von 2.400 Einheiten um die Mitte. Der Unwakened schläft in der Mitte. 2 Slumbering Voids patrouillieren zwischen 4.600 und 6.500 Einheiten von der Mitte.
- **Der Dormant-Schwarm**: Er erscheint bei 9.417 / 6.606, 4.700 Einheiten von der Mitte entfernt und außerhalb der Zone
- **Felsen**: Kein Asteroid liegt im Umkreis von 4.900 Einheiten um die Mitte

<!-- swamp-glance:end -->

## Die Geschütze {#the-guns}

Die Türme des Sumpfs feuern auf das **nächste Schiff, das sie sehen können**, innerhalb ihrer Reichweite, und auf kein anderes: Die Zone ist der Kreis, den der am weitesten reichende von ihnen erreicht. Sie sind keine Entitäten irgendeiner Art: Sie haben keine Trefferpunkte, können nicht anvisiert werden, und nichts, was du auf sie schießt, bewirkt etwas. Ihre Schüsse sind echt, und die Welt skaliert ihren Schaden, wie sie die Waffen jedes Aliens skaliert.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Schaden eines Schusses, in jeder Welt:

| Geschütz | Ort | Feuert alle | Reichweite (Einheiten) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-Turm | 5.000 / 4.400 | 2 s | 3.640 | 75.000 | 112.500 | 150.000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-Turm | 5.000 / 4.400 | 5 s | 1.080 | 50.000 | 75.000 | 100.000 |
| Laserturm × 2 | 3.600 / 5.200; 6.400 / 5.200 | 1 s | 2.500 | 45.000–55.000 | 67.500–82.500 | 90.000–110.000 |

- Eine Rakete wird ab 90 % ihrer Reichweite abgefeuert, damit sie ankommt; ein Laserturm feuert einmal pro Sekunde, und sein Schaden wird im gezeigten Bereich ausgewürfelt.
- Eine N.I.K.E. hat 35 % Schilddurchdringung, die von der Absorption eines Schilds abgezogen wird.
- Eine N.U.K.E. detoniert in einem Radius von 900 Einheiten, in der Mitte am härtesten.

<!-- swamp-guns:end -->

- **Nichts reicht über die Zone hinaus,** und in ihr wird ein Schiff in Sekunden zerstört: Je näher es der Mitte kommt, desto mehr Geschütze schalten sich zu, und selbst die bestgeschützte Wraith hält nicht durch.
- **Eine Tarnung bringt dich hinein.** Kein Turm sieht je ein getarntes Schiff, noch eines im Fenster eines EMP, in keiner Entfernung. Eine Explosion, die auf ein sichtbares Schiff gezielt war und neben einem getarnten detoniert, verletzt dieses trotzdem und beendet seine Tarnung.
- **Sie schießen nur auf Piloten,** nie auf Aliens, Konzernpiloten oder den Schwarm, und der Schutz eines Schiffs, das gerade von einer Zerstörung zurückgekehrt ist, gilt auch gegen sie.
- **Der Hinweisring.** Ein Schiff, das den Ring außerhalb der Zone überquert, erhält eine Systemzeile: Die Türme feuern auf jedes Schiff, das sie sehen, und in der Mitte schläft etwas. Es wird erst wieder informiert, wenn es den Ring verlassen hat und zurückgekommen ist.
- **Wieder hinaus.** Wirst du dort zerstört und kehrst an Ort und Stelle zurück, oder loggst du dich in der Zone ein, wirst du außerhalb abgesetzt. Ein Kurs, den du anklickst, wird um die Zone herumgeführt, und ein Hinweis warnt dich, wenn der angeklickte Ort in ihr liegt.

## Die Aliens {#the-aliens}

Drei Aliens der verlorenen Zivilisation leben hier, jedes mit eigenen Zahlen. Sie werden bezahlt wie der Boss eines Schwarms: **nach dem angerichteten Schaden**, an jeden Piloten, der mindestens den in [Schwärme](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm) genannten Anteil erreicht hat, und die Kiste geht an den Piloten mit dem meisten Schaden. Ihre Abschüsse zählen für deine PvE-Rangpunkte wie die eines Schwarmschiffs, im Verhältnis zu ihrer Bezahlung ([Ränge](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). Der Schild jedes von ihnen nimmt 80 % jedes Treffers auf, solange er hält ([Schilde](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** Der schlanke Jäger, das schnellste Alien im Spiel (so schnell wie eine Storm mit Afterburner III). Einige patrouillieren immer in der Umgebung des Sumpfs, und andere kommen in Wellen zu den Baggern. Es ist aggressiv, jagt den nächsten Piloten, den es sehen kann, und sieht nie ein getarntes Schiff.
- **Inert Mass.** Ein toter Koloss mit violetten Rissen, so groß wie eine kleine Station. Sie bleiben in einem festen Umkreis um die Mitte des Sumpfs und verlassen ihn vorerst nicht. Sie feuert **Dormant Lances**: gelenkte Raketen mit sehr großer Reichweite, die einem Schiff folgen, bis es sich tarnt, ein EMP-Fenster öffnet, einen Schutzring betritt, springt oder stirbt. Sie ist schneller als jedes Schiff, nur diese Unterbrechungen helfen. Ein Asteroid auf dem Weg einer Dormant Lance hält sie auf, und die Lance beschädigt ihn mit ihrem eigenen Schaden (niemand wird dafür bezahlt); ein Felsen schützt vor einer Inert Mass also nur für ein paar Treffer.
- **Der Unwakened.** Ein Monolith, der in der Mitte des Sumpfs schläft, das größte Ding auf jeder Karte, so langsam, dass er nie ein Schiff erwischt. Er feuert nichts, aber jedes Schiff in seiner Aura verbrennt, **getarnt oder nicht**. Er ist **immun**: Schüsse und Raketen treffen und bewirken nichts, das Zielfenster zeigt volle Balken und das Wort Immun. Ein späteres Event wird es erlauben, ihn zu bekämpfen; seine Belohnungen unten sind aufgeschrieben und noch nicht zu verdienen.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrouillieren zwischen 4.600 und 6.500 Einheiten von der Mitte des Sumpfs; einer, der zerstört wird, kommt 1 h später zurück. Die Wellen eines Baggers bringen weitere desselben Aliens.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 25.000 | 37.500 | 50.000 |
| Schild | 150.000 | 225.000 | 300.000 |
| Schildabsorption | 80 % | 80 % | 80 % |
| Laserschaden (eine Salve pro Sekunde) | 3.000 | 4.500 | 6.000 |
| Tempo | 400 | 400 | 400 |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | 2.500 | 2.500 | 2.500 |
| Credits | 23.000 | 46.000 | 69.000 |
| Thulium | 60 | 120 | 180 |
| Erfahrung (EP) | 3.600 | 7.200 | 10.800 |
| Ehre | 16 | 32 | 48 |
| PvE-Punkte pro Abschuss | 10 | 10 | 10 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Eines von Ultra Core und Experimental Fusion Core, zufällig gewählt | 60 % | 30–60 |
| Eine der 4 epischen [Raketen](/wiki/06-Items/Rockets.md), zufällig gewählt | 40 % | 1–3 |

### Inert Mass

5 Inert Masses stehen im Umkreis von 2.400 Einheiten um die Mitte; eine, die zerstört wird, kommt 1 h später zurück. Feuert alle 6 s eine gelenkte [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) auf das nächste Schiff ab, das sie sehen kann: Tempo 750, Flugweite 5.250 Einheiten, 40 % Penetration.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 250.000 | 375.000 | 500.000 |
| Schild | 100.000 | 150.000 | 200.000 |
| Schildabsorption | 80 % | 80 % | 80 % |
| Schaden einer Dormant Lance | 5.000–8.000 | 7.500–12.000 | 10.000–16.000 |
| Tempo | 60 | 60 | 60 |
| Raketenreichweite | 5.000 | 5.000 | 5.000 |
| Aggro-Radius | 5.000 | 5.000 | 5.000 |
| Credits | 125.000 | 250.000 | 375.000 |
| Thulium | 335 | 670 | 1.005 |
| Erfahrung (EP) | 20.200 | 40.400 | 60.600 |
| Ehre | 88 | 176 | 264 |
| PvE-Punkte pro Abschuss | 15 | 15 | 15 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Ultra Core und Experimental Fusion Core, gleichmäßig aufgeteilt | 100 % | 400–800 insgesamt |
| Eine der 4 epischen [Raketen](/wiki/06-Items/Rockets.md), zufällig gewählt | 100 % | 20–40 |
| N.I.K.E. | 5 % | 1–2 |
| Dark Matter | 5 % | 1–3 |
| Ancient Control Unit | 10 % | 1 |
| Power Core | 25 % | 1–2 |

### The Unwakened

Es gibt einen, in der Mitte des Sumpfs und sonst nirgends; er kommt 24 h nach seiner Zerstörung zurück. Er ist **immun**, bis eine spätere Quest die Markierung abschaltet: Schüsse und Raketen treffen ihn und bewirken nichts. Seine Belohnungen sind aufgeschrieben und noch nicht zu verdienen.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 10.000.000 | 15.000.000 | 20.000.000 |
| Schild | 10.000.000 | 15.000.000 | 20.000.000 |
| Schildabsorption | 80 % | 80 % | 80 % |
| Aura-Schaden pro Sekunde an jedes Schiff darin | 75.000 | 112.500 | 150.000 |
| Aura-Radius | 700 | 700 | 700 |
| Tempo | 10 | 10 | 10 |
| Aggro-Radius | 3.000 | 3.000 | 3.000 |
| Credits | 7.500.000 | 15.000.000 | 22.500.000 |
| Thulium | 20.000 | 40.000 | 60.000 |
| Erfahrung (EP) | 1.200.000 | 2.400.000 | 3.600.000 |
| Ehre | 5.200 | 10.400 | 15.600 |
| PvE-Punkte pro Abschuss | 112 | 112 | 112 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Ultra Core und Experimental Fusion Core, gleichmäßig aufgeteilt | 100 % | 10.000–15.000 insgesamt |
| Eine der 4 epischen [Raketen](/wiki/06-Items/Rockets.md), zufällig gewählt | 100 % | 500–800 |
| N.I.K.E. | 100 % | 20–30 |
| N.U.K.E. | 100 % | 5–10 |
| Dark Matter | 100 % | 40–60 |
| Ancient Control Unit | 100 % | 10–20 |
| Power Core | 100 % | 100–200 |

<!-- swamp-members:end -->

## Was du hier tun kannst {#what-to-do-here}

- **Schauen, nicht anfassen.** Der Sumpf ist für später. Das Einzige, was du ohne Tarnung erreichst, liegt außerhalb der Zone: Die patrouillierenden Voids in einem Ring um die Zone sind die erste Linie des Sumpfs und der Ort, an dem eine Gruppe ohne die Geschütze kämpfen kann.
- **Bekämpfe die Voids mit Penetration.** Der große Schild eines Voids nimmt 80 % eines Treffers auf und ist fast nebensächlich: Die Hülle dahinter ist klein. Je mehr Schildpenetration deine Laser haben, desto früher fällt er ([Laser & Munition](/wiki/06-Items/Lasers.md)).
- **Halte dich von den Lances fern.** Eine Inert Mass sieht weit, und einer Lance entkommt man nicht: Brich ihren Griff mit einer Tarnung, einem EMP, einem Schutzring oder einem Sprung, oder verlasse ihre Reichweite. Eine Mass ist selbst für eine große Gruppe der stärksten Schiffe ein langer Kampf.
- **Der Dormant-Schwarm** erscheint jetzt knapp außerhalb der Zone, sodass eine Gruppe ohne die Geschütze auf ihn warten kann. Siehe [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md).

## Weiterlesen {#where-to-read-more}

- [Gefahrensektoren](/wiki/01-General/Danger-Sectors.md): was sich an Tag 11 geändert hat.
- [Riesenbagger](/wiki/03-Mechanics/Giant-Excavator.md): die Wellen der Slumbering Voids und was sie bewachen.
- [Schwärme](/wiki/05-Swarms/Swarms.md) und [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md): so zahlt ein Boss-Abschuss.
- [Raketen](/wiki/06-Items/Rockets.md#the-craft-only-rockets): die N.I.K.E. und die N.U.K.E., die der Turm abfeuert.
- [Schwarzes Loch](/wiki/03-Mechanics/Black-Hole.md): die andere Gefahr von `DS-4`.
- [Frachtkisten](/wiki/03-Mechanics/Cargo.md): die Kisten, die die Aliens fallen lassen.
