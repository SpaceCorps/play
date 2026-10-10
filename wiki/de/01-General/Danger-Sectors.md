<!-- wiki-i18n source: 13c9ac551cfd01fa -->
<!-- wiki-i18n title: Gefahrensektoren -->
# Gefahrensektoren {#danger-sectors}

<!-- wiki-search: ds; ds-1; ds-2; ds-3; ds-4; central pvp zone; pvp zone; pulsar; giant excavator; excavator; dormant swamp; swamp; event 2; tech surge; gefahrensektor; riesenbagger; bagger; sumpf; techschub -->

Die **Gefahrensektoren** sind die vier Sektoren in der Mitte der Galaxie, `DS-1` bis `DS-4`. Dort treffen die drei Konzerne aufeinander, und die Piloten dürfen sich dort in jeder Welt gegenseitig bekämpfen ([Reisen im All](/wiki/01-General/Spacemap%20Travel.md)). `DS-1`, `DS-2` und `DS-3` haben je das Tor eines Konzerns; `DS-4` ist der Kern, mit dem [Schwarzen Loch](/wiki/03-Mechanics/Black-Hole.md) in der Mitte. In keinem von ihnen gibt es eine Station: Die einzigen sicheren Orte sind die Ringe um die Sprungtore.

Hier lebte einst eine Zivilisation der alten Galaxie, fortgeschritten und violettschwarz, und aus einem Grund, den niemand kennt, ist sie untergegangen. Ihre Überreste waren nie ganz tot: Der [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md) war das erste Zeichen. Ab **Saisontag 11**, dem Beginn von Event 2 (**Techschub**, siehe die [Wipe-Zeitleiste](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)), erwacht mehr davon, und die Gefahrensektoren verändern sich. Jeder Pilot der Welt erfährt es an dem Tag, an dem es beginnt, und was neu ist, bleibt bis zum Wipe.

![Flying in towards the Dormant Swamp: the amber notice ring and, inside it, the red ring of the zone the guns reach](../../img/wiki-img/shots/swamp-rings.jpg)

## Was ab Tag 11 neu ist {#what-is-new-from-day-11}

- **Riesenbagger.** `DS-1`, `DS-2` und `DS-3` haben ab dem ersten Tag der Saison je einen Pulsar, ein Licht am Himmel und sonst nichts; ab Tag 11 bekommt jeder einen **Riesenbagger** daneben. Legst du Dark Matter in den Tank des Baggers und wählst eine Ressource, baut er den Pulsar ab: Thulium und seltene Erze landen in Kisten rund um ihn, die jeder nehmen darf. Es ist das Reichste, worum in den Gefahrensektoren gekämpft wird, und das Gefährlichste. Siehe [Riesenbagger](/wiki/03-Mechanics/Giant-Excavator.md).
- **Slumbering Voids.** Solange ein Bagger abbaut, fliegen **Slumbering Voids** in Wellen vom Kartenrand heran und jagen die Piloten in seiner Nähe. Andere patrouillieren am Sumpf. Siehe [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).
- **Der Dormant Swamp.** In einer Ecke von `DS-4` steht die Basis der verlorenen Zivilisation: Geschütze, die auf jedes Schiff feuern, das sie sehen, Inert Masses, die sie bewachen, und in der Mitte der Unwakened. Es ist ein Ort, den Piloten noch nicht besuchen sollen. Siehe [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md).
- **Ein schnellerer, reicherer Dormant-Schwarm.** Der Schwarm erscheint jetzt am Sumpf, kommt nach seiner Zerstörung früher zurück und zahlt doppelt so viel. Siehe [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md).
- **Vor Tag 11** leuchten nur die Pulsare: Die Gefahrensektoren sind sonst so, wie [Reisen im All](/wiki/01-General/Spacemap%20Travel.md) sie beschreibt. Eine Welt ab Tag 11 hat alles auf einmal.

## Wo alles liegt {#where-everything-is}

Jede Welt hat von allem ihre eigene Kopie, und ein Pulsar und sein Bagger stehen im offenen Drittel ihres Sektors, weit weg von jedem Torring, auf der Seite, die zur Kartenmitte zeigt. Entfernungen sind in Karteneinheiten; die Sektoren sind 32.000 mal 18.000 Einheiten groß.

