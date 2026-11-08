<!-- wiki-i18n source: 554085379d2ae5df -->
<!-- wiki-i18n title: Tesseract-Schwarm -->
# Tesseract-Schwarm {#tesseract-swarm}

Der Tesseract-Schwarm besteht aus einem einzigen riesigen Mutterschiff, dem **Tesseract**, und den **Facets**, die es aussendet, solange es getroffen wird. Der Tesseract hat seinen festen Heimatplatz im [Gefahrensektor](/wiki/01-General/Danger-Sectors.md) `DS-4`, besitzt keine eigene Waffe und verlässt seinen Sektor nie. Er ist für eine sehr große Gruppe der stärksten Piloten gedacht: Seine Hülle und sein Schild übertreffen einen Crystalys bei Weitem, und er heilt sich selbst, sobald man ihn in Ruhe lässt. Die Gefahrensektoren sind PvP-Sektoren, der Kampf kann also neben den Facets auch Rivalen anlocken.

## Auf einen Blick {#at-a-glance}

<!-- tesseract-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Wo**: Der Gefahrensektor `DS-4`
- **Wie viele**: Einer in jeder Welt
- **Erscheint**: Ab Saisontag 4 bis zum Wipe (Beta und Gamma: ab Saisontag 1)
- **Anführer**: Tesseract
- **Heimat**: Im Umkreis von 2.500 Einheiten um den Punkt 25.900, 6.100 der Sektorkarte
- **Regeneration**: In Alpha 125.000 HP pro Sekunde, erst die Hülle, dann der Schild, sobald 5 s lang kein Schaden entstanden ist
- **Begleiter**: Bis zu 100 × Facet, alle 5 s 20 weitere, solange der Anführer getroffen wird
- **Begleiter kommen**: Nur solange der Anführer in den letzten 5 s getroffen wurde, im Umkreis von 400 Einheiten um ihn
- **Jäger**: Jeder Facet fliegt eigene Strecken um den Anführer, im Umkreis von 3.600 Einheiten um ihn, und verfolgt niemanden. Er feuert auf den nächsten Piloten, der den Anführer getroffen hat, wenn dieser in seiner Reichweite ist. Ohne Ziel fliegt er weiter um den Anführer und verschwindet 20 s nach dem letzten Treffer
- **Anführer zerstört**: Die Begleiter verschwinden 1 min nach der Zerstörung des Anführers, auch wenn sie gerade angreifen
- **Kehrt zurück**: 30 min nach der Zerstörung des Anführers, im selben Sektor
- **Meldungen**: Die Piloten des Sektors erfahren, wann der Anführer auftaucht und wann er zerstört wird. Das sind Systemzeilen: Sie erscheinen im Tab **System** des Chats, mit Zähler für Ungelesenes, und nicht in **Global** oder **Lokal**. Der Kill-Feed nennt den Piloten, dem der Abschuss gutgeschrieben wird.

<!-- tesseract-glance:end -->

## Die Mitglieder {#the-members}

- **Tesseract**: ein würfelförmiges Mutterschiff, um ein Vielfaches größer als ein Crystalys, aus dunklem Schmiedeeisen mit glühenden Nähten und mit seinem Namen darüber. Eine Bucht in seiner Frontwand öffnet sich, solange er getroffen wird, und ein leuchtender Würfel dreht sich in einem Käfig auf seinem Dach. Er ist passiv: Er treibt langsam in seinem Heimatbereich umher, solange ihn niemand verletzt, und bleibt stehen und hält seinen Platz, sobald ein Pilot ihn trifft. Er feuert nicht und jagt niemanden; seine Verteidigung sind seine Größe, seine Selbstheilung und die Facets, die er aussendet.
- **Facet**: ein kleines, schnelles Schiff aus demselben dunklen Eisen, mit glühenden Kanten, einer leuchtenden Linse in der Nase und zwei schwebenden Flügelplatten. Es existiert nur, solange der Tesseract getroffen wird. Es verfolgt niemanden: Es bleibt beim Tesseract, fliegt eigene kurze Strecken zu zufälligen Orten rund um ihn und feuert auf den nächsten Piloten, der den Tesseract getroffen hat, sobald einer in seiner Reichweite ist. Es zieht ab, wenn der Tesseract in Ruhe gelassen wird. Es ist schneller als jedes Schiff, Weglaufen vor dem Schwarm hilft also nicht, aber ein Pilot, der weit vom Tesseract wegbleibt, wird nie beschossen.

