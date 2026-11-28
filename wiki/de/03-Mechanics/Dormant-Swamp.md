<!-- wiki-i18n source: 3c07d568f3af3aab -->
<!-- wiki-i18n title: Dormant Swamp -->
# Dormant Swamp

<!-- wiki-search: swamp; dormant swamp; base; turret; turrets; nike turret; laser turret; inert mass; unwakened; the unwakened; slumbering void; void; dormant lance; ds-4; sumpf; geschütz; geschütze; turm; türme -->

Vor langer Zeit lebte mitten in der Galaxie eine fortgeschrittene Zivilisation. Sie baute in violettschwarzem Kristall mit leuchtenden violetten Adern, und aus einem Grund, den niemand kennt, ist sie untergegangen. Der **Dormant Swamp** ist ihr Außenposten, in der oberen linken Ecke von `DS-4`. Ab Saisontag 11 regt er sich: Geschütze in der Mitte feuern auf jedes Schiff, das sie sehen, **Inert Masses** bewachen ihn, und ganz in der Mitte schläft **der Unwakened**. Unter Tarnung kannst du bis zum Unwakened fliegen. Seit sich die [Deep Void](/wiki/03-Mechanics/Deep-Void.md) geöffnet hat, können die Geschütze und der Unwakened zerstört werden, und der erste Abschuss des Unwakened in einer Saison öffnet in jeder Welt die Threshold dieser Welt. Die Basis selbst kann nicht betreten oder geentert werden, und man kann nicht mit ihr handeln.

