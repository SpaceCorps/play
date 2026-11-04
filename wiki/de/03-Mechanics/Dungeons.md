<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: Dungeons -->
# Dungeons

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; tor; tore; kriegsherr; labyrinth; stufe; beutezone; karte -->

Ein **Dungeon** heißt im Spiel **Tor**: ein geschlossenes Labyrinth mit einem **Kriegsherrn** an seinem Ende. Ein Stellvertreter oder der Anführer eines [Clans](/wiki/03-Mechanics/Clans.md) öffnet eines und bezahlt es aus der Clan-Bank, und Mitglieder des Clans fliegen gemeinsam als eine [Gruppe](/wiki/03-Mechanics/Groups.md) hinein. Sie kämpfen sich durch die Aliens des Labyrinths, öffnen Beutezonen, um aus jeder eine Karte zu wählen, und bringen den Kriegsherrn zu Fall. Jeder Pilot, der am Kampf teilgenommen hat, wird bezahlt, wenn der Kriegsherr fällt, im Rahmen der Grenzen weiter unten. Die Tore findest du im Reiter **Tore** der Clan-Seite.

Ein Tor ist ein Kampf allein gegen die Aliens: Niemand kann darin einen Clankameraden oder sonst jemanden angreifen. Die Aliens zahlen nichts. Die Belohnung kommt allein vom Kriegsherrn, du wirst also nur bezahlt, wenn du im Kampf dabei bist, während er fällt.

## Auf einen Blick {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Öffnet**: Ab Saisontag 4
- **Wer ein Tor öffnet**: Ein Stellvertreter oder der Anführer, der den Preis aus der Clan-Bank zahlt
- **Gruppe**: 4 bis 10 Mitglieder des Clans in einer Gruppe
- **Tore pro Tag**: 3 pro Clan und UTC-Tag, immer nur eines gleichzeitig offen
- **Tore gleichzeitig**: 6 in einer Welt
- **Instanzen**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labyrinthe**: 8; beim Öffnen eines Tors wird eines ausgewählt
- **Sammeln**: 10 min zum Sammeln und Starten. Ein Tor, das niemand startet, schließt sich, und sein Preis geht an die Clan-Bank zurück
- **Zeitlimit**: Stufe 1: 80 min, Stufe 2: 110 min, Stufe 3: 150 min ab dem Start. Läuft sie ab, scheitert das Tor und zahlt nichts
- **Leer**: Ein Tor, in dem 3 min lang niemand ist, scheitert
- **Nachdem der Kriegsherr gefallen ist**: Das Tor bleibt 2 min lang für die Piloten darin offen
- **Rückkehr**: Ein Pilot, der gegangen oder zerstört wurde, kann 3 Mal wieder hineinfliegen, mit 20 s Abstand dazwischen

<!-- dungeons-glance:end -->

## Der Ablauf {#how-a-run-goes}