## Wie der Kampf verläuft {#how-the-fight-goes}

- **Bring eine sehr große Gruppe mit und schlagt gemeinsam zu.** Hülle und Schild des Tesseract sind ein Vorrat von Millionen Punkten, der Kampf dauert also selbst mit einer großen Gruppe starker Schiffe lange, und die Bezahlung wird nach Schaden aufgeteilt: Jeder anwesende Pilot zählt.
- **Lass ihn nie in Ruhe.** Hat ihn die Zeit aus der Liste *Auf einen Blick* lang niemand verletzt, heilt er erst seine Hülle und dann seinen Schild in dieser Geschwindigkeit; eine Pause von wenigen Sekunden kann also eine lange Minute Arbeit zunichtemachen. Ein Tesseract, der vollständig geheilt ist, vergisst, wer ihn verletzt hat: Bezahlung und Kiste richten sich nach dem Schaden des Kampfes, der ihn zerstört.
- **Jeder Treffer ruft die Facets.** Solange der Tesseract getroffen wird, erscheint alle paar Sekunden ein Schub Facets in seiner Nähe, bis zur Höchstzahl aus der Liste *Auf einen Blick*. Wird er nicht getroffen, kommt keiner, und die schon vorhandenen warten und ziehen ab.
- **Die Facets fliegen rund um den Tesseract und feuern auf jeden in Reichweite.** Sie jagen weder den Piloten mit dem meisten Schaden noch sonst einen einzelnen: Jeder Facet fliegt eigene kurze Strecken zu zufälligen Orten eines weiten Rings um den Tesseract, in alle Richtungen, und sobald ein Pilot, der den Tesseract getroffen hat, in seiner Reichweite ist, feuert er auf den nächsten dieser Piloten. Eine Gruppe, die dicht beisammen bleibt, ist für weniger Facets gleichzeitig in Reichweite und teilt sich deren Feuer, anders als eine Gruppe, die rund um den Tesseract verteilt ist. Ein Facet hat wenig Hülle und Schild, und ihn abzuschießen zahlt nichts, nimmt aber den Piloten in seiner Nähe eine Salve ab. Ein Pilot, der den Tesseract nicht getroffen hat, ist nicht ihr Ziel.
- **Wer weit genug wegbleibt, wird in Ruhe gelassen.** Die Facets entfernen sich nie weiter vom Tesseract als die Entfernung aus der Liste *Auf einen Blick*; wer jenseits davon und der Laserreichweite eines Facets bleibt, wird nicht beschossen, wie viel Schaden er auch gemacht hat. Ein Facet ohne Ziel fliegt weiter um den Tesseract und zieht ab, wenn der Tesseract in Ruhe gelassen wird.
- **Beta und Gamma sind härter.** Die Schwärme dieser Welten sind stärker ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)), und das gilt auch für die Selbstheilung des Tesseract und die Salve jedes Facets.
- **Die Gefahrensektoren sind PvP.** Ein Rivale kann die Gruppe mitten im Kampf angreifen und auf die Kiste warten: Sie gehört 30 Sekunden lang dem Piloten mit dem meisten Schaden (und seinem Clan), danach jedem ([Frachtkisten](/wiki/03-Mechanics/Cargo.md)). Komm nicht allein.
- **Der Tesseract kommt zurück**, nach der Zeit aus der Liste *Auf einen Blick*, mit voller Stärke und an seinem Heimatplatz.