<!-- danger-sites:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Sektor | Tor des Konzerns | Pulsar | Riesenbagger |
| :--- | :--- | :--- | :--- |
| `DS-1` | Mars | 8.000 / 5.000 | 8.805 / 5.402 |
| `DS-2` | Terra | 8.000 / 13.000 | 8.805 / 12.598 |
| `DS-3` | Galactic | 24.000 / 13.000 | 23.195 / 12.598 |

<!-- danger-sites:end -->

`DS-4` hat keinen Pulsar: Dort ist das Schwarze Loch. Seine Ecke enthält stattdessen den Dormant Swamp; dessen Zahlen stehen in [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#at-a-glance).

<!-- danger-rules:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- Die Pulsare leuchten ab dem ersten Tag der Saison; alles andere Neue erscheint an Saisontag 11 und bleibt bis zum Wipe.
- Jede Welt hat ihre eigenen Pulsare, Bagger und ihren eigenen Sumpf: Was in einer geschieht, geschieht nicht in einer anderen.
- Kein Asteroid liegt innerhalb von 2.600 Einheiten um einen Pulsar, 2.200 Einheiten um einen Riesenbagger oder 4.900 Einheiten um die Mitte des Dormant Swamp.

<!-- danger-rules:end -->

## Ärger vermeiden {#keeping-out-of-trouble}

- **Strahlung.** Ein Bagger, der überhitzt oder zerstört wurde, und sein Pulsar verbrennen jedes Schiff, das in ihren Kreisen bleibt ([Riesenbagger](/wiki/03-Mechanics/Giant-Excavator.md#heat-and-radiation)). Das Spiel warnt dich vorher, und die Kreise werden im Flug auf den Boden und auf die Minikarte gezeichnet.
- **Die Geschütze des Sumpfs.** Auf ein Schiff, das die Türme des Sumpfs sehen können, wird geschossen, lange bevor es etwas sehen kann, was die Reise lohnt ([Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#the-guns)). Ein Kurs, den du anklickst, wird um die Geschütze und die Strahlung herumgeführt, wie um das Schwarze Loch, und ein Hinweis warnt dich, wenn der angeklickte Ort darin liegt.
- **Wenn du dort zerstört wirst,** setzt dich die Wahl, **an Ort und Stelle** zurückzukehren, an den nächsten Punkt außerhalb der Strahlung und außerhalb der Zone des Sumpfs, wie beim Schwarzen Loch ([Erste Schritte](/wiki/01-General/Getting-Started.md#dying-and-coming-back)).
- **Eine Gruppe und ein Ausweg.** Die Bagger ziehen Voids und Rivalen gleichermaßen an. Bring eine [Gruppe](/wiki/03-Mechanics/Groups.md) mit, wisse, welches Tor am nächsten ist, und denk daran, dass du in den Gefahrensektoren nicht hinausspringen kannst, solange du angegriffen wirst ([Sprung unter Beschuss](/wiki/01-General/Spacemap%20Travel.md#jumping-under-fire)).
- **Der Rest ist PvP wie immer.** Nichts hier ist ein sicherer Ort: Es gelten die normalen Regeln deiner Welt, Rivalen eingeschlossen.

## Weiterlesen {#where-to-read-more}

- [Riesenbagger](/wiki/03-Mechanics/Giant-Excavator.md): das Bedienfeld, der Treibstoff, was er abbaut, die Voids, die Hitze und die Strahlung.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): die Geschütze, die drei Aliens und das neue Zuhause des Schwarms.
- [Dormant-Schwarm](/wiki/05-Swarms/Dormant-Swarm.md) und [Schwärme](/wiki/05-Swarms/Swarms.md).
- [Das Schwarze Loch](/wiki/03-Mechanics/Black-Hole.md) und [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md): woher der Treibstoff kommt.
- [Asteroidenabbau](/wiki/03-Mechanics/Asteroid-Mining.md): die Felsen der Gefahrensektoren.