Am Sumpf erscheint ab Tag 11 auch der [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md), und **Slumbering Voids** patrouillieren um ihn herum. Dieselben Voids kommen in Wellen zu den [Riesenbaggern](/wiki/03-Mechanics/Giant-Excavator.md#the-slumbering-voids). Die Sektoren stehen in [Gefahrensektoren](/wiki/01-General/Danger-Sectors.md).

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## Auf einen Blick {#at-a-glance}

<!-- swamp-glance:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- **Wo**: Die obere linke Ecke von `DS-4`: Die Mitte liegt bei 5.000 / 5.000
- **Erscheint**: Ab Saisontag 11 bis zum Wipe
- **Die Zone**: 4.300 Einheiten um die Mitte: so weit reichen die Geschütze höchstens
- **Der Hinweis**: Ein Schiff, das den Ring 4.800 Einheiten von der Mitte überquert, erhält eine Systemzeile
- **Tarnung**: Kein Geschütz sieht je ein getarntes Schiff oder eines im Fenster eines EMP
- **Die Aliens**: 5 Inert Masses bleiben im Umkreis von 2.400 Einheiten um die Mitte. Der Unwakened schläft in der Mitte. 2 Slumbering Voids patrouillieren zwischen 4.600 und 6.500 Einheiten von der Mitte.
- **Der Dormant-Schwarm**: Er erscheint bei 9.417 / 6.606, 4.700 Einheiten von der Mitte entfernt und außerhalb der Zone
- **Felsen**: Kein Asteroid liegt im Umkreis von 4.900 Einheiten um die Mitte

<!-- swamp-glance:end -->

## Die Geschütze {#the-guns}

Die Türme des Sumpfs feuern auf das **nächste Schiff, das sie sehen können**, innerhalb ihrer Reichweite, und auf kein anderes: Die Zone ist der Kreis, den der am weitesten reichende von ihnen erreicht. Sie sind keine Schiffe, aber seit sich die Deep Void geöffnet hat, hat jeder von ihnen Trefferpunkte: Klicke ein Geschütz an, um mit deinen Lasern darauf zu feuern, und eine Rakete, die in seiner Nähe explodiert, schadet ihm auch. Ein zerstörtes Geschütz bleibt zerstört, bis der Unwakened zurückkehrt. Ihre Schüsse sind echt, und die Welt skaliert ihren Schaden, wie sie die Waffen jedes Aliens skaliert.

<!-- swamp-guns:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

Schaden eines Schusses, in jeder Welt:

| Geschütz | Ort | Feuert alle | Reichweite (Einheiten) | Alpha | Beta | Gamma |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-Turm | 5.000 / 4.400 | 2 s | 3.640 | 75.000 | 112.500 | 150.000 |
| [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets)-Turm | 5.000 / 4.400 | 5 s | 1.080 | 50.000 | 75.000 | 100.000 |
| Laserturm × 2 | 3.600 / 5.200; 6.400 / 5.200 | 1 s | 2.500 | 45.000–55.000 | 67.500–82.500 | 90.000–110.000 |

- Eine Rakete wird ab 82 % der Reichweite abgefeuert, die dieselbe Rakete in der Hand eines Piloten hat, damit sie ankommt; ein Laserturm feuert einmal pro Sekunde, und sein Schaden wird im gezeigten Bereich ausgewürfelt.
- Eine N.I.K.E. hat 35 % Schilddurchdringung, die von der Absorption eines Schilds abgezogen wird.
- Die N.I.K.E. des Turms fliegt 25 % schneller und 2× so weit wie deine: 1.250 Einheiten pro Sekunde, 8.910 Einheiten insgesamt, sodass ein Schiff, das vor ihr flieht, weit verfolgt wird.
- Eine N.U.K.E. detoniert in einem Radius von 1.013 Einheiten, in der Mitte am härtesten.
- Die N.U.K.E. des Turms fliegt 25 % schneller und 2× so weit wie deine: 375 Einheiten pro Sekunde, 2.640 Einheiten insgesamt, sodass ein Schiff, das vor ihr flieht, weit verfolgt wird.

<!-- swamp-guns:end -->

- **Von außerhalb der Zone schießt nichts,** und in ihr wird ein Schiff in Sekunden zerstört: Je näher es der Mitte kommt, desto mehr Geschütze schalten sich zu, und selbst die bestgeschützte Wraith hält nicht durch. Eine Rakete, die schon in der Luft ist, fliegt allerdings weiter, und die Raketen des Turms fliegen schneller und weiter als deine: Wer geradewegs vor einer davonfliegt, schüttelt sie nicht ab.
- **Eine Tarnung bringt dich hinein.** Kein Turm sieht je ein getarntes Schiff, noch eines im Fenster eines EMP, in keiner Entfernung. Eine Explosion, die auf ein sichtbares Schiff gezielt war und neben einem getarnten detoniert, verletzt dieses trotzdem und beendet seine Tarnung.
- **Sie schießen nur auf Piloten,** nie auf Aliens, Konzernpiloten oder den Schwarm, und der Schutz eines Schiffs, das gerade von einer Zerstörung zurückgekehrt ist, gilt auch gegen sie.
- **Der Hinweisring.** Ein Schiff, das den Ring außerhalb der Zone überquert, erhält eine Systemzeile: Die Türme feuern auf jedes Schiff, das sie sehen, und in der Mitte schläft etwas. Es wird erst wieder informiert, wenn es den Ring verlassen hat und zurückgekommen ist.
- **Wieder hinaus.** Wirst du dort zerstört, kannst du nicht an Ort und Stelle zurückkehren (ein Gefahrensektor bietet nur die Basis und das nächste Portal an), und loggst du dich in der Zone ein, wirst du außerhalb abgesetzt. Ein Kurs, den du anklickst, wird um die Zone herumgeführt, und ein Hinweis warnt dich, wenn der angeklickte Ort in ihr liegt.

## Die Aliens {#the-aliens}

Drei Aliens der verlorenen Zivilisation leben hier, jedes mit eigenen Zahlen. Sie werden bezahlt wie der Boss eines Schwarms: **nach dem angerichteten Schaden**, an jeden Piloten, der mindestens den in [Schwärme](/wiki/05-Swarms/Swarms.md#the-rules-of-every-swarm) genannten Anteil erreicht hat, und die Kiste geht an den Piloten mit dem meisten Schaden. Ihre Abschüsse zählen für deine PvE-Rangpunkte wie die eines Schwarmschiffs, im Verhältnis zu ihrer Bezahlung ([Ränge](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points)). Der Schild jedes von ihnen nimmt {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}} jedes Treffers auf, solange er hält ([Schilde](/wiki/03-Mechanics/Shields.md)).

- **Slumbering Void.** Der schlanke Jäger, das schnellste Alien im Spiel (schneller als eine Storm mit Afterburner III). Einige patrouillieren immer in der Umgebung des Sumpfs, und andere kommen in Wellen zu den Baggern. Es ist aggressiv, jagt den nächsten Piloten, den es sehen kann, und sieht nie ein getarntes Schiff.
- **Inert Mass.** Ein toter Koloss mit violetten Rissen, so groß wie eine kleine Station. Sie bleiben in einem festen Umkreis um die Mitte des Sumpfs und verlassen ihn vorerst nicht. Sie feuert **Dormant Lances**: gelenkte Raketen mit sehr großer Reichweite, die einem Schiff folgen, bis es sich tarnt, ein EMP-Fenster öffnet, einen Schutzring betritt, springt oder stirbt. Sie ist schneller als jedes Schiff, nur diese Unterbrechungen helfen. Ein Asteroid auf dem Weg einer Dormant Lance hält sie auf, und die Lance beschädigt ihn mit ihrem eigenen Schaden (niemand wird dafür bezahlt); ein Felsen schützt vor einer Inert Mass also nur für ein paar Treffer.
- **Der Unwakened.** Ein Monolith, der in der Mitte des Sumpfs schläft, das größte Ding auf jeder Karte, so langsam, dass er nie ein Schiff erwischt. Er feuert nichts, aber jedes Schiff in seiner Aura verbrennt, **getarnt oder nicht**. Seit sich die [Deep Void](/wiki/03-Mechanics/Deep-Void.md) geöffnet hat, kann er zerstört werden: Er wird nach dem verursachten Schaden bezahlt, kommt einen Tag nach seinem Tod zurück, und der erste Abschuss einer Saison öffnet in jeder Welt ihre Threshold. Die **Strahlungstechnik** eines Piloten senkt das Brennen auf das 0,40-Fache auf Stufe 100.

<!-- swamp-members:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

### Slumbering Void

2 Slumbering Voids patrouillieren zwischen 4.600 und 6.500 Einheiten von der Mitte des Sumpfs; einer, der zerstört wird, kommt {{guide:vitals.respawn@Slumbering Void}} später zurück. Die Wellen eines Baggers bringen weitere desselben Aliens.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Slumbering Void}} | {{guide:vitals.hull*1.5@Slumbering Void}} | {{guide:vitals.hull*2@Slumbering Void}} |
| Schild | {{guide:vitals.shield@Slumbering Void}} | {{guide:vitals.shield*1.5@Slumbering Void}} | {{guide:vitals.shield*2@Slumbering Void}} |
| Schildabsorption | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} | {{guide:vitals.absorbance@Slumbering Void}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Slumbering Void}} | {{guide:vitals.dps*1.5@Slumbering Void}} | {{guide:vitals.dps*2@Slumbering Void}} |
| Tempo | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} | {{guide:vitals.speed@Slumbering Void}} |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} | {{guide:vitals.aggro@Slumbering Void}} |
| Credits | {{guide:spoils.pay.credits@Slumbering Void}} | {{guide:spoils.pay.credits*2@Slumbering Void}} | {{guide:spoils.pay.credits*3@Slumbering Void}} |
| Thulium | {{guide:spoils.pay.thulium@Slumbering Void}} | {{guide:spoils.pay.thulium*2@Slumbering Void}} | {{guide:spoils.pay.thulium*3@Slumbering Void}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Slumbering Void}} | {{guide:spoils.pay.experience*2@Slumbering Void}} | {{guide:spoils.pay.experience*3@Slumbering Void}} |
| Ehre | {{guide:spoils.pay.honor@Slumbering Void}} | {{guide:spoils.pay.honor*2@Slumbering Void}} | {{guide:spoils.pay.honor*3@Slumbering Void}} |
| PvE-Punkte pro Abschuss | 10 | 10 | 10 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Slumbering Void}} |

