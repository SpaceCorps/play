<!-- wiki-i18n source: 9421722a69e53475 -->
<!-- wiki-i18n title: Dungeons -->
# Dungeons

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; clan dungeon alerts; dungeon goombah; dungeon pirate; dungeon crystalys; dungeon warlord; 75 percent; three quarters; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; tor; tore; kriegsherr; labyrinth; stufe; beutezone; karte; portal; clan-portal; booster; nebel; wächter; startraum; verschlossener raum; schwarm-unterstützung; zone des chaos; clan-tor-hinweise; dungeon; dungeons; clan-dungeon; clan-dungeon-hinweise; drei viertel; 75 prozent; kerker -->

Ein **Dungeon** ist ein geschlossenes Labyrinth mit einem **Kriegsherrn** an seinem Ende (vor 0.5.2 hieß er im Spiel Tor). Ein Stellvertreter oder der Anführer eines [Clans](/wiki/03-Mechanics/Clans.md) öffnet eines und bezahlt es aus der Clan-Bank, und Mitglieder des Clans fliegen gemeinsam als eine [Gruppe](/wiki/03-Mechanics/Groups.md) hinein. Sie kämpfen sich durch die Aliens des Labyrinths, öffnen Beutezonen, um aus jeder eine Karte zu wählen, und bringen den Kriegsherrn zu Fall. Jeder Pilot, der am Kampf teilgenommen hat, wird bezahlt, wenn der Kriegsherr fällt, im Rahmen der Grenzen weiter unten. Die Dungeons findest du im Reiter **Dungeons** der Clan-Seite.

Ein Dungeon ist ein Kampf allein gegen die Aliens: Niemand kann darin einen Clankameraden oder sonst jemanden angreifen. Die Aliens zahlen nichts. Die Belohnung kommt allein vom Kriegsherrn, du wirst also nur bezahlt, wenn du im Kampf dabei bist, während er fällt.

## Auf einen Blick {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Öffnet**: Ab Saisontag 1
- **Wer einen Dungeon öffnet**: Ein Stellvertreter oder der Anführer, der den Preis aus der Clan-Bank zahlt
- **Gruppe**: 4 bis 10 Mitglieder des Clans in einer Gruppe
- **Dungeons pro Tag**: 3 pro Clan und UTC-Tag, immer nur eines gleichzeitig offen
- **Dungeons gleichzeitig**: 6 in einer Welt
- **Instanzen**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Labyrinthe**: 8; beim Öffnen eines Dungeons wird einer ausgewählt
- **Boss-Raum**: Öffnet sich, wenn 75 % der Crystalys und ihrer Twins zerstört sind, aufgerundet
- **Sammeln**: 10 min zum Sammeln und Starten. Ein Dungeon, den niemand startet, schließt sich, und sein Preis geht an die Clan-Bank zurück
- **Zeitlimit**: Stufe 1: 95 min, Stufe 2: 130 min, Stufe 3: 165 min ab dem Start. Läuft sie ab, scheitert der Dungeon und zahlt nichts
- **Leer**: Ein Dungeon, in dem 3 min lang niemand ist, scheitert
- **Nachdem der Kriegsherr gefallen ist**: Der Dungeon bleibt 2 min lang für die Piloten darin offen
- **Rückkehr**: Ein Pilot, der gegangen oder zerstört wurde, kann 3 Mal wieder hineinfliegen, mit 20 s Abstand dazwischen

<!-- dungeons-glance:end -->

## Der Ablauf {#how-a-run-goes}

