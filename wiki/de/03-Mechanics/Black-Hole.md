<!-- wiki-i18n source: 7f0874c517580c9b -->
<!-- wiki-i18n title: Schwarzes Loch -->
# Das Schwarze Loch {#the-black-hole}

<!-- wiki-search: black hole -->

Genau in der Mitte von Gefahrensektor 4 (`DS-4`, dem Zentrum der PvP-Zone) hängt ein Schwarzes Loch im Dunkel. Es ist in jeder Welt (Alpha, Beta und Gamma) dasselbe, an jedem Tag der Saison, auch während des Friedensprotokolls. Es nimmt sich, was ihm zu nahe kommt, und gibt nur eines zurück: [Dark Matter](#dark-matter), für eine N.I.K.E.-Rakete, die hineingeschossen wird. Den ganzen Weg, von der Forschung bis zur Plate, beschreibt [Dark Matter und Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md).

![A Wraith approaches the black hole from 3,500 units: the radiation and pull rings lie around it like a gravity well](../../img/wiki-img/shots/black-hole-approach.jpg)
![Looking down on the black hole from 1,300 units: the shadow, the photon ring and the spiral of the accretion disk, with the starfield bent around it](../../img/wiki-img/shots/black-hole-closeup.jpg)

## Die Ringe {#the-rings}

Die Entfernungen gelten ab der Mitte des Sektors, in Karteneinheiten. Der Sektor misst 32.000 mal 18.000 Einheiten.

| Ring | Entfernung | Was passiert |
| :--- | ---: | :--- |
| **Strahlung** | 4.000 | Dein Schiff nimmt jede Sekunde Schaden, einen Anteil seiner gesamten maximalen HP. Je näher, desto mehr. |
| **Sog** | 3.000 | Das Schwarze Loch zieht dein Schiff zur Mitte, umso stärker, je näher du bist. Ein Schiff, das nicht fliegt, wird mitgetragen. |
| **Punkt ohne Wiederkehr** | etwa 1.000 bis 2.600 | Dort, wo der Sog dem Tempo deines Schiffs entspricht. Innerhalb davon wirst du selbst mit voller Kraft hineingezogen. Er hängt von deinem Tempo ab. |
| **Ereignishorizont** | 300 | Jedes Schiff, das ihn erreicht, wird sofort zerstört, egal wie stark Hülle und Schild sind. |

Die Portale von Gefahrensektor 4 und die Bahnen zwischen ihnen verlaufen alle weit außerhalb der Strahlung, sodass du ihr auf der Durchreise nie zufällig begegnest. Ab Saisontag 11 liegt im selben Sektor außerdem der [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), in seiner oberen linken Ecke, weit vom Loch entfernt; die Aliens dort kommen nie in die Ringe des Lochs.

## Strahlung {#radiation}

Der Schaden ist ein **Prozentsatz der gesamten maximalen HP deines Schiffs** (Hülle plus Schild) pro Sekunde, daher hält jede Schiffsklasse in einer bestimmten Entfernung genau gleich lange durch: Bei 2.000 Einheiten brennt die Strahlung eine volle Protos ebenso wie eine volle Wraith in 50 Sekunden herunter.

| Entfernung | Schaden pro Sekunde | Ein volles Schiff hält |
| ---: | ---: | ---: |
| 4.000 | 0,3 % | 333 s |
| 3.500 | 0,55 % | 182 s |
| 3.000 | 0,8 % | 125 s |
| 2.000 | 2 % | 50 s |
| 1.200 | 5 % | 20 s |
| 700 | 11 % | 9 s |
| 300 | 24 % | 4 s |

Zwischen zwei Zeilen steigt der Schaden linear. In Trefferpunkten pro Sekunde, für die Standardausstattung:

| Schiff | Max. HP gesamt | Bei 3.500 | Bei 3.000 | Bei 2.000 | Bei 1.200 | Bei 700 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Protos | 30.000 | 165 | 240 | 600 | 1.500 | 3.300 |
| Kitefin | 46.000 | 253 | 368 | 920 | 2.300 | 5.060 |
| Ostirion | 82.500 | 454 | 660 | 1.650 | 4.125 | 9.075 |
| Nomad | 130.500 | 718 | 1.044 | 2.610 | 6.525 | 14.355 |
| Paragon | 162.500 | 894 | 1.300 | 3.250 | 8.125 | 17.875 |
| Storm | 198.000 | 1.089 | 1.584 | 3.960 | 9.900 | 21.780 |
| Wraith | 372.000 | 2.046 | 2.976 | 7.440 | 18.600 | 40.920 |
| Ironclad | 673.200 | 3.703 | 5.386 | 13.464 | 33.660 | 74.052 |

- Den Schaden **nimmt zuerst der Schild**, dann die Hülle. Es ist kein Treffer: Die Absorption des Schilds spielt keine Rolle, und ausweichen kannst du ihm nicht.
- Strahlung zählt als **erlittener Schaden**: Dein Schild lädt sich nicht auf, eine Repair Drone stoppt („Reparatur unterbrochen: Strahlung.“) und lässt sich nicht starten, und eine Schutzzone würde dich erst 5 Sekunden nach der letzten Dosis schützen.
- Booster und Upgrades ändern, wie groß deine Gesamtsumme ist, nicht, wie lange du durchhältst: Der Schaden ist ein Anteil davon.
- Nichts macht ein Schiff immun. Strahlung ist kein Treffer, also fängt nichts sie ab; die Fähigkeiten wirken darin aber weiter: Ein Shield Surge stellt deinen Schild weiter wieder her und eine Emergency Repair heilt deine Hülle weiter, jeweils für ihre zehn Sekunden (sie sind nicht die natürlichen Reparaturen, die die Dosis stoppt). Eine Tarnung verbirgt das Schiff nicht vor ihr.

## Der Sog {#the-pull}

Innerhalb von 3.000 Einheiten zieht das Schwarze Loch jedes Schiff zur Mitte, und der Sog wird nur stärker, je näher du kommst. Am Rand setzt er sanft ein und ist schon 200 Einheiten weiter innen spürbar:

| Entfernung | Sog (Einheiten pro Sekunde) | Ein Schiff, das nicht fliegt, wird getragen |
| ---: | ---: | :--- |
| 3.000 | 0 | noch gar nicht |
| 2.800 | 25 | 25 Einheiten in einer Sekunde |
| 2.300 | 60 | 60 Einheiten in einer Sekunde |
| 1.800 | 120 | 120 Einheiten in einer Sekunde |
| 1.300 | 220 | 220 Einheiten in einer Sekunde |
| 1.000 | 262 | 262 Einheiten in einer Sekunde, Tendenz steigend |
| 900 | 289 | 289 Einheiten in einer Sekunde, schnell steigend |
| 700 | 496 | in etwa einer Sekunde bis zum Horizont |
| 300 | 2.829 | der Ereignishorizont |

Von 3.000 bis 925 Einheiten steigt der Sog zwischen zwei Zeilen linear; innerhalb von 925 folgt er einer steileren Kurve (die letzten drei Zeilen liegen auf ihr). Er ist eine Strömung: Er bewegt dein Schiff, und deine Triebwerke kämpfen dagegen an.

- **Ein Schiff, das nicht fliegt, kann nicht stillstehen.** Hältst du an (du erreichst den Punkt, den du angeklickt hast, oder du hast nie einen Befehl gegeben), trägt das Schwarze Loch dein Schiff zur Mitte, und dein Befehl wandert mit, sodass dein Schiff weiter fällt, egal wie schnell seine Triebwerke fliegen könnten. Um eine Position zu halten, musst du weiter dorthin fliegen: Halte die Maus darauf, dann hält dein Schiff seine Position, wo sein Tempo über dem Sog liegt, und sackt zwischen zwei Befehlen ein wenig ab. Zwei Schiffe, die im Sog anhalten, um sich zu beschießen, werden beide hineingetragen.
- **Ein Schiff, das fliegt, spürt Gegenwind.** Fliegst du direkt von der Mitte weg, wird das Tempo deines Schiffs um den Sog an deiner Position gekürzt: Mit Tempo 155 schaffst du bei 2.800 noch 130 Einheiten pro Sekunde, bei 2.300 noch 95 und bei 1.800 noch 35, und bei 1.500 (ein Sog von 180) kommst du gar nicht mehr voran.

Dein **Punkt ohne Wiederkehr** ist die Entfernung, in der der Sog deinem Tempo entspricht. Ein Schiff mit Tempo 150 hat ihn bei 1.650 Einheiten; je schneller du bist, desto tiefer liegt er:

| Schiff (Standardausstattung) | Tempo | Punkt ohne Wiederkehr |
| :--- | ---: | ---: |
| Ironclad | 99 | 1.974 |
| Protos | 165 | 1.577 |
| Kitefin | 184 | 1.480 |
| Ostirion | 208 | 1.362 |
| Nomad | 211 | 1.347 |
| Paragon | 222 | 1.287 |
| Wraith | 233 | 1.208 |
| Storm | 263 | 995 |

Ein Schiffsdesign ändert das Tempo seines Schiffs und damit auch seinen Punkt ohne Wiederkehr: Eine DUMA ist langsamer als eine Ironclad, eine NOTSUM schneller als eine Storm.

Ein Schiff, das schneller als 272 Einheiten pro Sekunde ist (eine auf Flucht ausgelegte Ausstattung oder eine Wraith in Standardausstattung mit laufendem Afterburner), hat seinen Punkt ohne Wiederkehr dort, wo er immer lag: Bei Tempo 300 liegt er bei 885, bei 432 bei 747.

Rüste auf Tempo, und du kommst aus größerer Tiefe heraus; pack dich mit schweren Schilden voll, und du schaffst es nicht (eine Ironclad, das langsamste Schiff, mit einem Heavy Shield Core in allen 14 Slots fliegt mit 39,1, ihr Punkt ohne Wiederkehr liegt bei etwa 2.600). Nur ein Geschwindigkeitsschub holt ein Schiff knapp innerhalb seines Punkts ohne Wiederkehr noch zurück: Ein laufender [Afterburner](/wiki/03-Mechanics/Abilities.md) zählt und verlegt den Punkt ohne Wiederkehr nach innen, solange er läuft (zehn Sekunden mit einem Triebwerk, fünfzehn mit zwei, zwanzig mit drei; Afterburner III verlegt den einer Protos in Standardausstattung von 1.577 auf 989 und den einer Wraith in Standardausstattung von 1.208 auf 801). Innerhalb von etwa 390 Einheiten kommt nichts mehr heraus, auch kein auf Tempo ausgelegtes Schiff, dessen Tempowerte alle bis zum Maximum verzaubert sind und das den stärksten Schub laufen hat (einen bis zur Obergrenze verzauberten Afterburner III, x1,69); ein unverzaubertes, auf Tempo ausgelegtes Schiff (Engine IIIs mit einem Impulse Thruster IV und zwei Momentum Thruster IV, Adaptive Core IIs mit zwei Impulse Thruster IV) mit Afterburner III kommt bestenfalls von außerhalb von 427 heraus.

Der Fall vom Punkt ohne Wiederkehr beginnt langsam: Ein Schiff, das wenige Einheiten innerhalb davon mit voller Kraft fliegt, wird über zwanzig Sekunden oder länger hineingezogen, dann immer schneller. Der Sog ist kein Flug: Er zählt nicht als geflogene Strecke.

## Der Ereignishorizont {#the-event-horizon}

Ein Schiff, das bis auf 300 Einheiten an die Mitte herankommt, wird zerstört. Ein Schiff, dessen Hülle schon auf dem Weg dorthin unter der Strahlung aufgebraucht ist, wird stattdessen von der Strahlung zerstört. So oder so:

- Es ist eine gewöhnliche Zerstörung: Du wählst, wo du zurückkommst (siehe [Zerstörung und Rückkehr](/wiki/01-General/Getting-Started.md)), mit höchstens 10.000 Hülle und leerem Schild (siehe dort), und sie kostet, was eine Zerstörung immer kostet. „An Ort und Stelle“ setzt dich nie wieder in den Ring: Es versetzt dich zum nächsten Punkt außerhalb davon (4.500 Einheiten von der Mitte) und sagt dir das.
- **Kein Wrack, keine Kiste, keine Beute**, und du verlierst keine Ehre.
- Deine Zerstörung wird wie ein PvP-Abschuss dem **letzten feindlichen Piloten angerechnet, der dein Schiff in den 15 Sekunden vor seinem Ende getroffen hat**: einem Piloten eines anderen Konzerns (wo und wann PvP erlaubt ist), egal wie klein der Treffer war. Für ihn zählt es als Abschuss in seiner Statistik und bringt PvP-Rangpunkte nach deinem Schiffstyp, sonst nichts. Ein einziger Schuss genügt, und hat dich in diesen 15 Sekunden niemand aus einem anderen Konzern getroffen, bekommt niemand etwas.
- Piloten deines eigenen Konzerns, die dein Schiff in diesen 15 Sekunden getroffen haben, verlieren trotzdem die Ehre für Eigenbeschuss, egal was es zerstört hat.
- Aliens und Konzernpiloten kommen nie in seine Nähe. Gerät doch einer hinein, verschwindet er ohne Beute, Belohnung oder Anspruch.

## Was du siehst und hörst {#what-you-see-and-hear}

Der Bildausschnitt ist klein (beim Standardzoom etwa 1.900 mal 1.150 Einheiten auf dem Bildschirm, ganz herausgezoomt 4.400 mal 2.650), daher zeigt sich das eigentliche Bild des Schwarzen Lochs nur innerhalb von etwa dreitausend Einheiten (ganz herausgezoomt 3.600). Aus größerer Entfernung weist nichts auf dem Bildschirm darauf hin (schau auf die Minikarte oder die Sternensystem-Karte, unten); die Warnungen der Oberfläche kommen erst, wenn du nah bist:

- **Aus der Ferne.** Neigst du die Kamera nach unten, um über die Ebene zu blicken, wird das Schwarze Loch dort gezeichnet, wo es auf dem Bildschirm liegt, von überall im Sektor aus, sobald es im Bild ist: eine schwarze Scheibe mit einem Ring in einem Schein aus Akkretionslicht, so skaliert, dass sie gut zu sehen bleibt (etwa 2 % der Bildhöhe aus der entferntesten Ecke, die etwa 18.000 Einheiten entfernt ist), und sie wächst in ihr eigentliches Bild hinein, während du dich näherst. Nichts darin bewegt sich von selbst. Ist das Schwarze Loch nicht im Bild, gibt es auf dem Bildschirm keine Markierung dafür.
- **Ringe auf der Flugebene.** Ein violettes Band leuchtet bis zu einer scharfen Kante am Rand der Strahlung (4.000 Einheiten), und ein dünneres bernsteinfarbenes markiert den Rand des Sogs (3.000). Innerhalb des Sogs zeigt eine **rote Linie** *deinen eigenen* Punkt ohne Wiederkehr. Sie folgt deinem Tempo und wandert also, wenn dein Schiff schneller oder langsamer wird.
- **Die Anzeige** über der Aktionsleiste erscheint innerhalb von tausend Einheiten vor dem Rand und bleibt, solange du brennst. Sie zeigt die Strahlung in Prozent der gesamten HP deines Schiffs pro Sekunde, wie lange die Strahlung allein bräuchte, um den Rest aufzuzehren („Tödlich in 31 s“, rot unter zehn), einen Balken dieser HP, den Sog an deiner Position gegen dein Tempo und die Strecke, die dir noch bis zu deinem Punkt ohne Wiederkehr bleibt, oder eine blinkende Warnung, sobald du ihn hinter dir hast. Zeige auf eine Zeile, um zu sehen, was sie bedeutet; das (i) öffnet eine Karte.
- **Die Bildschirmränder** leuchten violett, werden mit steigender Dosis rot und pulsieren einmal pro Sekunde.
- **Die Minikarte** zeichnet das Schwarze Loch mit seinen Ringen als Ellipsen (die Karte streckt sich mit ihrem Fenster), und ihr Tooltip nennt die Radien. Die Sternensystem-Karte markiert den Sektor mit einem kleinen Schwarzen Loch.
- **Ein Strahlungszähler** tickt über den Kampflärm hinweg umso schneller, je höher die Dosis steigt. Ein Warnton aus zwei Tönen erklingt, wenn du den Rand überquerst, und noch einmal an deinem Punkt ohne Wiederkehr, und ab etwa 6.500 Einheiten ist ein tiefes Grollen zu hören, umso tiefer, je näher du bist.
- **Das Bild:** ab **Grafik Mittel** (mit eingeschalteter Nachbearbeitung) wird das Loch gezeichnet, indem das Licht um es herum Strahl für Strahl verfolgt wird: ein schwarzer Schatten mit einem dünnen weißen Photonenring darum, und die Akkretionsscheibe so, wie ihr Licht dich erreichen würde. Mit hoher Kamera ist es ein heller Ring um das Dunkel; kippst du die Kamera tief, biegt sich die Rückseite der Scheibe über das Loch hinweg nach oben und ihre Unterseite darunter, während die Vorderseite davor vorbeiläuft. Auch der Himmel hinter dem Loch krümmt sich, mäßig: Sterne, Nebel, Planeten und Asteroiden werden um den Schatten nach außen gedrückt, und ihre Linien biegen sich um ihn. Schiffe werden über das Loch gezeichnet und von ihm nicht mehr geschwärzt: Ein Rumpf zwischen dir und dem Loch bleibt davor. Mittel verfolgt das Licht über weniger Windungen, zeichnet weniger Bilder der Scheibe und lässt die Aufhellung der Seite weg, die sich auf dich zudreht, die Hoch und Ultra hinzufügen. **Niedrige Grafikqualität** und ein Bild ohne Nachbearbeitung behalten das ältere Bild: eine schwarze Scheibe mit einem hellen Ring und eine Akkretionsscheibe aus drei gegenläufig rotierenden Schichten, ohne Krümmung des Himmels. Eine Grafikkarte, die das neue Bild nicht aufbauen kann, fällt ebenfalls auf das ältere Bild zurück, mit der schwachen Krümmung der Sterne, die es hatte. Auf jeder Stufe kommen Materieschlieren hinzu, die entlang des Sogs hineinfallen (sie fallen mit der Geschwindigkeit des Sogs selbst, sodass ein Schiff, das nicht fliegt, im Gleichschritt mit ihnen hineingetragen wird und eines, das gegen den Sog hinausfliegt, sie vorbeiströmen sieht). Ein Schiff, das der Sog trägt, hat keine Triebwerksflamme und hinterlässt keine Triebwerksspur; eines, das gegen ihn hinausfliegt, brennt mit vollem Tempo durch die Strömung, und seine Spur strömt zum Loch. Das Kamerazittern wächst mit dem Sog, gemessen in Anteilen des Tempos deines Schiffs, erreicht an deinem Punkt ohne Wiederkehr seine eingestellte Stärke und steigt bis zum Horizont weiter. Ein Schiff, das das Loch verbrennt, sprüht violette Funken; eines, das es verschluckt, wird zur Mitte gezogen und in die Länge gestreckt. Der Himmel des Sektors ist der dunkle violett-grüne von `DS-3`.
- **Die Trümmer:** Felsbrocken und Teile zerstörter Hüllen kreisen um das Schwarze Loch und fallen auf Spiralen hinein, vom Rand seines Sogs bis zum Horizont: erst langsam, dann immer schneller, sie fegen um das Loch herum und taumeln umso schneller, je näher sie kommen. Sie glühen orange im Licht der Scheibe, werden zu Nadeln gestreckt, während sie zerrissen werden, und sind verschwunden, bevor sie den Horizont erreichen. Ein paar große Brocken sind darunter, und manche treiben über der Flugebene, sodass Schiffe unter ihnen hindurchfliegen. Sie sind reine Kulisse: Nichts trifft sie, und sie treffen nichts, und sie zeigen sich nur innerhalb von etwa viertausend Einheiten um das Schwarze Loch und blenden zu 6.500 hin aus. Das Licht der Scheibe fällt auch auf dein Schiff, wenn es nah ist.
- **Wenn du stirbst**, sagt die Einblendung, warum: „Vom Schwarzen Loch verschluckt“ oder „Von Strahlung verbrannt“, und im Spielprotokoll steht die Zeile dazu.

Einstellungen helfen, wo das Loch den Rechner stark fordert oder die Augen anstrengt: **Bewegung reduzieren** hält die Scheibe und die Schlieren an, lässt die Trümmer stillstehen und stoppt das Pulsieren der Bildschirmränder, und **Bildschirmwackeln reduzieren** stoppt das Kamerazittern nahe dem Loch; **niedrige Grafikqualität** behält das ältere Bild ohne die Raytracing-Linse und zeichnet weniger Schlieren (40, gegenüber 100 bei Mittel und 200 darüber) und weniger Trümmerteile (30, gegenüber 80 bei Mittel und 160 darüber), lässt den Ring zum Ausgleich heller brennen und zeichnet die Fernansicht mit einem Schein weniger. Eine niedrigere **Partikelqualität** dünnt die Trümmer so aus, wie sie die Felsen im Hintergrund ausdünnt.

## Draußen bleiben {#staying-out}

- Der Server lenkt dich: Ein Bewegungsbefehl, der dein Schiff quer durch den Strahlungsring führen würde (4.200 Einheiten von der Mitte, etwas weiter als die Strahlung selbst), wird stattdessen **um ihn herum** geflogen, an seinem Rand entlang. Befehle, die innerhalb des Rings enden, werden so geflogen, wie du sie gibst; hineinzufliegen ist deine Entscheidung. Routen quer durch den Sektor werden bis zu einem Fünftel länger, die Bahnen zwischen den Portalen gar nicht.
- Der Tab **System** des Chats warnt dich, wenn du den Rand der Strahlung, den Rand des Sogs und deinen eigenen Punkt ohne Wiederkehr überquerst, und noch einmal, wenn du wieder draußen bist. Diese Zeilen stehen nicht in **Global** oder **Lokal**.
- Verlässt du das Spiel in der Strahlung, aber außerhalb des Sogs, kommst du am äußeren Rand des Rings zurück, auf der Stelle haltend, mit der Hülle, die du hattest. Verlässt du es **innerhalb des Sogs** (3.000 Einheiten), kommst du genau dort zurück, wo du es verlassen hast, mit der Hülle, die du hattest, und der Fall geht weiter: Ausloggen ist kein Ausweg aus dem Schwarzen Loch.
- Eine ältere Version des Spiels zeigt das Schwarze Loch nicht. Sie bekommt trotzdem die Warnungen und die Lenkung und kann per Befehl trotzdem in den Ring fliegen.

Drohnen fliegen mit ihrem Schiff. Fracht wird nie innerhalb des Rings abgelegt: Eine Kiste, die dort landen würde, wird auf seinen Rand gesetzt. Dark-Matter-Kisten sind die einzige Ausnahme.

## Dark Matter gewinnen {#dark-matter}

Neu bei Dark Matter? [Dark Matter und Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) beschreibt den ganzen Weg, von der Forschung bis zur Plate. Dieser Abschnitt ist die Seite des Schwarzen Lochs.

Das Loch gibt **Dark Matter** für eine **N.I.K.E.**-Rakete zurück, die es erreicht. Eine N.I.K.E. ist eine Rakete mit 67.500 bis 75.000 Schaden, die das erste Schiff trifft, das sie verletzen darf, und daran verbraucht ist; ist nichts im Weg, fliegt sie zum Loch und wird verbraucht, wenn sie den Ereignishorizont überquert. Die [Montage](/wiki/06-Items/Rockets.md) stellt N.I.K.E.s her, sobald ihre Technologie erforscht ist ([Forschung](/wiki/03-Mechanics/Research.md)), fünf pro Herstellung (100.000 Credits, 1.500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite).

- **Abfeuern.** Eine N.I.K.E. fliegt 4.050 Einheiten in 4,5 Sekunden (900 pro Sekunde) geradeaus dorthin, wohin du gezielt hast: Ohne gewähltes Ziel setzt du den Mauszeiger auf das Schwarze Loch (oder richtest dein Schiff darauf aus). Sie erreicht den Horizont von überall zwischen dem Rand der Strahlung (4.000 Einheiten) und 4.380 Einheiten von der Mitte. Von weiter draußen fällt sie zu kurz und ist verschwendet. Wie jede Rakete nutzt sie den gemeinsamen Timer, und danach wartest du 4,6 Sekunden auf die nächste Rakete (du brauchst dafür keinen ausgerüsteten Laser); das Abfeuern beendet deinen Schutz in der Schutzzone und deine Tarnung. **Ein Schiff in der Schusslinie bekommt sie stattdessen ab**: Ein Rivale, der am Rand wartet, oder ein Pilot eines anderen Konzerns, der im Weg Kisten einsammelt, wird mit 67.500 bis 75.000 getroffen, und das Loch bekommt nichts. Aliens und Konzernpiloten kommen nie in den Ring, also liegt es an dir, die Linie frei zu halten; die Rakete fliegt durch deinen eigenen Konzern hindurch und durch Schiffe, die vor dir sicher sind. Verlässt du die Karte nach dem Schuss, fliegt sie weiter, ohne jemanden zu verletzen, und erzeugt trotzdem dein Dark Matter. Eine Drohnenformation kann den Schaden des Treffers ändern, aber nicht die Wartezeit nach einer N.I.K.E. (siehe [Drohnenformationen und Raketen](/wiki/06-Items/Rockets.md#drone-formations-and-rockets)).
- **Was zurückkommt.** Jede N.I.K.E., die den Horizont erreicht, bringt **1, 2 oder 3 Dark Matter** (im Schnitt 2, fünf N.I.K.E.s machen also etwa zehn), in einer oder zwei kleinen Kisten, die am Rand der Zone des Lochs erscheinen, **3.050 bis 3.950 Einheiten von der Mitte**, nahe der Linie, auf der dein Schuss hereinkam. Der Sog endet bei 3.000, also werden die Kisten und die Schiffe, die sie einsammeln, nicht gezogen, und die Strahlung beträgt dort 0,3 bis 0,8 % der HP eines Schiffs pro Sekunde: Eine Minute in der Mitte des Bands kostet ein Drittel deines Schiffs. Ein volles Schiff hält dort drei Minuten durch.
- **Wem sie gehören.** Die Kisten gehören dir und deinem Clan, **60 Sekunden** lang ab dem Schuss. Danach darf jeder auf der Karte sie nehmen, und nach **4 Minuten** treiben sie davon. Der Gefahrensektor ist ein PvP-Sektor, also rechne mit Gesellschaft. Ein Pilot, der sich nach dem Abfeuern ausloggt, behält seine Kisten.
- **Wie viele.** Eine Karte fasst höchstens 32 Dark-Matter-Kisten; eine neue verdrängt die älteste von ihnen und nie eine andere Art von Kiste. Der [Resource Magnet Booster](/wiki/03-Mechanics/Cargo.md) fügt Dark Matter nichts hinzu.
- **Was du siehst.** Überquert eine N.I.K.E. den Horizont, wird sie in das Loch hineingestreckt, der Raum kräuselt sich von der Stelle aus, an der sie eintrat, und die Scheibe und der Photonenring flammen etwa anderthalb Sekunden lang auf (ein Drittel davon, mit halbem Licht, unter **Bewegung reduzieren**). Einen Moment später kommen die Kisten aus dem Loch und treiben an ihre Plätze am Rand: Jede ist eine violett-schwarze Kugel mit hellem Rand und Funkeln, von Weitem gut zu sehen, und trägt den Titel **Dark Matter**, wenn du auf sie zeigst. Über deinen stehen die Sekunden, die dir bleiben, und sie erscheinen auf der Minikarte als kleine violette Markierung, ebenso für deinen Clan; die Kisten anderer Piloten erscheinen auf der Minikarte erst, wenn ihre Minute vorbei ist.
- **Wofür es gut ist.** Die Montage presst 5 Dark Matter mit einer Velkonite und einer Orvium Reinforced Plate zu einer **Dark Matter Plate**, und [die Schmiede](/wiki/06-Items/Forge.md) verlangt zwei davon, um einen Gegenstand von Göttlich auf Berstend zu heben und noch einmal von Berstend auf Ewig: zehn Dark Matter pro Schritt. Die letzte Stufe jeder Aufwertungskette verlangt 3 Plates, 15 Dark Matter pro Teil: die Amps, Schildzellen und Schubdüsen der Stufe IV sowie Heavy Shield Core, Engine III, Helios Beam, Extra Slots CPU III und Base CPU II. Auch das [Forschungszentrum](/wiki/03-Mechanics/Research.md#dark-matter) des Skylab braucht Dark Matter: 10 für jede der 16 Technologien an der Spitze seines Baums, insgesamt 160, dem Zentrum hinzugefügt, bevor die Forschung beginnt. Auch die Drohnenformationen verlangen Dark Matter, je nach Stärke 5, 13 oder 20: 189 mehr, insgesamt 349. Die beiden Forschungen der Hüllenpanzerung verlangen 65 mehr, die Schiffsdesigns und Panzerungs-Slots 490 ([Forschung](/wiki/03-Mechanics/Research.md#ship-technologies)). Ein Helios Beam mit seinen drei Amps der Stufe IV enthält 60 Dark Matter, ein Wraith, der nur Teile der letzten Stufe trägt, 900 ([Dark Matter und Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)).