### Inert Mass

5 Inert Masses stehen im Umkreis von 2.400 Einheiten um die Mitte; eine, die zerstört wird, kommt {{guide:vitals.respawn@Inert Mass}} später zurück. Feuert alle 6 s eine gelenkte [Dormant Lance](/wiki/06-Items/Rockets.md#the-craft-only-rockets) auf das nächste Schiff ab, das sie sehen kann: Tempo 750, Flugweite 5.250 Einheiten, 40 % Penetration.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Inert Mass}} | {{guide:vitals.hull*1.5@Inert Mass}} | {{guide:vitals.hull*2@Inert Mass}} |
| Schild | {{guide:vitals.shield@Inert Mass}} | {{guide:vitals.shield*1.5@Inert Mass}} | {{guide:vitals.shield*2@Inert Mass}} |
| Schildabsorption | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} | {{guide:vitals.absorbance@Inert Mass}} |
| Schaden einer Dormant Lance | {{guide:behaviour.ability:rocket.damageMin@Inert Mass}}–{{guide:behaviour.ability:rocket.damage@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*1.5@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*1.5@Inert Mass}} | {{guide:behaviour.ability:rocket.damageMin*2@Inert Mass}}–{{guide:behaviour.ability:rocket.damage*2@Inert Mass}} |
| Tempo | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} | {{guide:vitals.speed@Inert Mass}} |
| Raketenreichweite | 5.000 | 5.000 | 5.000 |
| Aggro-Radius | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} | {{guide:vitals.aggro@Inert Mass}} |
| Credits | {{guide:spoils.pay.credits@Inert Mass}} | {{guide:spoils.pay.credits*2@Inert Mass}} | {{guide:spoils.pay.credits*3@Inert Mass}} |
| Thulium | {{guide:spoils.pay.thulium@Inert Mass}} | {{guide:spoils.pay.thulium*2@Inert Mass}} | {{guide:spoils.pay.thulium*3@Inert Mass}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Inert Mass}} | {{guide:spoils.pay.experience*2@Inert Mass}} | {{guide:spoils.pay.experience*3@Inert Mass}} |
| Ehre | {{guide:spoils.pay.honor@Inert Mass}} | {{guide:spoils.pay.honor*2@Inert Mass}} | {{guide:spoils.pay.honor*3@Inert Mass}} |
| PvE-Punkte pro Abschuss | 15 | 15 | 15 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Inert Mass}} |