## Belohnungen und Beute {#rewards-and-drops}

Der Tesseract zahlt für den Kampf, der er ist: so viel wie viele Crystalys zusammen, und für den Schaden, den er einsteckt, mehr als ein Crystalys, das bestbezahlte Alien. Die Bezahlung wird nach Schaden unter den Piloten aufgeteilt, die ihn bekämpft haben ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Seine Kiste gehört dem Piloten mit dem meisten Schaden und enthält Power Cores und Ancient Control Units, hin und wieder Dark Matter. Die Hüllenplatten liegen nicht darin: Jeder Pilot, den der Abschuss bezahlt, bekommt seine eigene [private Kiste](/wiki/03-Mechanics/Cargo.md#private-boxes) mit Platten, die nur er sehen und nehmen kann, 10 Minuten lang. Sie wird für seinen Schadensanteil ausgewürfelt, wie die Beute eines [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot): Wer ein Fünftel des Schadens gemacht hat, bekommt etwa ein Fünftel der Mengen aus der Tabelle, und in einer Gruppe bekommt jeder Pilot seinen Teil vom Anteil der Gruppe, so wie die Bezahlung geteilt wird. Die Facets zahlen nichts, lassen nichts fallen und bringen keine PvE-Punkte: Sie abzuschießen ist kein Farmen.

## Die Werte {#the-numbers}

Die Werte der Schwarmschiffe in den drei Welten ([Welten](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- tesseract-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Tesseract

Basis: Crystalys mit 625 % der Hülle; ohne Waffe, Schild und Tempo sind eigene Werte.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 1.600.000 | 2.400.000 | 3.200.000 |
| Schild | 1.200.000 | 1.800.000 | 2.400.000 |
| Laserschaden (eine Salve pro Sekunde) | keiner | keiner | keiner |
| Tempo | 30 | 30 | 30 |
| Laserreichweite | – | – | – |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Heilt pro Sekunde, nach 5 s ohne Schaden (erst Hülle, dann Schild) | 125.000 | 187.500 | 250.000 |
| Credits | 900.000 | 1.800.000 | 2.700.000 |
| Thulium | 2.400 | 4.800 | 7.200 |
| Erfahrung (EP) | 144.000 | 288.000 | 432.000 |
| Ehre | 624 | 1.248 | 1.872 |
| PvE-Punkte pro Abschuss | 42 | 42 | 42 |

**Beute**: eine Kiste, für den Piloten mit dem meisten Schaden.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Power Core | 70 % | 1–2 |
| Ancient Control Unit | 35 % | 1 |
| Dark Matter | 2,5 % | 1 |

**Beute für jeden Piloten, den der Abschuss bezahlt**: je eine weitere Kiste, nur für ihn, mit seinem Anteil an diesen Mengen.

| Gegenstand | Chance | Menge |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 100 % | 1–2 |
| Velkonite Reinforced Plate | 60 % | 3–6 |
| Orvium Reinforced Plate | 40 % | 1–2 |

### Facet

Basis: Seeker mit 2.500 % der Hülle und 309 % des Laserschadens; Schild, Tempo und Reichweite sind eigene Werte.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Hülle | 20.000 | 30.000 | 40.000 |
| Schild | 16.000 | 24.000 | 32.000 |
| Laserschaden (eine Salve pro Sekunde) | 556 | 834 | 1.112 |
| Tempo | 750 | 750 | 750 |
| Laserreichweite | 600 | 600 | 600 |
| Aggro-Radius | nur wenn angegriffen | nur wenn angegriffen | nur wenn angegriffen |
| Credits | 0 | 0 | 0 |
| Thulium | 0 | 0 | 0 |
| Erfahrung (EP) | 0 | 0 | 0 |
| Ehre | 0 | 0 | 0 |
| PvE-Punkte pro Abschuss | 0 | 0 | 0 |

**Beute**: keine. Der Abschuss zahlt nichts.

<!-- tesseract-members:end -->
