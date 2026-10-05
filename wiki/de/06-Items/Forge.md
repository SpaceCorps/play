<!-- wiki-i18n source: e3d36c8d68eda434 -->
<!-- wiki-i18n title: Schmiede -->
# Die Schmiede {#the-forge}

Die **Schmiede** ist der zweite Tab der Montage-Seite (und des Montage-Fensters im Flug). Sie tut zwei Dinge mit Ausrüstung, die du besitzt: Sie **hebt einen Gegenstand um eine Stufe an**, gegen Credits und Alien-Beute, und sie **führt zwei Exemplare** eines Gegenstands **zusammen**, zu einem, der das Beste aus beiden behält. Sie hat die alte Fusionskammer ersetzt, die fünf identische Gegenstände brauchte und das Ergebnis einem Wurf mit 25 % Chance überließ.

## Was sich schmieden lässt {#what-can-be-forged}

Laser, Laserverstärker, Schilde, Schildzellen, Triebwerke, Schubdüsen, adaptive Kerne und Repair Drones: jedes einzelne Ausrüstungsstück, das [Verzauberungsboni](/wiki/06-Items/Overview.md) tragen kann. Es kann in deinem Inventar liegen, auf einem Schiff (es bleibt dort und wirkt sofort mit seiner neuen Stufe) oder in einen anderen Gegenstand eingesetzt sein. Drohnen, Schiffe, Munition, Ressourcen und Booster lassen sich nicht schmieden, ebenso wenig alles im Transport-Cache: Nimm es zuerst heraus.

## Aufwerten {#tier-up}

Wähle einen Gegenstand, und das Panel zeigt seine Stufe, die Stufe, die er erreichen würde, was sich dadurch ändert (wie viele Boni er fassen kann und wie groß sie sind) und den Preis mit dem, was du von jedem Teil hast: grün, wenn du genug hast, rot, wenn nicht, und wie viele dir fehlen. Wenn du alles hast, hebt **Aufwerten** den Gegenstand um genau eine Stufe an. Es gibt keinen Sprung: Um Ewig zu erreichen, durchläuft ein Gegenstand Verdorben, Göttlich und Berstend, jede mit eigenem Preis.

| Schritt | Erfolg | Credits | Thulium | Materialien |
| :--- | :---: | :---: | :---: | :--- |
| Standard zu Verdorben | 100 % | 10.000 | – | 5 Ship Fragment, 15 Daraxium |
| Verdorben zu Göttlich | 90 % | 50.000 | – | 30 Ship Fragment, 45 Nyxite |
| Göttlich zu Berstend | 75 % | 200.000 | – | 20 Reinforced Hull Plate, 120 Cataclysite, 2 Dark Matter Plate |
| Berstend zu Ewig | 60 % | 500.000 | 2.000 | 8 Power Core, 240 Quorvium, 2 Dark Matter Plate |