### The Unwakened

Es gibt einen, in der Mitte des Sumpfs und sonst nirgends; er kommt {{guide:vitals.respawn@The Unwakened}} nach seiner Zerstörung zurück. Seit sich die Deep Void geöffnet hat, kann er zerstört werden, und er wird wie die anderen Aliens hier nach dem verursachten Schaden bezahlt.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@The Unwakened}} | {{guide:vitals.hull*1.5@The Unwakened}} | {{guide:vitals.hull*2@The Unwakened}} |
| Schild | {{guide:vitals.shield@The Unwakened}} | {{guide:vitals.shield*1.5@The Unwakened}} | {{guide:vitals.shield*2@The Unwakened}} |
| Schildabsorption | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} | {{guide:vitals.absorbance@The Unwakened}} |
| Aura-Schaden pro Sekunde an jedes Schiff darin | {{guide:behaviour.ability:aura.damagePerSecond@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*1.5@The Unwakened}} | {{guide:behaviour.ability:aura.damagePerSecond*2@The Unwakened}} |
| Aura-Radius | 700 | 700 | 700 |
| Tempo | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} | {{guide:vitals.speed@The Unwakened}} |
| Aggro-Radius | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} | {{guide:vitals.aggro@The Unwakened}} |
| Credits | {{guide:spoils.pay.credits@The Unwakened}} | {{guide:spoils.pay.credits*2@The Unwakened}} | {{guide:spoils.pay.credits*3@The Unwakened}} |
| Thulium | {{guide:spoils.pay.thulium@The Unwakened}} | {{guide:spoils.pay.thulium*2@The Unwakened}} | {{guide:spoils.pay.thulium*3@The Unwakened}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@The Unwakened}} | {{guide:spoils.pay.experience*2@The Unwakened}} | {{guide:spoils.pay.experience*3@The Unwakened}} |
| Ehre | {{guide:spoils.pay.honor@The Unwakened}} | {{guide:spoils.pay.honor*2@The Unwakened}} | {{guide:spoils.pay.honor*3@The Unwakened}} |
| PvE-Punkte pro Abschuss | 112 | 112 | 112 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@The Unwakened}} |