1. **Rufen.** Im Reiter Dungeons wählt ein [Stellvertreter oder der Anführer](/wiki/03-Mechanics/Clans.md#hierarchy-roles) eine Stufe und drückt **Rufen**. Der Preis wird der [Clan-Bank](/wiki/03-Mechanics/Clans.md#clan-economy-taxation) entnommen, und der Dungeon erhält eine der oben aufgeführten Instanzen. Ein Dungeon, den niemand startet, schließt sich, und der Preis geht an die Bank zurück.
2. **Betreten.** Mitglieder des Clans drücken im Clan-Fenster **Betreten**, während sie fliegen, springen durch das Clan-Portal oder drücken auf der Hinweiskarte **Beitreten** (siehe Betreten). Alle landen im Startraum, und die Piloten im Inneren sind die Gruppe des Dungeons.
3. **Starten.** Der Startraum ist ein kleiner Raum an einem Ende des Labyrinths, und seine Tür bleibt zu, solange sich der Dungeon sammelt. Es gibt dort keine Aliens, du kannst also sicher warten. Der Dungeon **startet von selbst**, sobald jeder Pilot, auf den es wartet, drin ist und die Gruppe groß genug ist. Es wartet auf die Mitglieder des Clans, die online und nicht abwesend sind und in der Gruppe eines Piloten sind, der hineingekommen ist, und es startet sofort, wenn die Gruppe voll ist. Der Pilot, der den Dungeon geöffnet hat, oder ein Offizier kann **Starten** drücken, um früher mit den Piloten zu beginnen, die drin sind, wenn es genug sind. Ein Pilot, der geht, wird nicht mehr erwartet. Wenn der Dungeon startet, öffnet sich die Tür für immer, und danach können nur noch Piloten zurückkehren, die schon drin waren.
4. **Durchs Labyrinth kämpfen.** Du kommst an einem Ende des Labyrinths hinein, und am anderen wartet der Kriegsherr in einem verschlossenen Raum. Das Labyrinth ist dunkel: Du siehst nur, was die Gruppe erkundet hat und was nahe an ihren Schiffen liegt. Die Aliens schlafen in Rudeln in den Gängen, und ein Rudel, das aufwacht, jagt die Gruppe durchs Labyrinth.
5. **Beutezonen öffnen.** Ringe im Labyrinth markieren die Zonen. Halte eine, und die Gruppe stimmt über eine Karte ab, die zusammen mit der Belohnung des Kriegsherrn ausgezahlt wird.
6. **Den Raum des Kriegsherrn entsperren.** Zerstöre drei Viertel der Crystalys und ihrer Twins des Labyrinths, und die Tür zum Raum des Kriegsherrn öffnet sich. Bis dahin kann der Kriegsherr nicht verletzt werden. Die übrigen Aliens bleiben, wo sie sind, und du kannst sie auch zerstören.
7. **Den Kriegsherrn besiegen.** Brich seinen Schild und seine Hülle und antworte auf seine Fähigkeiten. Wenn er fällt, ist der Dungeon geschafft.
8. **Bezahlt werden.** Die Belohnung kommt in dem Moment, in dem der Kriegsherr fällt. Der Dungeon bleibt für die Piloten im Inneren noch etwas länger offen und schließt sich dann.

## Betreten {#entering}

Um einen Dungeon zu betreten, brauchst du ein **Schiff im Flug**, starte also zuerst und öffne dann das Clan-Fenster, und eine [Gruppe](/wiki/03-Mechanics/Groups.md) mit genug Mitgliedern des Clans. Außerdem brauchst du das **Level**, das die Stufe verlangt, und du darfst nicht schon in einem anderen Dungeon sein. Die Gruppe eines Dungeons hat eine Größengrenze: Ist sie voll, kann niemand mehr hinein.

Ein Stellvertreter oder der Anführer öffnet einen Dungeon, für den Clan immer nur eines auf einmal und nur bis zur Zahl der Dungeons pro Tag. Die Clan-Bank muss den Preis haben. Ein Clan kann eine Stufe erst öffnen, wenn er die Stufe davor geschafft hat.

In einem Dungeon kannst du die Welt nicht wechseln, und die Jump CPU und die Base CPU funktionieren nicht. Mit der Schaltfläche **Verlassen** im Fenster Clan-Dungeon kommst du hinaus. Sie fragt vorher nach einer Bestätigung, außer wenn der Kriegsherr schon gefallen ist: Dann gehst du sofort. Ein Pilot, der gegangen ist oder zerstört wurde, kann einige Male wieder hineinfliegen, mit einer kurzen Wartezeit dazwischen.

### Das Clan-Portal und der Hinweis {#the-clan-portal-and-the-call}

Wenn ein Dungeon geöffnet wird, bekommt der Clan dafür ein **Portal** auf der Heimatkarte jedes Konzerns (`M-1`, `T-1` und `G-1`), ein Stück außerhalb der Schutzzone der Station. Nur die Piloten des Clans sehen es: Für alle anderen ist es nicht da. Es hat keine eigene Schutzzone. Fliege hin und springe wie an jedem anderen Portal, und es bringt dich nach den Regeln von **Betreten** in den Dungeon: ein Schiff im Flug, eine Gruppe mit genug Mitgliedern des Clans, das Level der Stufe und Platz in der Gruppe. Sobald der Dungeon gestartet ist, können es nur noch Piloten nutzen, die schon drin waren. Das Portal verschwindet, wenn der Dungeon vorbei ist.

Solange sich der Dungeon deines Clans sammelt und du woanders fliegst, erreicht dich ein **Hinweis**: eine Karte oben im Flugbild, mit einem Ton. Sie sagt, wer den Dungeon geöffnet hat, wie viele Piloten drin sind und wie lange der Dungeon noch offen bleibt. **Beitreten** fliegt dich hinein, so wie **Betreten** im Reiter Dungeons, und wenn du den Dungeon verlässt, kommt dein Schiff dorthin zurück, wo es war. Beitreten ist ausgegraut, solange deine Gruppe zu klein ist. **Nicht jetzt** blendet die Karte für diesen Dungeon aus. Ist deine Gruppe schon drin und wartet der Dungeon auf dich, steht das auf der Karte. Die Karte erreicht die Piloten des Clans, die fliegen (nicht die, die an einer Station angedockt sind) und die das Level haben, das die Stufe verlangt. Karte und Ton kannst du mit **Clan-Dungeon-Hinweise** unter Einstellungen › Allgemein › Gruppen ausschalten.

### Das Fenster Clan-Dungeon {#the-clan-dungeon-window}

In einem Dungeon hat der Durchgang ein eigenes Fenster, **Clan-Dungeon**. Es zeigt die vergangene und die verbleibende Zeit, wie viele Aliens fliegen und wie viele zerstört wurden, was die Gruppe jetzt tun soll (das Labyrinth erkunden, eine Zone halten, den Boss finden, drei Viertel der Crystalys und ihrer Twins zerstören, den Kriegsherrn besiegen), den Haltebalken, solange du in einer Zone stehst, die Fähigkeit des Kriegsherrn mit ihrem Countdown und die Schaltfläche **Verlassen**. Es ist ein Fenster wie die anderen: Ziehe es an seiner Titelleiste und schließe es mit dem roten Licht in seiner Ecke. Es öffnet sich von selbst, wenn du einen Dungeon betrittst, einmal für jeden Dungeon: Schließt du es, bleibt es bis zum nächsten Dungeon zu. Die Symbolleiste hat dafür eine Schaltfläche **Clan-Dungeon**, solange du in einem Dungeon bist. Ist das Fenster geschlossen, erscheint eine Fähigkeit des Kriegsherrn, die gleich startet oder gerade wirkt, als einzeilige Leiste mit Namen und Countdown. Klicke auf die Leiste, um das Fenster wieder zu öffnen.

## Die Stufen {#the-stages}

Ein Dungeon hat eine Stufe, und die Stufe ist sein Schwierigkeitsgrad. Eine höhere Stufe hat zähere Aliens, die härter treffen, und sie zahlt mehr. Die Faktoren in der Tabelle sind die der Aliens. Schaden meint ihre Laser und Raketen. Der Kriegsherr folgt der Tabelle nicht: Er hat für jede Stufe eigene Werte, weiter unten. Die Tabelle sagt auch, wie viele Aliens eine Stufe im Vergleich zur ersten schickt. Der **Preis** wird der Clan-Bank entnommen, wenn der Dungeon geöffnet wird.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stufe | Voraussetzung | Hülle und Schild der Aliens | Zahl der Aliens | Schaden der Aliens | Preis des Dungeons (Credits, aus der Clan-Bank) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Stufe 1** | Ab Level 6 | ×1 | ×1 | ×1 | 500.000 |
| **Stufe 2** | Ab Level 7 | ×1,5 | ×1 | ×1,5 | 1.000.000 |
| **Stufe 3** | Ab Level 8 | ×2 | ×1 | ×2 | 2.000.000 |

<!-- dungeons-stages:end -->

## Das Labyrinth {#the-maze}

Jeder Dungeon ist ein geschlossenes Labyrinth auf einer eigenen Instanz, einer der Instanzen aus der Liste oben, und das Labyrinth ist eines von mehreren Layouts. Das Labyrinth füllt die ganze Karte, von Rand zu Rand: ein Raster aus Räumen und Gängen mit festen Wänden. Schiffe können eine Wand nicht durchqueren, und eine Wand blockt Schüsse, sie ist also Deckung. Ein Meteor fällt von oben, und eine Wand hält ihn nicht auf.

**Räume und Türen.** Der Startraum, in dem du landest, und der Raum des Kriegsherrn am fernen Ende haben je eine Tür. Eine geschlossene Tür ist für Schiffe, Schüsse und Aliens gleichermaßen eine Wand. Die Starttür öffnet sich, wenn der Dungeon startet. Die Tür des Kriegsherrn bleibt verschlossen, bis drei Viertel der Crystalys und ihrer Twins zerstört sind (siehe [Der verschlossene Raum](#the-locked-room)). Dazwischen hat das Labyrinth für jede Beutezone einen Beuteraum.

**Nebel.** Das Labyrinth ist dunkel. Im Flug siehst du seine Wände und seine Aliens nur dort, wo die Gruppe gewesen ist, und ein Stück um jedes Schiff der Gruppe herum. Ein Raum gilt als erkundet, sobald einer von euch darin ist. Die Minikarte funktioniert genauso: Sie ist eine Karte der ganzen Ebene, die sich füllt, während die Gruppe sie erkundet, mit dem Eingang, der Tür des Kriegsherrn, den Zonen, die ihr gefunden habt, und dem Kriegsherrn, sobald ihr ihn gefunden habt. Die Piloten deiner eigenen Gruppe werden immer angezeigt.

## Die Aliens {#the-aliens}

Vier Arten von Aliens bewachen das Labyrinth. Sie schlafen in Rudeln in den Gängen, nie in einem Raum, und ein Rudel wacht auf, wenn ein Pilot näher kommt. Ein wachendes Rudel wartet nicht auf dich: Es jagt die Gruppe durchs Labyrinth, und ein Rudel, das alle verliert, geht dorthin zurück, wo es geschlafen hat, und heilt sich. Ein paar Rudel sind von der ersten Sekunde an wach und stehen abseits des Eingangs in den Gängen, bis ein Pilot näher kommt. Der Dungeon hält nur eine bestimmte Zahl von Aliens gleichzeitig in der Luft, und diese Zahl wächst mit der Größe der Gruppe, sodass ein Rudel, das aufwacht, auf Platz warten muss und ein zerstörtes Rudel das nächste hereinlässt. Eine größere Gruppe trifft im selben Verhältnis auf mehr Aliens, eine kleinere auf weniger, und eine Alienart fällt nie unter eins. Ein Rudel, das noch auf Platz wartet, wenn alle Piloten weggeflogen sind, legt sich wieder schlafen und wacht auf, wenn ein Pilot näher kommt.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Aliens, für eine Gruppe von 5 | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Dungeon Goombah | 156 | 156 | 156 |
| Dungeon Pirate | 34 | 34 | 34 |
| Dungeon Crystalys | 34 | 34 | 34 |
| Dungeon Crystalys Twin | 11 | 11 | 11 |
| Zusammen | 235 | 235 | 235 |
| Zum Öffnen des Boss-Raums | 34 | 34 | 34 |
| Die Welle einer Beutezone | 12 × Dungeon Goombah und 1 × Dungeon Crystalys | 12 × Dungeon Goombah und 1 × Dungeon Crystalys | 12 × Dungeon Goombah und 1 × Dungeon Crystalys |

- **Gleichzeitig am Leben**: Höchstens 10 je Pilot der Gruppe und 70 insgesamt

<!-- dungeons-population:end -->

Die Arten der Reihe nach. Hülle und Schild sind die üblichen Werte mal dem Faktor der Stufe in der Spalte.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Dungeon Goombah

- **Sieht aus wie**: Goombah
- **Fliegt in Rudeln zu**: 6

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 32.000 | 48.000 | 64.000 |
| Schild | 48.000 | 72.000 | 96.000 |
| Laserschaden (eine Salve pro Sekunde) | 3.000 | 4.500 | 6.000 |
| Tempo | 180 | 180 | 180 |
| Laserreichweite | 800 | 800 | 800 |
| Aggro-Radius | 1.800 | 1.800 | 1.800 |

### Dungeon Pirate

- **Sieht aus wie**: Pirate Boss
- **Fliegt in Rudeln zu**: 2
- **Rakete**: Alle 5 s eine gerade Rakete, Reichweite 1.000 Einheiten

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 300.000 | 450.000 | 600.000 |
| Schild | 50.100 | 75.150 | 100.200 |
| Laserschaden (eine Salve pro Sekunde) | 200 | 300 | 400 |
| Raketenschaden | 5.000 | 7.500 | 10.000 |
| Tempo | 110 | 110 | 110 |
| Laserreichweite | 700 | 700 | 700 |
| Aggro-Radius | 1.800 | 1.800 | 1.800 |

### Dungeon Crystalys

- **Sieht aus wie**: Crystalys
- **Fliegt in Rudeln zu**: 2

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 256.000 | 384.000 | 512.000 |
| Schild | 160.000 | 240.000 | 320.000 |
| Laserschaden (eine Salve pro Sekunde) | 10.000 | 15.000 | 20.000 |
| Tempo | 230 | 230 | 230 |
| Laserreichweite | 900 | 900 | 900 |
| Aggro-Radius | 2.400 | 2.400 | 2.400 |

### Dungeon Crystalys Twin

- **Sieht aus wie**: Crystalys, 1,4-mal so groß
- **Fliegt in Rudeln zu**: 1

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 512.000 | 768.000 | 1.024.000 |
| Schild | 320.000 | 480.000 | 640.000 |
| Laserschaden (eine Salve pro Sekunde) | 20.000 | 30.000 | 40.000 |
| Tempo | 230 | 230 | 230 |
| Laserreichweite | 900 | 900 | 900 |
| Aggro-Radius | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## Der Kriegsherr {#the-warlord}

Der Kriegsherr wartet im Raum am fernen Ende des Labyrinths, und er ist das Einzige in einem Dungeon, der zahlt. Er ist ein riesig gewachsener Crystalys. Seine Hülle und sein Schild wachsen mit der Größe der Gruppe: Je mehr Piloten hineingehen, desto zäher ist er, im selben Verhältnis. Er verlässt seinen Raum nie, ob die Tür zu ist oder offen: Er bleibt innerhalb der Wände des Raums und jagt nicht durch die Gänge. Ein Pilot draußen kann ihn nur bis an den Rand des Raums locken, und durch eine offene Tür schießt er trotzdem auf alles, was sein Laser erreicht. Er setzt seine Fähigkeiten nacheinander in zufälliger Reihenfolge ein, jede mit eigener Abklingzeit.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Sieht aus wie**: Crystalys, 3-mal so groß
- **Schildaufladung**: 3.000 pro Sekunde, nach 15 s ohne Schaden

|  | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | ---: | ---: | ---: |
| Hülle | 10.000.000 | 15.000.000 | 25.000.000 |
| Schild | 8.000.000 | 12.000.000 | 20.000.000 |
| Laserschaden (eine Salve pro Sekunde) | 12.500–15.000 | 15.000–17.500 | 20.000–25.000 |
| Tempo | 120 | 120 | 120 |
| Laserreichweite | 1.100 | 1.100 | 1.100 |

Hülle und Schild oben gelten für eine Gruppe von 5. Sie wachsen mit der Gruppe: Das sind Hülle und Schild des Kriegsherrn zusammen, nach der Zahl der Piloten in der Gruppe beim Start des Dungeons.

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

### Der verschlossene Raum {#the-locked-room}

Die Tür zum Raum des Kriegsherrn ist ab dem Moment verschlossen, in dem der Dungeon geöffnet wird, und solange sie zu ist, kann der Kriegsherr nicht verletzt werden: Kein Laser, keine Rakete und keine Explosion trifft ihn, und er setzt keine Fähigkeit ein. Die Tür öffnet sich für immer, wenn **drei Viertel der Crystalys und ihrer Twins** zerstört sind, mit denen der Dungeon gebaut wurde, aufgerundet (die Tabelle der Aliens oben zählt sie für eine Gruppe von 5, und ihre letzte Zeile sagt, wie viele es braucht). Es zählen die Crystalys und die Twins in den Rudeln des Labyrinths, auch in den Rudeln, die von der ersten Sekunde an in den Gängen stehen, und gleich, wer sie zerstört. Die übrigen Aliens, die Wellen der Beutezonen, die Goombahs, die der Kriegsherr ruft, und der Kriegsherr selbst zählen für die Tür nicht.

Das Fenster Clan-Dungeon zählt, wie viele davon noch zerstört werden müssen, um den Raum zu öffnen, und sagt in einem kleinen Feld, dass der Kriegsherr nicht verletzt werden kann, und eine Meldung sagt dir, wann der Raum entsperrt ist. Ein Rudel, das noch schläft, zählt voll, also muss die Gruppe die Crystalys und ihre Twins im Labyrinth finden. **Die übrigen Aliens verschwinden nicht, wenn die Tür sich öffnet.** Sie bleiben im Labyrinth, wachen auf, wenn ein Pilot näher kommt, und können wie zuvor zerstört werden; eine Gruppe, die das will, kann also alle zerstören, bevor sie gegen den Kriegsherrn kämpft: Die Zahl der Aliens im Fenster läuft weiter bis zu allen Aliens, mit denen der Dungeon gebaut wurde, und steht auf voll, wenn keiner mehr übrig ist. Sie bringen nichts ein, und die, die noch leben, wenn der Kriegsherr fällt, verschwinden mit dem Dungeon. Auf der Minikarte ist die Tür eine rote Linie, solange sie verschlossen ist, und eine grüne, wenn sie offen ist. Ein Dungeon ist nie eine Falle: Das Zeitlimit beendet auch einen Dungeon, dessen Tür verschlossen bleibt, und ein Administrator kann den Raum eines festgefahrenen Dungeons entsperren.

### Seine Fähigkeiten {#its-abilities}

- **Der rote Ring** der Lebensraub-Aura verletzt jeden Piloten darin und heilt den Kriegsherrn mit dem Schaden. Auch die Schildabsorption hat einen roten Ring: Er entzieht den Schilden der Piloten darin Energie und lädt damit den des Kriegsherrn auf. Verlasse in beiden Fällen den Ring oder stell dich hinter eine Wand.
- **Die bernsteinfarbenen Ringe** des Meteoritenhagels zeigen, wo einen Moment später Meteore einschlagen. Bleib in Bewegung und verlasse den Ring, bevor er einschlägt.
- **Fokus auf den Meistgesuchten** markiert den Piloten, der dem Kriegsherrn den meisten Schaden zugefügt hat, mit einer goldenen Klammer an seinem Schiff, und der Kriegsherr feuert, solange es dauert, jede Sekunde einen zusätzlichen Schuss auf ihn. Sein Ziel ändert sich nicht: Er schießt weiter auf den nächsten Piloten, den er sehen kann, ein markierter Pilot, der auch der nächste ist, kassiert also beides. Der zusätzliche Schuss braucht freie Sicht und die Reichweite des Lasers des Kriegsherrn, eine Wand oder etwas Abstand rettet ihn also. Er startet nicht, solange noch niemand Schaden verursacht hat.
- **Die Raketensalve** schickt zielsuchende Raketen auf zufällige Piloten, aber nur auf Piloten, die der Kriegsherr sehen kann, und eine Wand im Weg stoppt eine Rakete. Ein Ring zeigt, welchem Piloten eine Rakete folgt. Eine EMP Charge oder eine Tarnung schüttelt sie ab.
- **Die Schwarm-Unterstützung** ist der Kriegsherr, der seine Goombahs ruft. Solange sie leben, kann er nicht verletzt werden, und er feuert nicht und setzt keine andere Fähigkeit ein. Zerstöre sie alle: Das Banner zählt, wie viele übrig sind. Vergeht eine Minute, kann der Kriegsherr wieder verletzt werden, und die übrigen Goombahs bleiben und kämpfen weiter. Sie zählen nicht für den Raum des Kriegsherrn, und sie zahlen nichts.
- **Die Zone des Chaos** ist ein violetter Ring auf dem Boden, um den Kriegsherrn herum, und solange sie andauert, geht er überallhin mit, wohin der Kriegsherr geht. Niemand im Ring kann angreifen, weder mit Lasern noch mit Raketen, doch Reparaturen, Tarnung und Fliegen funktionieren weiter, und der Kriegsherr und seine Aliens feuern wie immer. Der Ring zeigt sich einen Moment, bevor er wirkt: Tritt aus ihm heraus und bleib draußen, denn er folgt dem Kriegsherrn. Ein Pilot außerhalb kann weiter schießen, soweit seine Waffen reichen.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fähigkeit | Anlauf | Dauer | Abklingzeit | Ringradius (Einheiten) | Der Kriegsherr gewinnt höchstens zurück |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Lebensraub-Aura** | 2 s | 15 s | 2 min | 900 | 8 % seiner Hülle und seines Schilds |
| **Meteoritenhagel** | 1,5 s | 3 Salven, 4 s Abstand | 2 min | 420 | – |
| **Fokus auf den Meistgesuchten** | 1 s | 20 s | 2 min | – | – |
| **Raketensalve** | 1,5 s | 45 s | 2 min | – | – |
| **Schildabsorption** | 2 s | 15 s | 2 min | 900 | 6 % seines Schilds |
| **Schwarm-Unterstützung** | 2 s | Bis zu 1 min | 3 min | – | – |
| **Zone des Chaos** | 2 s | 15 s | 2 min | 900 | – |

| Fähigkeit | Stufe 1 | Stufe 2 | Stufe 3 |
| :--- | :--- | :--- | :--- |
| **Lebensraub-Aura** | 8.000 pro Sekunde | 10.000 pro Sekunde | 12.000 pro Sekunde |
| **Meteoritenhagel** | 6 Meteore pro Salve, je 40.000 | 8 Meteore pro Salve, je 50.000 | 10 Meteore pro Salve, je 60.000 |
| **Fokus auf den Meistgesuchten** | 18.750–22.500 pro Extraschuss auf den Piloten mit dem meisten Schaden, einer alle 1 s | 22.500–26.250 pro Extraschuss auf den Piloten mit dem meisten Schaden, einer alle 1 s | 30.000–37.500 pro Extraschuss auf den Piloten mit dem meisten Schaden, einer alle 1 s |
| **Raketensalve** | 26.000 pro Rakete, eine alle 15 s | 32.500 pro Rakete, eine alle 15 s | 39.000 pro Rakete, eine alle 15 s |
| **Schildabsorption** | 10.000 Schild pro Sekunde | 12.500 Schild pro Sekunde | 15.000 Schild pro Sekunde |
| **Schwarm-Unterstützung** | 12 Goombahs | 18 Goombahs | 24 Goombahs |
| **Zone des Chaos** | Piloten im Ring können nicht angreifen | Piloten im Ring können nicht angreifen | Piloten im Ring können nicht angreifen |

<!-- dungeons-abilities:end -->

## Beutezonen {#loot-zones}

Ein Ring auf dem Boden des Labyrinths markiert jede Beutezone, sobald die Gruppe sie gefunden hat. Bleibe kurz darin stehen, und die Zone erwacht, und eine Welle Aliens kommt auf sie zu. Dann muss die Gruppe die Zone **halten**: einen Piloten darin lassen, bis der Balken voll ist. Je mehr Piloten im Ring stehen, desto schneller füllt sich der Balken: Eine Zahl neben dem Balken sagt, wie viel schneller, und die Tabelle unten gibt die Zeiten an. Genug Aliens im Ring halten den Balken an (die Liste unten sagt, wie viele), und er läuft zurück, solange niemand darin ist, räumt also zuerst die Welle. Wenn sich die Zone öffnet, sieht die Gruppe drei verschiedene Karten und **stimmt** über eine ab. Eine Zone öffnet sich nur einmal, und ihre Welle kommt nicht wieder.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Beutezonen**: 6 in jedem Labyrinth
- **Radius**: 450 Einheiten
- **Wecken**: 2 s lang im Ring stehen
- **Halten**: Einen Piloten 30 s lang im Ring halten. Das Halten stoppt, solange 3 oder mehr Aliens im Ring sind, und läuft zurück, solange niemand darin ist
- **Wählen**: Die Gruppe hat 45 s zum Abstimmen. Die Abstimmung endet früher, wenn jeder anwesende Pilot gewählt hat oder eine Karte mehr als die Hälfte der Stimmen hat

Mehr Piloten im Ring halten eine Zone schneller. So lange dauert es, eine Zone zu halten:

| Piloten im Ring | Zeit zum Halten der Zone |
| :--- | ---: |
| 1 | 30 s |
| 2 | 20 s |
| 3 | 15 s |
| 4 | 12 s |
| 5 oder mehr | 10 s |

<!-- dungeons-zones:end -->

### Booster {#boosters}

In den Stufen 2 und 3 verdient sich die Gruppe Booster, indem sie die Aliens des Dungeons zerstört. Bei jedem Zehntel von ihnen fällt ein Booster: wenn ein Zehntel der Aliens zerstört ist, dann zwei Zehntel und so weiter bis zu allen, zehn Drops insgesamt. Es zählt jedes Alien, mit dem der Dungeon gebaut wurde, gleich, wer es zerstört (es ist die Zählung der zerstörten Aliens im Fenster Clan-Dungeon); die Wellen der Beutezonen und die Aliens, die der Kriegsherr ruft, zählen nicht, eine Zone bringt also keinen Booster. Bei jedem Drop bekommt jeder Pilot ein Fenster von einer halben Minute, um sich einen zeitweiligen Booster auszusuchen, und zwar aus drei, die das Spiel zufällig aus fünf zieht: **Schaden** (deine Laser treffen härter), **Trefferpunkte** (dein Schiff hält mehr Hülle aus), **Schild** (dein Schild hält mehr aus), **Tempo** (dein Schiff fliegt schneller) und **Schildaufladung** (dein Schild lädt sich schneller auf). Drücke auf eine Karte, um sie zu wählen. Antwortest du nicht rechtzeitig, wählt das Spiel Trefferpunkte für dich, oder die erste der drei, wenn Trefferpunkte nicht darunter sind. Eine Wahl ist in Stufe 3 3 % wert und in Stufe 2 1,5 %, zehn Wahlen summieren sich also in Stufe 3 auf höchstens dreißig Prozent und in Stufe 2 auf fünfzehn Prozent, welche Arten es auch sind. Stufe 1 hat keine Booster.

Der zehnte Drop kommt mit dem letzten Alien. Eine Gruppe, die jedes Alien zerstört, bevor sie gegen den Kriegsherrn kämpft, bekommt alle zehn Drops; eine Gruppe, die den Raum des Kriegsherrn öffnet und weiterfliegt, bekommt die Drops der Aliens, die sie bis dahin zerstört hat, und die übrigen Aliens bleiben und können weiter zerstört werden. Hat der Kampf gegen den Kriegsherrn begonnen, fällt kein Booster mehr.

Ein Booster hält, bis der Dungeon geschafft ist. Verlässt du den Dungeon oder wirst du zerstört, verlierst du deine Booster, und du bekommst sie zurück, wenn du wieder hineinfliegst. Ein kleines Feld unter dem Fenster Clan-Dungeon zeigt, was du hast.

### Die Karten {#the-cards}

Die Karten werden eine nach der anderen aus dem Pool unten gezogen. Die Chance ist die einer Karte bei einem Zug. Jede Karte geht an jeden bezahlten Piloten, auch die Ausrüstungskarten: Eine Karte mit vielen Exemplaren gibt jedem so viele, eine Ausrüstungskarte gibt jedem ein eigenes, für ihn geschmiedetes Stück. Ein Pilot, der nicht bezahlt wird, bekommt auch keine Karte, und eine Zone, die in einem gescheiterten Dungeon geöffnet wurde, zahlt nichts.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Karte | Stufe 1 | Stufe 2 | Stufe 3 | Chance | Geht an |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | 23,9 % | Jeden bezahlten Piloten |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13,65 % | Jeden bezahlten Piloten |
| Velkonite | 200 | 300 | 500 | 13,65 % | Jeden bezahlten Piloten |
| Orvium | 200 | 300 | 500 | 13,65 % | Jeden bezahlten Piloten |
| Ultra Core | 5.000 | 7.500 | 12.500 | 11,4 % | Jeden bezahlten Piloten |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 9,1 % | Jeden bezahlten Piloten |
| Dark Matter | 10 | 16 | 24 | 9,1 % | Jeden bezahlten Piloten |
| Dark Matter Plate | 1 | 1 | 2 | 4,55 % | Jeden bezahlten Piloten |
| Starfire-III | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Helios Beam | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Engine III | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Adaptive Core III | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Heavy Shield Core | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Momentum Thruster IV | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Impulse Thruster IV | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Hull Plating II | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Hull Plating III | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Damage Amp IV | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Crit Amp IV | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Penetration Amp IV | – | – | 1 | 0,07 % | Jeden bezahlten Piloten |
| Capacity Shield Cell IV | – | – | 1 | 0,08 % | Jeden bezahlten Piloten |
| Absorption Shield Cell IV | – | – | 1 | 0,08 % | Jeden bezahlten Piloten |

- **Ausrüstung**: Die Karten mit einem Exemplar sind Ausrüstung: zusammen 1 % der Karten

<!-- dungeons-cards:end -->

Die Karten mit einem Exemplar sind **Ausrüstung**, und nur ein Dungeon der Stufe 3 kann sie anbieten. Ein Ausrüstungsteil wird für jeden bezahlten Piloten bei der Auszahlung geschmiedet: Jeder würfelt eine eigene [Verzauberungsstufe](/wiki/06-Items/Overview.md#item-enchants) mit denselben Chancen wie ein Teil, das du in der Montage baust, die meisten sind also Standard, und eine höhere Stufe, bis zu Ewig, mit Buffs, ist ein seltener Fund.

## Belohnung {#pay}

Wenn der Kriegsherr fällt, wird jeder Pilot, der es verdient hat, einmal für den Durchgang bezahlt. Die Karten, die die Gruppe gewählt hat, kommen zur Belohnung der Stufe hinzu. Es gibt keinen Weltfaktor: Die Belohnung ist in jeder Welt gleich.

Die **Orvium Reinforced Plates** sind keine Karte der Abstimmung. Sie gehören zur Belohnung der Stufe, und jeder bezahlte Pilot bekommt sie einmal für den Durchgang. Die Gegenstände, die ein Dungeon auszahlt, sind nicht Handelbar: Du kannst sie nicht [in der Auktion verkaufen](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Stufe | Ehre | Erfahrung | Credits | Thulium | x4-Munition | Orvium Reinforced Plates | PvE-Rangpunkte |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Stufe 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 5 | 600 |
| **Stufe 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 10 | 1.500 |
| **Stufe 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 15 | 2.400 |

<!-- dungeons-pay:end -->

### Wer bezahlt wird {#who-is-paid}

Die Aliens zahlen nie. Ein Durchgang wird auch dann vollständig gespielt, wenn er nichts zahlt, und der Ergebnisbildschirm sagt, warum. Der Zutritt wird nie verweigert, weil du für eine Stufe schon bezahlt wurdest: Dieser Durchgang zahlt dann nur nichts.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Ein Tag**: Eine Stufe zahlt einem Piloten einmal pro UTC-Tag: an dem Tag, an dem der Kriegsherr fällt
- **Eine Woche**: Ein Pilot wird für höchstens 10 Stufen-Abschlüsse pro UTC-Woche bezahlt, Montag bis Sonntag
- **Im Dungeon**: Mindestens 2 min insgesamt
- **Anteil am Kampf**: Mindestens eines davon: Schaden in Höhe von 2 % der Hülle und des Schilds des Kriegsherrn verursacht; 10 Aliens des Dungeons zerstört; andere Piloten im Kampf gegen den Kriegsherrn um 50.000 geheilt

<!-- dungeons-rules:end -->

### Was ein Tag und eine Woche wert sind {#what-a-day-and-a-week-are-worth}

Was ein Pilot an einem Tag und in der besten Woche bekommen kann, die die Grenzen erlauben. Die letzte Spalte zeigt, was die Belohnung deinen [PvE-Punkten](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) hinzufügt.

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Belohnung je Pilot | Ehre | Erfahrung | Credits | Thulium | x4-Munition | Orvium Reinforced Plates | PvE-Rangpunkte |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Ein Tag, jede Stufe einmal | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 30 | 4.500 |
| Die beste Woche: 7 × Stufe 3 und 3 × Stufe 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 135 | 21.300 |

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
- **Bezahlte Piloten**: Mindestens 3 im Dungeon

<!-- dungeons-clan:end -->

## Tipps {#tips}

- Räume die Welle einer Zone, bevor du versuchst, sie zu halten, und kämpfe im Ring, wenn Aliens hereinkommen.
- Bring die ganze Gruppe zu einer Zone: Je mehr Piloten im Ring stehen, desto schneller wird sie gehalten.
- Suche im Labyrinth die Crystalys und ihre Twins: Die Tür des Kriegsherrn öffnet sich, wenn drei Viertel von ihnen tot sind, und nicht früher. Die übrigen Aliens können warten oder auch zerstört werden.
- Nutze die Wände: Laser durchqueren sie nicht, die roten Ringe der Auren des Kriegsherrn enden an ihnen, und eine Wand stoppt auch die Raketen des Kriegsherrn.
- Spare eine EMP Charge für die Raketensalve auf.
- Ruft der Kriegsherr seine Goombahs, zerstöre sie zuerst: Er kann nicht verletzt werden, bis sie weg sind. Tritt in der Zone des Chaos aus dem Ring, bevor du schießt.
- Behalte die Uhr im Fenster Clan-Dungeon im Blick. Läuft die Zeit ab, scheitert der Dungeon und zahlt nichts.