1. **Rufen.** Im Reiter Tore wählt ein [Stellvertreter oder der Anführer](/wiki/03-Mechanics/Clans.md#hierarchy-roles) eine Stufe und drückt **Rufen**. Der Preis wird der [Clan-Bank](/wiki/03-Mechanics/Clans.md#clan-economy-taxation) entnommen, und das Tor erhält eine der oben aufgeführten Instanzen. Ein Tor, das niemand startet, schließt sich, und der Preis geht an die Bank zurück.
2. **Betreten.** Mitglieder des Clans drücken im Clan-Fenster **Betreten**, während sie fliegen. Die Piloten im Inneren sind die Gruppe des Tors.
3. **Starten.** Der Pilot, der das Tor geöffnet hat, oder ein Offizier drückt **Starten**, sobald genug Piloten drin sind. Danach können nur noch Piloten zurückkehren, die schon drin waren.
4. **Durchs Labyrinth kämpfen.** Du kommst an einem Ende des Labyrinths hinein, und am anderen wartet der Kriegsherr. Die Aliens schlafen in ihren Räumen und wachen in Rudeln auf, wenn die Gruppe näher kommt.
5. **Beutezonen öffnen.** Ringe im Labyrinth markieren die Zonen. Halte eine, und die Gruppe stimmt über eine Karte ab, die zusammen mit der Belohnung des Kriegsherrn ausgezahlt wird.
6. **Den Kriegsherrn besiegen.** Brich seinen Schild und seine Hülle und antworte auf seine Fähigkeiten. Wenn er fällt, ist das Tor geschafft.
7. **Bezahlt werden.** Die Belohnung kommt in dem Moment, in dem der Kriegsherr fällt. Das Tor bleibt für die Piloten im Inneren noch etwas länger offen und schließt sich dann.

## Betreten {#entering}

Um ein Tor zu betreten, brauchst du ein **Schiff im Flug**, starte also zuerst und öffne dann das Clan-Fenster, und eine [Gruppe](/wiki/03-Mechanics/Groups.md) mit genug Mitgliedern des Clans. Außerdem brauchst du das **Level**, das die Stufe verlangt, und du darfst nicht schon in einem anderen Tor sein. Die Gruppe eines Tors hat eine Größengrenze: Ist sie voll, kann niemand mehr hinein.

Ein Stellvertreter oder der Anführer öffnet ein Tor, für den Clan immer nur eines auf einmal und nur bis zur Zahl der Tore pro Tag. Die Clan-Bank muss den Preis haben. Ein Clan kann eine Stufe erst öffnen, wenn er die Stufe davor geschafft hat.

In einem Tor kannst du die Welt nicht wechseln, und die Jump CPU und die Base CPU funktionieren nicht. Mit der Schaltfläche **Verlassen** in der Leiste des Tors kommst du nach einer Bestätigung hinaus. Ein Pilot, der gegangen ist oder zerstört wurde, kann einige Male wieder hineinfliegen, mit einer kurzen Wartezeit dazwischen.

## Die Stufen {#the-stages}

Ein Tor hat eine Stufe, und die Stufe ist sein Schwierigkeitsgrad. Eine höhere Stufe hat zähere Aliens, die härter treffen, und sie zahlt mehr. Die Faktoren in der Tabelle gelten für jedes Alien und für den Kriegsherrn. Schaden meint Laser, Raketen und die Fähigkeiten des Kriegsherrn. Die Tabelle sagt auch, wie viele Aliens eine Stufe im Vergleich zur ersten schickt. Der **Preis** wird der Clan-Bank entnommen, wenn das Tor geöffnet wird.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stufe | Voraussetzung | Hülle und Schild der Aliens | Zahl der Aliens | Schaden der Aliens | Preis des Tors (Credits, aus der Clan-Bank) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Stufe 1** | Ab Level 6 | ×1 | ×1 | ×1 | 500.000 |
| **Stufe 2** | Ab Level 7 | ×1,5 | ×1 | ×1,25 | 1.000.000 |
| **Stufe 3** | Ab Level 8 | ×2,5 | ×1 | ×1,5 | 2.000.000 |

<!-- dungeons-stages:end -->

## Das Labyrinth {#the-maze}

Jedes Tor ist ein geschlossenes Labyrinth auf einer eigenen Instanz, einer der Instanzen aus der Liste oben, und das Labyrinth ist eines von mehreren Layouts. Ein Labyrinth ist ein Raster aus Räumen und Gängen mit festen Wänden. Schiffe können eine Wand nicht durchqueren, und eine Wand blockt Schüsse, sie ist also Deckung. Ein Meteor fällt von oben, und eine Wand hält ihn nicht auf.

## Die Aliens {#the-aliens}

Vier Arten von Aliens bewachen das Labyrinth. Sie schlafen in ihren Räumen und wachen auf, wenn ein Pilot näher kommt. Das Tor hält nur eine bestimmte Zahl von Aliens gleichzeitig in der Luft, und diese Zahl wächst mit der Größe der Gruppe, sodass ein zerstörtes Rudel das nächste hereinlässt. Eine größere Gruppe trifft im selben Verhältnis auf mehr Aliens, eine kleinere auf weniger, und eine Alienart fällt nie unter eins.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aliens, für eine Gruppe von 5 | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| Zusammen | 195 | 195 | 195 |
| Die Welle einer Beutezone | 10 × Gate Goombah und 1 × Gate Crystalys | 10 × Gate Goombah und 1 × Gate Crystalys | 10 × Gate Goombah und 1 × Gate Crystalys |

- **Gleichzeitig am Leben**: Höchstens 10 je Pilot der Gruppe und 70 insgesamt

<!-- dungeons-population:end -->

Die Arten der Reihe nach. Hülle und Schild sind die üblichen Werte mal dem Faktor der Stufe in der Spalte.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Sieht aus wie**: Goombah
- **Fliegt in Rudeln zu**: 6

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 32.000 | 48.000 | 80.000 |
| Schild | 48.000 | 72.000 | 120.000 |
| Laserschaden (eine Salve pro Sekunde) | 3.000 | 3.750 | 4.500 |
| Tempo | 180 | 180 | 180 |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | 1.800 | 1.800 | 1.800 |

### Gate Pirate

- **Sieht aus wie**: Pirate Boss
- **Fliegt in Rudeln zu**: 2
- **Rakete**: Alle 5 s eine gerade Rakete, Reichweite 970 Einheiten

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 300.000 | 450.000 | 750.000 |
| Schild | 50.100 | 75.150 | 125.250 |
| Laserschaden (eine Salve pro Sekunde) | 200 | 250 | 300 |
| Raketenschaden | 5.000 | 6.250 | 7.500 |
| Tempo | 92 | 92 | 92 |
| Laserreichweite | 700 | 700 | 700 |
| Aggro-Radius | 1.800 | 1.800 | 1.800 |

### Gate Crystalys

- **Sieht aus wie**: Crystalys
- **Fliegt in Rudeln zu**: 2

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 256.000 | 384.000 | 640.000 |
| Schild | 160.000 | 240.000 | 400.000 |
| Laserschaden (eine Salve pro Sekunde) | 10.000 | 12.500 | 15.000 |
| Tempo | 230 | 230 | 230 |
| Laserreichweite | 900 | 900 | 900 |
| Aggro-Radius | 2.400 | 2.400 | 2.400 |

### Gate Crystalys Twin

- **Sieht aus wie**: Crystalys, 1,4-mal so groß
- **Fliegt in Rudeln zu**: 1

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 512.000 | 768.000 | 1.280.000 |
| Schild | 320.000 | 480.000 | 800.000 |
| Laserschaden (eine Salve pro Sekunde) | 20.000 | 25.000 | 30.000 |
| Tempo | 230 | 230 | 230 |
| Laserreichweite | 900 | 900 | 900 |
| Aggro-Radius | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## Der Kriegsherr {#the-warlord}

Der Kriegsherr wartet im Raum am fernen Ende des Labyrinths, und er ist das Einzige in einem Tor, das zahlt. Er ist ein riesig gewachsener Crystalys. Seine Hülle und sein Schild wachsen mit der Größe der Gruppe: Je mehr Piloten hineingehen, desto zäher ist er, im selben Verhältnis. Er bleibt in seinem Raum und setzt seine Fähigkeiten nacheinander in zufälliger Reihenfolge ein, jede mit eigener Abklingzeit.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Sieht aus wie**: Crystalys, 3-mal so groß
- **Schildaufladung**: 3.000 pro Sekunde, nach 15 s ohne Schaden

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 10.000.000 | 15.000.000 | 25.000.000 |
| Schild | 8.000.000 | 12.000.000 | 20.000.000 |
| Laserschaden (eine Salve pro Sekunde) | 8.000 | 10.000 | 12.000 |
| Tempo | 120 | 120 | 120 |
| Laserreichweite | 1.100 | 1.100 | 1.100 |

Hülle und Schild oben gelten für eine Gruppe von 5. Sie wachsen mit der Gruppe: Das sind Hülle und Schild des Kriegsherrn zusammen, nach der Zahl der Piloten in der Gruppe beim Start des Tors.

| Piloten in der Gruppe | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14.400.000 | 21.600.000 | 36.000.000 |
| 5 | 18.000.000 | 27.000.000 | 45.000.000 |
| 6 | 21.600.000 | 32.400.000 | 54.000.000 |
| 7 | 25.200.000 | 37.800.000 | 63.000.000 |
| 8 | 28.800.000 | 43.200.000 | 72.000.000 |
| 9 | 32.400.000 | 48.600.000 | 81.000.000 |
| 10 | 36.000.000 | 54.000.000 | 90.000.000 |

<!-- dungeons-boss:end -->

### Seine Fähigkeiten {#its-abilities}

- **Der rote Ring** der Lebensraub-Aura verletzt jeden Piloten darin und heilt den Kriegsherrn mit dem Schaden. Auch die Schildabsorption hat einen roten Ring: Er entzieht den Schilden der Piloten darin Energie und lädt damit den des Kriegsherrn auf. Verlasse in beiden Fällen den Ring oder stell dich hinter eine Wand.
- **Die bernsteinfarbenen Ringe** des Meteoritenhagels zeigen, wo einen Moment später Meteore einschlagen. Bleib in Bewegung und verlasse den Ring, bevor er einschlägt.
- **Fokus auf Heiler** richtet den Kriegsherrn auf jeden, der einen anderen Piloten heilt, und er trifft diesen Piloten härter. Verteile die Heilung.
- **Die Raketensalve** schickt zielsuchende Raketen auf zufällige Piloten. Eine EMP Charge oder eine Tarnung schüttelt sie ab.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fähigkeit | Anlauf | Dauer | Abklingzeit | Ringradius (Einheiten) | Der Kriegsherr gewinnt höchstens zurück |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Lebensraub-Aura** | 2 s | 15 s | 2 min | 900 | 8 % seiner Hülle und seines Schilds |
| **Meteoritenhagel** | 1,5 s | 3 Salven, 4 s Abstand | 2 min | 420 | – |
| **Fokus auf Heiler** | 1 s | 45 s | 2 min | – | – |
| **Raketensalve** | 1,5 s | 45 s | 2 min | – | – |
| **Schildabsorption** | 2 s | 15 s | 2 min | 900 | 6 % seines Schilds |

| Fähigkeit | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | :--- | :--- | :--- |
| **Lebensraub-Aura** | 8.000 pro Sekunde | 10.000 pro Sekunde | 12.000 pro Sekunde |
| **Meteoritenhagel** | 6 Meteore pro Salve, je 40.000 | 8 Meteore pro Salve, je 50.000 | 10 Meteore pro Salve, je 60.000 |
| **Fokus auf Heiler** | Sein Laser trifft den Piloten, auf den er sich richtet, ×1,5 so hart | Sein Laser trifft den Piloten, auf den er sich richtet, ×1,5 so hart | Sein Laser trifft den Piloten, auf den er sich richtet, ×1,5 so hart |
| **Raketensalve** | 6.500 pro Rakete, eine alle 15 s | 8.125 pro Rakete, eine alle 15 s | 9.750 pro Rakete, eine alle 15 s |
| **Schildabsorption** | 10.000 Schild pro Sekunde | 12.500 Schild pro Sekunde | 15.000 Schild pro Sekunde |

<!-- dungeons-abilities:end -->

## Beutezonen {#loot-zones}

Ein Ring auf dem Boden des Labyrinths markiert jede Beutezone, sobald die Gruppe sie gefunden hat. Bleibe kurz darin stehen, und die Zone erwacht, und eine Welle Aliens kommt auf sie zu. Dann muss die Gruppe die Zone **halten**: einen Piloten darin lassen, bis der Balken voll ist. Aliens im Ring halten den Balken an, und er läuft zurück, solange niemand darin ist, räumt also zuerst die Welle. Wenn sich die Zone öffnet, sieht die Gruppe drei verschiedene Karten und **stimmt** über eine ab. Eine Zone öffnet sich nur einmal, und ihre Welle kommt nicht wieder.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Beutezonen**: 4 in jedem Labyrinth
- **Radius**: 450 Einheiten
- **Wecken**: 2 s lang im Ring stehen
- **Halten**: Einen Piloten 30 s lang im Ring halten. Das Halten stoppt, solange 3 oder mehr Aliens im Ring sind, und läuft zurück, solange niemand darin ist
- **Wählen**: Die Gruppe hat 45 s zum Abstimmen. Die Abstimmung endet früher, wenn jeder anwesende Pilot gewählt hat oder eine Karte mehr als die Hälfte der Stimmen hat

<!-- dungeons-zones:end -->

### Die Karten {#the-cards}

Die Karten werden eine nach der anderen aus dem Pool unten gezogen. Die Chance ist die einer Karte bei einem Zug. Eine Karte mit vielen Exemplaren geht an jeden bezahlten Piloten, eine Ausrüstungskarte mit einem Exemplar an einen Piloten der Gruppe. Ein Pilot, der nicht bezahlt wird, bekommt auch keine Karte, und eine Zone, die in einem gescheiterten Tor geöffnet wurde, zahlt nichts.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Karte | Stufe 1 | Stufe 2 | Stufe 3 | Chance | Geht an |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | 21 % | Jeden bezahlten Piloten |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12 % | Jeden bezahlten Piloten |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12 % | Jeden bezahlten Piloten |
| Velkonite | 200 | 300 | 500 | 12 % | Jeden bezahlten Piloten |
| Orvium | 200 | 300 | 500 | 12 % | Jeden bezahlten Piloten |
| Ultra Core | 5.000 | 7.500 | 12.500 | 10 % | Jeden bezahlten Piloten |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 8 % | Jeden bezahlten Piloten |
| Dark Matter | 5 | 8 | 12 | 8 % | Jeden bezahlten Piloten |
| Dark Matter Plate | 1 | 1 | 2 | 4 % | Jeden bezahlten Piloten |
| Engine III | 1 | 1 | 1 | 0,25 % | Einen Piloten der Gruppe |
| Heavy Shield Core | 1 | 1 | 1 | 0,25 % | Einen Piloten der Gruppe |
| Adaptive Core III | 1 | 1 | 1 | 0,25 % | Einen Piloten der Gruppe |
| Starfire-III | 1 | 1 | 1 | 0,25 % | Einen Piloten der Gruppe |

- **Ausrüstung**: Die Karten mit einem Exemplar sind Ausrüstung: zusammen 1 % der Karten

<!-- dungeons-cards:end -->

## Belohnung {#pay}

Wenn der Kriegsherr fällt, wird jeder Pilot, der es verdient hat, einmal für den Durchgang bezahlt. Die Karten, die die Gruppe gewählt hat, kommen zur Belohnung der Stufe hinzu. Es gibt keinen Weltfaktor: Die Belohnung ist in jeder Welt gleich.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stufe | Ehre | Erfahrung | Credits | Thulium | x4-Munition | PvE-Rangpunkte |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Stufe 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 600 |
| **Stufe 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 1.500 |
| **Stufe 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 2.400 |

<!-- dungeons-pay:end -->

### Wer bezahlt wird {#who-is-paid}

Die Aliens zahlen nie. Ein Durchgang wird auch dann vollständig gespielt, wenn er nichts zahlt, und der Ergebnisbildschirm sagt, warum. Der Zutritt wird nie verweigert, weil du für eine Stufe schon bezahlt wurdest: Dieser Durchgang zahlt dann nur nichts.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ein Tag**: Eine Stufe zahlt einem Piloten einmal pro UTC-Tag: an dem Tag, an dem der Kriegsherr fällt
- **Eine Woche**: Ein Pilot wird für höchstens 10 Stufen-Abschlüsse pro UTC-Woche bezahlt, Montag bis Sonntag
- **Im Tor**: Mindestens 2 min insgesamt
- **Anteil am Kampf**: Mindestens eines davon: Schaden in Höhe von 2 % der Hülle und des Schilds des Kriegsherrn verursacht; 10 Aliens des Tors zerstört; andere Piloten im Kampf gegen den Kriegsherrn um 50.000 geheilt

<!-- dungeons-rules:end -->

### Was ein Tag und eine Woche wert sind {#what-a-day-and-a-week-are-worth}

Was ein Pilot an einem Tag und in der besten Woche bekommen kann, die die Grenzen erlauben. Die letzte Spalte zeigt, was die Belohnung deinen [PvE-Punkten](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) hinzufügt.

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Belohnung je Pilot | Ehre | Erfahrung | Credits | Thulium | x4-Munition | PvE-Rangpunkte |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Ein Tag, jede Stufe einmal | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 4.500 |
| Die beste Woche: 7 × Stufe 3 und 3 × Stufe 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 21.300 |

Die Erfahrung eines bezahlten Abschlusses zählt für deine PvE-Rangpunkte: ein Punkt je 1.000 Erfahrung.

<!-- dungeons-totals:end -->

## Die Belohnung der Clan-Bank {#clan-bank-reward}

Auch die Clan-Bank wird bezahlt, in Credits und nicht in Thulium, wenn der Clan eine Stufe zum ersten Mal in einer Saison schafft. Der Clan muss alt genug sein, und genug Piloten dieses Durchgangs müssen bezahlt werden. Die Bank wird pro Stufe einmal in einer Saison bezahlt.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stufe | Credits für die Clan-Bank |
| :--- | ---: |
| **Stufe 1** | 10.000.000 |
| **Stufe 2** | 20.000.000 |
| **Stufe 3** | 30.000.000 |

- **Alter des Clans**: Mindestens 3 T
- **Bezahlte Piloten**: Mindestens 3 im Tor

<!-- dungeons-clan:end -->

## Tipps {#tips}

- Räume die Welle einer Zone, bevor du versuchst, sie zu halten, und kämpfe im Ring, wenn Aliens hereinkommen.
- Nutze die Wände: Laser durchqueren sie nicht, und die Ringe des Kriegsherrn enden an ihnen.
- Spare eine EMP Charge für die Raketensalve auf.
- Behalte die Uhr in der Leiste des Tors im Blick. Läuft die Zeit ab, scheitert das Tor und zahlt nichts.
