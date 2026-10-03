<!-- wiki-i18n source: 2543654c0a5dfec9 -->
<!-- wiki-i18n title: Dormant-Schwarm -->
# Dormant-Schwarm {#dormant-swarm}

Der Dormant-Schwarm besteht aus einer **Dormant Force** mit ihren **Dormant Pulses**: einer Gruppe von Schiffen, die nie einen Kampf beginnen und sehr hart zuschlagen, sobald sie geweckt sind. Es gibt nur einen in jeder Welt. Er wandert von einem Gefahrensektor zum nächsten, und er ist der härteste Kampf und die reichste Beute unter den Schwärmen: ein Kampf für eine große Gruppe der stärksten Schiffe.

## Auf einen Blick {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Gefahrensektoren `DS-1`, `DS-2`, `DS-3`, `DS-4`, von einem zum anderen fliegend
- **Wie viele**: Einer in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe
- **Anführer**: Dormant Force
- **Begleiter**: 2 × Dormant Pulse, die mit dem Anführer fliegen
- **Begleiter bleiben nahe**: höchstens 700 Einheiten vom Anführer entfernt
- **Anführer zerstört**: Dormant Pulse übernimmt die Führung
- **Reise**: Bleibt 8 bis 15 min auf einer Karte und fliegt dann zum Tor eines anderen Gefahrensektors. Er nimmt nie ein Tor aus den Gefahrensektoren hinaus und fliegt nie in den Ring des Schwarzen Lochs
- **Kehrt zurück**: 1 h nach der Zerstörung des ganzen Schwarms, in einem zufälligen Gefahrensektor
- **Meldungen**: Der Chat der ganzen Welt meldet, wann der Schwarm auftaucht und wann er zerstört wird. Eine Markierung zeigt ihn auf den Karten der Gefahrensektoren und auf der Galaxiekarte. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- dormant-glance:end -->

## Die Mitglieder {#the-members}

- **Dormant Force**: eine Wraith mit voller Stärke, mit Lasern, die dreimal so hart treffen wie die einer typischen Ausrüstung. Sie führt den Schwarm an, ist passiv, bis sie getroffen wird, und feuert **gerade Raketen** auf den ersten Piloten, der sie getroffen hat.
- **Dormant Pulse**: eine Paragon mit voller Stärke, mit derselben Art schwerer Laser und eigenen Raketen. Die Pulses fliegen dicht bei der Force, und wenn die Force zerstört wird, übernimmt eine von ihnen die Führung.

Sie sind passiv: Sie gehen nie auf einen Piloten los. Wird eines von ihnen getroffen, greifen die anderen in seiner Nähe mit ein, und zwar gegen den ersten Piloten, der es getroffen hat.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Finde ihn.** Die ganze Welt erfährt, wenn er auftaucht, und eine Markierung zeigt ihn auf den Karten der Gefahrensektoren und auf der Galaxiekarte. Er bleibt so lange auf einer Karte, wie die Liste *Auf einen Blick* sagt, fliegt dann zum Tor eines anderen Gefahrensektors und springt; er nimmt nie ein Tor aus den Gefahrensektoren hinaus und fliegt nie in den Ring des Schwarzen Lochs. Er fliegt mit dem Tempo seines langsamsten Schiffs und beginnt oder beendet, wie ein Pilot, keinen Sprung unter Beschuss.
- **Allein oder zu wenigen ist er nicht zu schaffen.** Acht Piloten von Level 8 in Paragons mit x2- oder x4-Munition zerstören ihn in Alpha in etwa einer Minute und verlieren höchstens ein Schiff; eine Paragon allein wird zerstört, und mit x2-Munition auch drei. Die Schwärme von Beta und Gamma sind stärker ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)), diese Welten brauchen also größere Gruppen.
- **Seine Laser entscheiden den Kampf.** Zusammen können sie eine Paragon in unter einer Minute zerstören, selbst eine mit den besten Schilden in unter zwei Minuten, mit oder ohne Raketen: Bring deinen Schaden schnell ins Ziel, mit den besten Schilden, die du hast.
- **Schiff für Schiff.** Jedes Schiff hat seine eigene Hülle und seine eigene Bezahlung, die Force oder eine Pulse kann also zuerst zerstört werden. Der Schwarm wird erst ersetzt, wenn er ganz zerstört ist, und zwar nach der Zeit in der Liste *Auf einen Blick*.

## Belohnungen und Beute {#rewards-and-drops}

Jedes Schiff zahlt für sich, nach dem Schaden, der ihm zugefügt wurde ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), und jedes lässt eine Kiste für den Piloten fallen, der ihm den meisten Schaden zugefügt hat. Die **Kiste der Force** ist der Preis: sehr viel x3- und x4-Munition, Epische Raketen einer Sorte und hin und wieder eine N.I.K.E. oder eine N.U.K.E. Die **Pulses** lassen vielleicht eine Ancient Control Unit, einen Power Core oder Dark Matter fallen. Eine Minute Kampf gegen den Schwarm zahlt mehr als eine Minute Kampf gegen den Crystalys, das bestbezahlte Alien.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force {#dormant-force}

Basis: Wraith mit 100 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds. Feuert alle 5 s eine gerade Rakete ab: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 324.000 | 486.000 | 648.000 |
| Schild | 83.400 | 125.100 | 166.800 |
| Laserschaden (eine Salve pro Sekunde) | 2.880 | 4.320 | 5.760 |
| Tempo | 225 | 225 | 225 |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Raketenschaden, höchstens | 7.500 | 11.250 | 15.000 |
| Credits | 160.000 | 320.000 | 480.000 |
| Thulium | 535 | 1.070 | 1.605 |
| Erfahrung (EP) | 32.100 | 64.200 | 96.300 |
| Ehre | 139 | 278 | 417 |
| PvE-Punkte pro Abschuss | 25 | 25 | 25 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Ultra Core und Experimental Fusion Core, gleichmäßig aufgeteilt | 100 % | 2.000–3.000 insgesamt |
| Eine der 4 epischen [Raketen](/wiki/06-Items/Rockets.md), zufällig gewählt | 100 % | 30–50 |
| Eines von [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) und [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets), zufällig gewählt | 50 % | 1 |

### Dormant Pulse {#dormant-pulse}

Basis: Paragon mit 100 % von Hülle, Schild und Schaden; Tempo und Reichweite bleiben die des Vorbilds. Feuert alle 5 s eine gerade Rakete ab: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 128.000 | 192.000 | 256.000 |
| Schild | 64.570 | 96.855 | 129.140 |
| Laserschaden (eine Salve pro Sekunde) | 1.920 | 2.880 | 3.840 |
| Tempo | 210 | 210 | 210 |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Raketenschaden, höchstens | 5.000 | 7.500 | 10.000 |
| Credits | 75.000 | 150.000 | 225.000 |
| Thulium | 255 | 510 | 765 |
| Erfahrung (EP) | 15.200 | 30.400 | 45.600 |
| Ehre | 66 | 132 | 198 |
| PvE-Punkte pro Abschuss | 10 | 10 | 10 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Ancient Control Unit | 20 % | 1 |
| Power Core | 20 % | 1 |
| Dark Matter | 20 % | 1–5 |

<!-- dormant-members:end -->