<!-- swamp-members:end -->

## Mit der Deep Void {#with-the-deep-void}

Was die Deep Void hier verändert hat, in Kürze:

- **Der Unwakened kann zerstört werden.** Er ist nicht mehr unverwundbar: Er wird wie die anderen Aliens hier nach dem verursachten Schaden bezahlt und kommt einen Tag nach seinem Tod zurück.
- **Die Geschütze können zerstört werden.** Jedes der drei Geschütze (der Raketenturm, der die N.I.K.E. und die N.U.K.E. abfeuert, und die beiden Lasertürme) hat jetzt Trefferpunkte, und Laser und Raketen schaden ihnen. Ein zerstörtes Geschütz bleibt zerstört, bis der Unwakened zurückkehrt.
- **Der erste Abschuss öffnet die Threshold.** Der erste Abschuss des Unwakened in einer Saison öffnet in jeder Welt die Threshold dieser Welt in der gegenüberliegenden Ecke von `DS-4`, wo die [Deep Void](/wiki/03-Mechanics/Deep-Void.md) beginnt.

## Was du hier tun kannst {#what-to-do-here}

- **Der erste Abschuss öffnet den Weg.** Der erste Abschuss des Unwakened in einer Saison öffnet die Threshold seiner Welt und damit den Weg in die [Deep Void](/wiki/03-Mechanics/Deep-Void.md); innerhalb der Zone zerstören die Geschütze ein Schiff in Sekunden. Außerhalb der Zone sind die patrouillierenden Voids in einem Ring um die Zone die erste Linie des Sumpfs und der Ort, an dem eine Gruppe ohne die Geschütze kämpfen kann.
- **Bekämpfe die Voids mit Penetration.** Der große Schild eines Voids nimmt {{guide:vitals.absorbance@Slumbering Void;Inert Mass;The Unwakened}} eines Treffers auf und ist fast nebensächlich: Die Hülle dahinter ist klein. Je mehr Schildpenetration deine Laser haben, desto früher fällt er ([Laser & Munition](/wiki/06-Items/Lasers.md)).
- **Halte dich von den Lances fern.** Eine Inert Mass sieht weit, und einer Lance entkommt man nicht: Brich ihren Griff mit einer Tarnung, einem EMP, einem Schutzring oder einem Sprung, oder verlasse ihre Reichweite. Eine Mass ist selbst für eine große Gruppe der stärksten Schiffe ein langer Kampf.
- **Der Dormant-Schwarm** erscheint jetzt knapp außerhalb der Zone, sodass eine Gruppe ohne die Geschütze auf ihn warten kann. Siehe [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md).

## Weiterlesen {#where-to-read-more}

- [Gefahrensektoren](/wiki/01-General/Danger-Sectors.md): was sich an Tag 11 geändert hat.
- [Riesenbagger](/wiki/03-Mechanics/Giant-Excavator.md): die Wellen der Slumbering Voids und was sie bewachen.
- [Schwärme](/wiki/05-Swarms/Swarms.md) und [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md): so zahlt ein Boss-Abschuss.
- [Raketen](/wiki/06-Items/Rockets.md#the-craft-only-rockets): die N.I.K.E. und die N.U.K.E., die der Turm abfeuert.
- [Schwarzes Loch](/wiki/03-Mechanics/Black-Hole.md): die andere Gefahr von `DS-4`.
- [Frachtkisten](/wiki/03-Mechanics/Cargo.md): die Kisten, die die Aliens fallen lassen.