- **Materialien** kommen aus deinen losen Stapeln: Gegenstände auf einem Schiff und Stapel im Transport-Cache werden nicht verwendet. Das Panel sagt dir, wenn die fehlenden im Cache liegen.
- **Ein Schritt kann misslingen.** Der Gegenstand bleibt genau, wie er war, die Credits sind weg, und die Hälfte der Materialien und die Hälfte des Thulium kommen zurück (abgerundet; von zwei Dark Matter Plates eine). Das Panel nennt dir die Chance und dies, bevor du drückst.
- **Bei Erfolg** wird jeder Bonus, den der Gegenstand hat, im Bereich der neuen Stufe neu ausgewürfelt und behält den besseren Wert. Hat der Gegenstand noch keinen Bonus, bekommt er immer seinen ersten; jeder andere Platz, den die neue Stufe öffnet, wird mit einer **Chance von 50 %, jeweils mit eigenem Wurf**, mit einem neuen Bonus auf einem anderen Wert des Gegenstands gefüllt, und ein Platz, der leer bleibt, kann bei einer späteren Aufwertung gefüllt werden (siehe [Boni nach Stufe](#buffs-by-tier)). Das Ergebnis erscheint über dem Panel; der Gegenstand bleibt ausgewählt, sein nächster Schritt steht also schon auf dem Bildschirm.
- Ein Aufwerten geschieht sofort.

### Dark Matter Plates

Die letzten beiden Schritte verlangen jeweils **2 Dark Matter Plates**, zusätzlich zu allem anderen. Eine Platte wird in der [Montage](/wiki/06-Items/Overview.md) aus **5 Dark Matter, 1 Velkonite Reinforced Plate und 1 Orvium Reinforced Plate** gepresst (250 Thulium, 2 Minuten), ein Schritt braucht also 10 Dark Matter, 2 Velkonite-Platten und 2 Orvium-Platten. Dark Matter stammt aus dem [Schwarzen Loch](/wiki/03-Mechanics/Black-Hole.md): Etwa fünf N.I.K.E.-Raketen (siehe [Raketen](/wiki/06-Items/Rockets.md)) ergeben zehn; eine N.I.K.E., die unterwegs auf ein Schiff trifft, trifft stattdessen dieses Schiff und ergibt nichts. Die Platten werden wie die anderen Materialien aus deinen losen Stapeln genommen, und das Panel nennt sie, wenn sie dir fehlen.

### Boni nach Stufe {#buffs-by-tier}

| Stufe | Höchstens gehaltene Boni | Größe jedes Bonus |
| :--- | :---: | :---: |
| Verdorben | 1 | +2 % bis +5 % |
| Göttlich | 2 | +4 % bis +8 % |
| Berstend | 3 | +6 % bis +11 % |
| Ewig | 4 | +9 % bis +15 % |

Ausrüstung, die vor der Schmiede hergestellt wurde, behält die Boni, mit denen sie ausgewürfelt wurde, und die sind oft kleiner als in der Tabelle (ein göttliches Stück von damals kann +2 % fassen). Nichts hebt sie von selbst an: Ein Aufwerten würfelt jeden Bonus im Bereich der neuen Stufe neu aus und behält den besseren Wert, und beim Zusammenführen bleibt für jeden Wert der bessere Bonus.

Ein Gegenstand kann nicht mehr Boni fassen, als er Werte hat: Ein Schild hat vier, ein Laser drei (Quantum Laser 1 und 2 haben zwei), ein Triebwerk oder ein adaptiver Kern zwei, ein Momentum Thruster zwei, ein Impulse Thruster einen (sein Faktor von 1,02 oder 1,03 ist zu klein für einen Bonus, und die Schmiede würfelt keinen auf einen Faktor von 1,05 oder weniger, sein Bonus kann also nur auf dem festen Tempo liegen), ein Crit Amp 1 oder eine Repair Drone einen, die höheren Krit-Verstärker zwei, die Schadensverstärker und Schildzellen drei. Wenn die nächste Stufe nicht mehr Boni fasst, als der Gegenstand tragen kann, sagt das Panel es: Die Stufe macht die Boni dann nur stärker. Reichweiten-Boni gehen nie über +5 % hinaus.

**Eine Stufe fasst höchstens so viele Boni.** Eine Aufwertung gibt einem Gegenstand immer seinen ersten Bonus; jeder andere Platz, den die neue Stufe öffnet und für den der Gegenstand einen Wert hat, wird mit einer **Chance von 50 %, jeweils mit eigenem Wurf**, gefüllt, und ein Platz, der leer bleibt, wird von der nächsten Aufwertung erneut versucht. Ein göttlicher Schild hat also zur Hälfte zwei Boni und zur anderen Hälfte einen; ein ewiger hat in etwa einem Drittel der Fälle alle vier (im Schnitt 3,1 Boni), ein Laser mit drei Werten hat alle drei in zwei von drei Fällen, und ein Triebwerk hat fast immer beide. Das Panel sagt für die nächste Stufe „bis zu“ und nennt, wie oft sich ein neuer Platz füllt. Gegenstände mit nur einem Wert und jeder Schritt zu Verdorben sind nicht betroffen, und Ausrüstung, die vor dieser Regel entstanden ist, behält ihre Boni. Ein **Zusammenführen** füllt einen Platz, den eine Aufwertung verpasst hat: Es behält den besten Bonus jedes Werts von zwei Exemplaren, bis zur Grenze der Stufe. Wegen der Chance trägt ein Stück den gleich beschriebenen Absorptionsbonus nur zum Teil (ein ewiger Schild zu 78 %, eine ewige Schildzelle zu 88 %): Die Zahlen dort gelten für Stücke, die ihn tragen.

Der **Absorptionsbonus eines Schilds** (und der Absorptions-Boost einer Schildzelle) multipliziert den Wert, ist also im Verhältnis dazu Punkte der [Absorption](/wiki/03-Mechanics/Shields.md#2-shield-absorbance-damage-split-) wert: +5 % auf die 50 % eines Heavy Shield Core sind +2,5 Punkte, und +15 % auf jedes Teil des besten Sets (ein Heavy Shield Core und drei Absorption Shield Cell IV, insgesamt 80 %) sind +12 Punkte. Ein ewiges Set bringt zwischen +7 und +12 Punkte, im Durchschnitt etwa 10; mit dem Schildabsorptions-Boost des Saison-Shops (+10 Punkte am Limit; die Wipe-Punkte des gesamten Spiels kaufen 34 seiner 100 Level, +3,4 Punkte) bringt das ein Schiff auf 95 %, und über 100 % nur mit dem Limit des Buffs, was der Wert zulässt: Die Schilddurchdringung eines Angreifers wird davon abgezogen. Ein göttliches Set bringt zwischen 3 und 6 Punkte.

Triebwerke, Schubdüsen, adaptive Kerne und Repair Drones bewegen mit einem prozentualen Bonus sehr wenig (ein Engine II gibt 4 Tempo, also sind +12 % ein halber Punkt): Schmiede sie, wenn du die Stufe willst, nicht wegen der Werte.

### Woher die Materialien kommen {#where-the-materials-drop}

| Material | Beute von |
| :--- | :--- |
| **Ship Fragment** | jedem Alien |
| **Daraxium** | [Seeker](/wiki/04-Aliens/Seeker.md), [Phantasm](/wiki/04-Aliens/Phantasm.md) |
| **Nyxite** | [Phantasm](/wiki/04-Aliens/Phantasm.md), [Bulwark](/wiki/04-Aliens/Bulwark.md) |
| **Reinforced Hull Plate** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md) |
| **Cataclysite** | [Bulwark](/wiki/04-Aliens/Bulwark.md), [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Power Core** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Quorvium** | [Goombah](/wiki/04-Aliens/Goombah.md), [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| **Dark Matter Plate** | keinem Alien: Die Montage presst sie aus Dark Matter (dem [Schwarzen Loch](/wiki/03-Mechanics/Black-Hole.md)) und den Platten des Skylab |

Die Kristalle folgen den Stufen: Daraxium ist blau wie Verdorben, Nyxite gelb wie Göttlich, Cataclysite orange wie Berstend und Quorvium violett wie Ewig. Jede Quelle mit den Chancen und Mengen steht auf der Seite [Ressourcen](/wiki/06-Items/Resources.md) und auf der Seite jedes Aliens; der Booster Resource Magnet erhöht den Inhalt einer Kiste um 25 %.

## Zusammenführen {#merge}

Zwei Exemplare desselben Gegenstands (zwei Light Shield Cores, zwei Quantum Laser 2) werden zu einem. Wechsle zu **Zusammenführen** und klicke den Gegenstand an, den du behalten willst (die **Basis**), dann ein zweites Exemplar (den **Spender**). Das Panel zeigt das Ergebnis, bevor du bestätigst.

- **Die Basis bleibt erhalten.** Sie behält ihren Platz: Sie kann auf einem Schiff liegen oder in einen anderen Gegenstand eingesetzt sein, und die in sie eingesetzten Module bleiben. **Der Spender wird verbraucht.** Er muss lose sein (nicht auf einem Schiff, nicht eingesetzt), und die in ihn eingesetzten Module gehen zurück in dein Inventar.
- **Das Ergebnis hat die höhere der beiden Stufen** und für jeden Wert den **besseren der beiden Werte**.
- **Es fasst nie mehr Boni, als seine Stufe erlaubt.** Haben die beiden Gegenstände zusammen mehr Boni, als die Stufe des Ergebnisses fassen kann, bleiben die besten erhalten und der Rest wird verworfen; die Tabelle markiert sie (durchgestrichen, „über dem Limit“). Um mehr Boni zu fassen, werte den Gegenstand zuerst auf. Ein Zusammenführen würfelt nie etwas aus: Was die Vorschau zeigt, bekommst du.
- **Ein Zusammenführen kostet Credits je nach der Stufe, die es ergibt**: 5.000 für Verdorben, 25.000 für Göttlich, 100.000 für Berstend, 250.000 für Ewig. Keine Materialien.
- Ein Zusammenführen, das nichts ändern würde (das Ergebnis ist nicht besser als die Basis), wird abgelehnt.
- Nach einem Zusammenführen bleibt das Ergebnis ausgewählt und der Spender-Platz ist leer: Lege den nächsten Spender ein oder wechsle zurück zu Aufwerten.

Ein Zusammenführen vervielfacht einen Gegenstand nicht, füllt aber die Plätze, die eine Aufwertung verpasst hat: Zwei zusammengeführte göttliche Schilde sind im Schnitt etwa dreieinhalb Punkte an Boni mehr wert als einer. Sein Nutzen liegt im Auswählen: ein göttlicher Kern mit den Werten, die du willst, oder eine Stufe, die auf den Gegenstand auf deinem Schiff übertragen wird, ohne dass du ihn ablegen musst.

## Modul-Upgrades in der Montage {#module-upgrades-in-the-assembly}

Die beiden obersten Laser, die obersten Laserverstärker, die Schildzellen und Schubdüsen der Stufen II bis IV, der Heavy Shield Core und das Engine III werden nicht verkauft, und die Montage stellt jedes erst her, wenn du seine Technologie im Skylab erforscht hast ([Forschung](/wiki/03-Mechanics/Research.md)). Du stellst sie im Tab **Herstellung** der Montage her, indem du das Stück eine Stufe darunter aufrüstest: einen Pulse Amp zu einem **Nova Amp**, einen Prism Amp zu einem **Apex Amp**, eine Capacity Shield Cell I zu einer **Capacity Shield Cell II** (und weiter zu III und IV; die Absorption Shield Cells, die Impulse Thrusters und die Momentum Thrusters steigen genauso auf), einen Basic Shield Core zu einem **Heavy Shield Core**, ein Engine II zu einem **Engine III**, einen Quantum Laser 3 zu einem **Starfire-3** und einen Starfire-3 zu einem **Helios Beam**. Was die Schmiede damit zu tun hat, ist die Stufe.

- **Die Stufe bleibt.** Ein Upgrade verbraucht ein Exemplar des Stücks, und der neue Gegenstand hat die Stufe dieses Exemplars: Ein Pulse Amp (Göttlich) ergibt einen Nova Amp (Göttlich), ein Pulse Amp (Standard) einen Nova Amp (Standard). Was du der Schmiede bezahlt hast, geht nicht verloren. Das Upgrade fügt keine eigene Stufe hinzu, ein Standard-Stück ergibt also immer ein Standard-Ergebnis.
- **Die Boni werden neu ausgewürfelt.** Der neue Gegenstand bekommt frische Boni für seine Stufe: so viele, wie das verbrauchte Stück hatte (ein Pulse Amp (Göttlich) mit zwei Boni ergibt einen Nova Amp (Göttlich) mit zwei, einer mit einem einzigen Bonus einen mit einem einzigen; über Standard mindestens einen), höchstens so viele, wie die Stufe fasst und der neue Gegenstand Werte dafür hat, jeden im Bereich der Stufe aus der Tabelle oben, auf Werten, die der Nova Amp hat. Sonst wird nichts vom alten Stück übernommen, die neuen Boni können also besser oder schlechter sein als die, die es hatte; im Durchschnitt sind sie gleich. Die Zahl bleibt erhalten, damit ein Upgrade die Plätze nicht füllen kann, die die Schmiede verpasst hat, und sie nimmt nie einen weg: Ein Stück aus der Zeit vor dieser Regel mit allen Plätzen gefüllt behält alle. Die Boni werden in dem Moment ausgewürfelt, in dem du den Auftrag einreihst, und was du abholst, ist, was ausgewürfelt wurde: Mit dem Abholen zu warten ändert nichts. Der Grund ist, dass das Upgrade einen neuen Gegenstand baut und die Würfel der Schmiede auf den Gegenstand fallen, den du besitzt. Die Stufe ist der Teil, der kostet: Ein ewiges Stück sind über eine Million Credits an Schmiedeschritten, ein Bonus dagegen nur ein paar Prozent eines Werts.
- **Platten.** Neben Thulium und dem, was die Aliens fallen lassen, verlangt jedes Modul-Upgrade **Velkonite Reinforced Plates**: 3 für einen Verstärker, 2, 4 oder 6 für eine Zelle oder eine Schubdüse der Stufe II, III oder IV, 6 für einen Heavy Shield Core oder ein Engine III und 8 für einen Starfire-3 (der Helios Beam verlangt stattdessen Orvium Reinforced Plates, 18 davon). Aliens lassen sie nicht fallen. Die [Skylab](/wiki/03-Mechanics/Skylab.md)-Schmiede stellt sie aus Velkonite-Erz her, 40 Erz pro Platte auf Schmiede-Level 1. Ein Velkonite-Kollektor auf Level 1 baut 10 Erz pro Stunde ab, die Platten eines Verstärkers sind also 12 Stunden Abbau und die einer Zelle oder Schubdüse der Stufe IV 24 (7 und 13 Stunden von einem Kollektor auf Level 5). Woher jedes Material kommt, steht auf der Seite [Ressourcen](/wiki/06-Items/Resources.md). Die eigenen Schritte der Schmiede verlangen Beute und Credits, und ihre obersten Schritte verlangen auch Platten (Göttlich zu Berstend: 20 Reinforced Hull Plates und 2 Dark Matter Plates; Berstend zu Ewig: 2 Dark Matter Plates), was etwas anderes ist als die Velkonite- und Orvium-Platten der Modul-Upgrades.
- **Welches Exemplar verwendet wird.** Du entscheidest. Besitzt du Exemplare, die sich unterscheiden (andere Stufe oder andere Boni), zeigt die Rezeptkarte sie als Reihe von Kacheln: Klicke das an, das verwendet werden soll, und die Zeile unter den Kacheln zeigt, was daraus wird („Pulse Amp (Göttlich)“, dann „Ergebnis: Nova Amp (Göttlich)“). Wählst du keines, geht das schlichteste: zuerst die niedrigste Stufe, und unter Exemplaren einer Stufe das älteste, egal welche Boni sie haben. Ein Exemplar der Stufe Göttlich oder höher wird nie verwendet, solange ein schlichteres lose liegt. Ein Exemplar über Standard zu verwenden, fragt vorher nach und nennt den Gegenstand.
- **Welche Exemplare verwendet werden können.** Lose: Ein Exemplar auf einem Schiff (auch in einem Fähigkeits-Slot), in einen anderen Gegenstand eingesetzt, mit eigenen Zellen oder Schubdüsen darin oder im [Transport-Cache](/wiki/03-Mechanics/Cargo.md) kann nicht verwendet werden, und die Montage sagt es dir. Lege es zuerst ab oder nimm es aus dem Cache. Zwei gleichzeitig gestartete Upgrades können nicht dasselbe Exemplar verwenden.

- **Der Starfire-3 ist auch ein Upgrade.** Er wird aus einem **Quantum Laser 3** hergestellt (mit 1.500 Thulium, 100.000 Credits, Beute und 8 Velkonite Reinforced Plates: siehe [Laser](/wiki/06-Items/Lasers.md)), und alles oben gilt: Ein Quantum Laser 3 (Göttlich) ergibt einen Starfire-3 (Göttlich) mit neuen Boni, du wählst das Exemplar, die Karte fragt nach, bevor sie eines über Standard verwendet, und der Quantum Laser 3 muss lose sein: Lege ihn zuerst im Hangar ab, und die Schaltfläche „Herstellen“ sagt „Quantum Laser 3 zuerst ausbauen“, bis du es tust. Die Stufe geht dann weiter nach oben: Ein Starfire-3 (Göttlich) ergibt einen Helios Beam (Göttlich).

- **Der Helios Beam ist auch ein Upgrade.** Er wird aus einem **Starfire-3** hergestellt (mit 2.000 Thulium, Beute und 18 Orvium Reinforced Plates: siehe [Laser](/wiki/06-Items/Lasers.md)), und alles oben gilt: Ein Starfire-3 (Göttlich) ergibt einen Helios Beam (Göttlich) mit neuen Boni (so vielen, wie der Starfire-3 hatte, höchstens zwei seiner drei Werte), du wählst das Exemplar, die Karte fragt nach, bevor sie eines über Standard verwendet, und der Starfire-3 muss lose sein. Ein Laser ist auf einem Schiff ausgerüstet und trägt Verstärker, ist es also oft nicht: Lege ihn zuerst im Hangar ab (seine Verstärker gehen zurück in dein Inventar), und die Schaltfläche „Herstellen“ sagt „Starfire-3 zuerst ausbauen“, bis du es tust.

Die Rezepte, ihre Kosten und die Zahlen hinter der Regel stehen in der [Gegenstandsübersicht](/wiki/06-Items/Overview.md#upgrading-modules) und, für den Starfire-3 und den Helios Beam, auf der Seite [Laser](/wiki/06-Items/Lasers.md).

## Alte Server {#old-servers}

Ein Spielserver, der noch nicht auf die Schmiede aktualisiert wurde, zeigt anstelle des Tabs „Die Schmiede ist auf diesem Server noch nicht verfügbar“; die Herstellung funktioniert wie bisher. Ein Spielclient von vor der Schmiede zeigt auf einem aktualisierten Server den alten Fusions-Tab und wird zum Aktualisieren aufgefordert.
