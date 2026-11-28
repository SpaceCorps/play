<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Dormant-Schwarm -->
# Dormant-Schwarm {#dormant-swarm}

Der Dormant-Schwarm besteht aus einer **Dormant Force** mit ihren **Dormant Pulses**: einer Gruppe von Schiffen, die nie einen Kampf beginnen und sehr hart zuschlagen, sobald sie geweckt sind. Es gibt nur einen in den Gefahrensektoren jeder Welt (die [Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) hat einen eigenen Besuch, einmal am Tag). Er wandert von einem Gefahrensektor zum nächsten, und er ist der härteste Kampf und die reichste Beute unter den Schwärmen: ein Kampf für eine große Gruppe der stärksten Schiffe. Ab Saisontag 11 startet er im [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) auf `DS-4`, kehrt früher zurück und zahlt doppelt so viel (siehe die Liste *Auf einen Blick*).

## Auf einen Blick {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Die Gefahrensektoren `DS-1`, `DS-2`, `DS-3`, `DS-4`, von einem zum anderen fliegend
- **Wie viele**: Einer in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe (Beta und Gamma: ab Saisontag 1)
- **Anführer**: Dormant Force
- **Begleiter**: 2 × Dormant Pulse, die mit dem Anführer fliegen
- **Begleiter bleiben nahe**: höchstens 700 Einheiten vom Anführer entfernt
- **Anführer zerstört**: Dormant Pulse übernimmt die Führung
- **Anführer zerstört**: Die Begleiter verschwinden 30 s nach der Zerstörung des Anführers, auch wenn sie gerade angreifen
- **Reise**: Bleibt 8 bis 15 min auf einer Karte und fliegt dann zum Tor eines anderen Gefahrensektors. Er nimmt nie ein Tor aus den Gefahrensektoren hinaus und fliegt nie in den Ring des Schwarzen Lochs
- **Kehrt zurück**: {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} nach der Zerstörung des ganzen Schwarms, in einem zufälligen Gefahrensektor
- **Ab Saisontag 11**: Er erscheint im [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) auf `DS-4` statt in einem zufälligen Gefahrensektor, kehrt 30 min nach der Zerstörung des ganzen Schwarms zurück, und jedes Schiff zahlt ×2 (Credits, Thulium, EP und Ehre; die Beute bleibt gleich)
- **Meldungen**: Die Piloten der ganzen Welt erfahren, wann der Schwarm auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Eine Markierung zeigt ihn auf den Karten der Gefahrensektoren und auf der Galaxiekarte. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- dormant-glance:end -->

## Die Mitglieder {#the-members}

- **Dormant Force**: eine Wraith mit voller Stärke, mit Lasern, die dreimal so hart treffen wie die einer typischen Ausrüstung. Sie führt den Schwarm an, ist passiv, bis sie getroffen wird, und feuert **gerade Raketen** auf den ersten Piloten, der sie getroffen hat.
- **Dormant Pulse**: eine Paragon mit voller Stärke, mit schweren Lasern derselben Art, von denen jeder doppelt so hart trifft wie einer der Force, und eigenen Raketen. Eine Pulse hat weniger Laser als die Force, ihre ganze Salve ist also größer als die der Force, aber nicht doppelt so groß (die Zahlen stehen unten). Die Pulses fliegen dicht bei der Force, und wenn die Force zerstört wird, übernimmt eine von ihnen die Führung.

Sie sind passiv: Sie gehen nie auf einen Piloten los. Wird eines von ihnen getroffen, greifen die anderen in seiner Nähe mit ein, und zwar gegen den ersten Piloten, der es getroffen hat.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Finde ihn.** Die ganze Welt erfährt, wenn er auftaucht, und eine Markierung zeigt ihn auf den Karten der Gefahrensektoren und auf der Galaxiekarte. Er bleibt so lange auf einer Karte, wie die Liste *Auf einen Blick* sagt, fliegt dann zum Tor eines anderen Gefahrensektors und springt; er nimmt nie ein Tor aus den Gefahrensektoren hinaus und fliegt nie in den Ring des Schwarzen Lochs. Er fliegt mit dem Tempo seines langsamsten Schiffs und beginnt oder beendet, wie ein Pilot, keinen Sprung unter Beschuss. Ab Saisontag 11 erscheint er zuerst knapp außerhalb der Zone des [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), wo eine Gruppe außerhalb der Geschütze des Sumpfs auf ihn warten kann, und fliegt dann durch ein Tor von `DS-4` hinaus.
- **Allein oder zu wenigen ist er nicht zu schaffen.** Acht Piloten von Level 8 in Paragons mit x2- oder x4-Munition zerstören ihn in Alpha in etwa einer Minute und verlieren höchstens ein Schiff; eine Paragon allein wird zerstört, und mit x2-Munition auch drei oder vier. Die Schwärme von Beta und Gamma sind stärker ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)), diese Welten brauchen also größere Gruppen.
- **Seine Laser entscheiden den Kampf.** Zusammen können sie eine Paragon in unter einer Minute zerstören, selbst eine mit den besten Schilden in unter zwei Minuten, mit oder ohne Raketen: Bring deinen Schaden schnell ins Ziel, mit den besten Schilden, die du hast.
- **Schiff für Schiff.** Jedes Schiff hat seine eigene Hülle und seine eigene Bezahlung, die Force oder eine Pulse kann also zuerst zerstört werden. Der Schwarm wird erst ersetzt, wenn er ganz zerstört ist, und zwar nach der Zeit in der Liste *Auf einen Blick*.

## Die drei Schritte des Anführers {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Sein Kampf hat drei Schritte ([so funktionieren sie](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); jeder geschieht einmal.

- **Am Anfang**: Nimmt 70 % von jedem Treffer, solange einer seiner Dormant Pulses lebt.
- **Unter zwei Dritteln**: Seine Dormant Pulses feuern für 15 s alle 2,5 s eine Rakete.
- **Unter einem Drittel**: Solange alle seine Dormant Pulses leben, heilen sie es 6 s lang um 5 % seiner Hülle pro Sekunde.

<!-- mob-ladder:end -->

## Belohnungen und Beute {#rewards-and-drops}

Jedes Schiff zahlt für sich, nach dem Schaden, der ihm zugefügt wurde ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), und jedes lässt eine Kiste für den Piloten fallen, der ihm den meisten Schaden zugefügt hat. Die **Kiste der Force** ist der Preis: sehr viel x3- und x4-Munition, Epische Raketen einer Sorte und hin und wieder eine N.I.K.E. oder eine N.U.K.E. Die **Pulses** lassen vielleicht eine Ancient Control Unit, einen Power Core oder Dark Matter fallen. Eine Minute Kampf gegen den Schwarm zahlt mehr als eine Minute Kampf gegen den Crystalys, das bestbezahlte Alien. Ab Saisontag 11 zahlt jedes Schiff doppelt so viel (siehe die Liste *Auf einen Blick*); die Kisten bleiben gleich.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)). Die Credits, das Thulium, die EP und die Ehre in den Tabellen sind die Bezahlung vor Saisontag 11; ab diesem Tag zahlt ein Abschuss doppelt so viel.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Basis: Wraith mit 100 % der Hülle und 300 % des Laserschadens; Tempo und Reichweite bleiben die des Vorbilds. Feuert alle 5 s eine gerade Rakete ab: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| Schild | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| Tempo | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Raketenschaden, höchstens | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| Credits | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| Ehre | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| PvE-Punkte pro Abschuss | 25 | 25 | 25 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

Basis: Paragon mit 100 % der Hülle und 600 % des Laserschadens; Tempo und Reichweite bleiben die des Vorbilds. Feuert alle 5 s eine gerade Rakete ab: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| Schild | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| Laserschaden (eine Salve pro Sekunde) | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| Tempo | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Raketenschaden, höchstens | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| Credits | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| Erfahrung (EP) | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| Ehre | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| PvE-Punkte pro Abschuss | 11 | 11 | 11 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
