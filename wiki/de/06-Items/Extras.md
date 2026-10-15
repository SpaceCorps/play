<!-- wiki-i18n source: d73343b5c426be4e -->
<!-- wiki-i18n title: Extras -->
# Extras

Extras sind die Gadgets in den **Extra-Slots** eines Schiffs (zwei auf Protos, Kitefin, Ostirion und Nomad, den Schiffen, mit denen du startest oder die du kaufst, und drei auf Paragon, Ironclad, Wraith und Storm, den Schiffen, die du baust, pro Konfiguration, und 3, 5 oder 7 mehr mit den Extra Slots CPUs). Du schaltest eines über die Extras-Auswahl der Aktionsleiste ein oder über einen Slot der Aktionsleiste, dem du es zugewiesen hast. Sie wirken nur in der Konfiguration, die du fliegst: Setzt du eines in die andere Konfiguration ein, wartet es, bis du wechselst.

| Extra | Wirkung | Nutzungen | Preis |
| :---- | :------ | :-------- | :---- |
| **Repair Drone I bis IV** | Repariert deine Hülle, 1,5 %, 2,25 %, 3,5 % und 5 % des Maximums pro Sekunde | unbegrenzt | 5.000 / 15.000 / 35.000 Credits, 2.000 Thulium |
| **Cloaking CPU S** | Verbirgt dein Schiff | 10 | 5.000 Thulium |
| **Cloaking CPU M** | Verbirgt dein Schiff | 25 | 11.250 Thulium |
| **Cloaking CPU L** | Verbirgt dein Schiff | 50 | 20.000 Thulium |
| **P.E.T. Station I bis III** | Ist sie AN, geben 2, 3 oder 5 angedockte [P.E.T.s](/wiki/03-Mechanics/Pets.md#the-station) deinem Schiff Boosts, sammeln Erfahrung und arbeiten; ist sie AUS, tun sie nichts davon | AN / AUS | Montage, nach ihrer Erforschung (der Gegenstandsbaum unten) |

Die Cloaking CPUs gibt es nur im Shop. Sie lassen sich nicht zusammenführen, und nichts verschenkt sie. Die **EMP Charge** ist kein Extra mehr: Seit 0.4.21 ist sie ein Verbrauchsgut, das wie eine Rakete als Stapel getragen wird und in keinem Slot sitzt, sie belegt also keinen deiner Extra-Slots (siehe [Raketen](/wiki/06-Items/Rockets.md#emp-charge)). Die beiden **Energetic Walls** sind ebenfalls keine Extras mehr: Seit 0.4.22 sind auch sie Verbrauchsgüter, werden als Stapel getragen und sitzen in keinem Slot (siehe [Energetic Wall](#energetic-wall)).

Das **Startpaket** eines neuen Piloten legt schon zwei Extras in die beiden Extra-Slots der Protos: eine **Base CPU I** (10 Nutzungen, ein Teleport zur Basis deines Konzerns) und eine **Repair Drone I**. Ziehe sie aus der Extras-Auswahl der Aktionsleiste auf einen Slot, um sie zu benutzen. Nur neue Piloten bekommen das Paket: Wer sich vor 0.4.10 angemeldet hat, hat es nicht.

Sieben weitere CPUs werden nicht verkauft: Die Montage stellt sie her, sobald das Forschungszentrum des Skylab sie erforscht hat (siehe [Forschung](/wiki/03-Mechanics/Research.md)). Es sind die Extra Slots CPU I, II und III, die Jump CPU, die Base CPU I und II und die Auto-Repair CPU, und [der letzte Abschnitt](#research-cpus) sagt, was jede tut. Wie die Cloaking CPU sind die Jump CPU und die Base CPUs etwas für einen ruhigen Moment: Keine der drei startet innerhalb von 10 Sekunden nach einem Schuss, den du abgibst, oder einem Treffer, den du einsteckst. Die beiden Warp-CPUs, die Jump CPU und die Base CPUs, werden außerdem verweigert, solange du einen Missionsgegenstand trägst („Mit einem Missionsgegenstand an Bord kannst du keine Warp-CPU benutzen.“): siehe [Missionsgegenstände](/wiki/03-Mechanics/Quests.md#quest-items).

Auf jedem Extra steht ein kurzes Kürzel auf seinem Slot der Aktionsleiste: **REP** für eine Repair Drone, **CLK** für eine Cloaking CPU und **ARP**, **BSE** und **JMP** für die Auto-Repair, die Base und die Jump CPU. Die Verbrauchsgüter haben ihre eigenen Kürzel: **EMP** und **WAL** (für eine Energetic Wall). Die drei **P.E.T. Station**-Gegenstände sind Extras wie die anderen, mit dem Kürzel **PET**: Rüste eine aus, und ihr Slot schaltet die Station **AN** oder **AUS** (eine Sekunde zwischen zwei Drücken) und zeigt, welches von beiden. Ist sie AN, zählen die angedockten [P.E.T.s](/wiki/03-Mechanics/Pets.md), ist sie AUS, zählen sie nicht. Zeige auf einen Slot, um zu lesen, was ein Druck gerade bewirkt oder warum er nichts bewirkt.

![The Extras picker of the hotbar: the Repair Drone, the Auto-Repair, Cloaking, Base and Jump CPUs and the P.E.T. Station you have fitted (REP, ARP, CLK, BSE, JMP, PET), to drag onto a slot](../../img/wiki-img/shots/cpu-hotbar.jpg)
![The Consumables picker of the hotbar: the EMP Charge and the Energetic Wall I and II (EMP, WAL) to drag onto a slot, with how many of each you hold](../../img/wiki-img/shots/emp-hotbar.jpg)
![The hotbar with extras on its slots: a Repair Drone, a Cloaking CPU with its uses left, the P.E.T. Station that says ON, the EMP Charge and the Energetic Wall I and II with the number of each you carry](../../img/wiki-img/shots/hotbar-slots.jpg)
![The Repair Drone of an extra slot docked to its ship and its wingmen](../../img/wiki-img/shots/repair-drones-extra.jpg)
![The Shop's Consumables category: the EMP Charge and the Energetic Wall I with their prices in Thulium, and the Energetic Wall II, which only Assembly makes](../../img/wiki-img/shots/shop-consumables.jpg)

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
P.E.T. Station I | extra, common | craft 100000 Credits, 2000 Thulium, 300 s | research 10800 s, 10800 science | 25 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU S | extra, common | buy 5000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Repair Drone I | extra, common | buy 5000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone II | extra, common | buy 15000 Credits | /wiki/06-Items/Extras.md#repair-drones
Repair Drone III | extra, common | buy 35000 Credits | /wiki/06-Items/Extras.md#repair-drones
Extra Slots CPU I | extra, uncommon | craft 12000 Thulium, 300 s | research 1800 s, 1800 science | 60 Ship Fragment, 3 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU I | extra, uncommon | craft 8000 Thulium, 300 s | research 10800 s, 10800 science | 40 Ship Fragment, 2 Power Core, 4 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#base-cpus
P.E.T. Station II | extra, uncommon | craft 400000 Credits, 6000 Thulium, 600 s | research 36000 s, 36000 science | 60 Ship Fragment, 6 Reinforced Hull Plate, 4 Power Core, 8 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Cloaking CPU M | extra, uncommon | buy 11250 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU II | extra, rare | craft 30000 Thulium, 600 s | research 36000 s, 36000 science | 120 Ship Fragment, 10 Reinforced Hull Plate, 6 Power Core, 12 Velkonite Reinforced Plate, 2 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Base CPU II | extra, rare | craft 20000 Thulium, 600 s | research 36000 s, 36000 science | 100 Ship Fragment, 5 Power Core, 1 Ancient Control Unit, 2 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#base-cpus
Auto-Repair CPU | extra, rare | craft 15000 Thulium, 600 s | research 21600 s, 21600 science | 80 Ship Fragment, 8 Reinforced Hull Plate, 4 Power Core, 6 Velkonite Reinforced Plate | /wiki/06-Items/Extras.md#auto-repair-cpu
P.E.T. Station III | extra, rare | craft 1500000 Credits, 18000 Thulium, 900 s | research 86400 s, 86400 science | 120 Ship Fragment, 12 Reinforced Hull Plate, 8 Power Core, 2 Ancient Control Unit, 12 Velkonite Reinforced Plate, 4 Orvium Reinforced Plate | /wiki/06-Items/Extras.md
Repair Drone IV | extra, rare | buy 2000 Thulium | /wiki/06-Items/Extras.md#repair-drones
Cloaking CPU L | extra, rare | buy 20000 Thulium | /wiki/06-Items/Extras.md#cloaking-cpu
Extra Slots CPU III | extra, epic | craft 75000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 240 Ship Fragment, 25 Reinforced Hull Plate, 12 Power Core, 2 Ancient Control Unit, 6 Orvium Reinforced Plate, 4 Dark Matter Plate | /wiki/06-Items/Extras.md#extra-slots-cpus
Jump CPU | extra, epic | craft 40000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 200 Ship Fragment, 20 Reinforced Hull Plate, 10 Power Core, 3 Ancient Control Unit, 15 Velkonite Reinforced Plate, 10 Orvium Reinforced Plate | /wiki/06-Items/Extras.md#jump-cpu

P.E.T. Station I -> P.E.T. Station II -> P.E.T. Station III
Cloaking CPU S -> Cloaking CPU M -> Cloaking CPU L
Repair Drone I -> Repair Drone II -> Repair Drone III -> Repair Drone IV
Extra Slots CPU I -> Extra Slots CPU II -> Extra Slots CPU III
Base CPU I -> Base CPU II
```
<!-- item-tree:end -->

## Repair Drones

Schalte eine Repair Drone ein (REP), und sie repariert die Hülle, bis sie voll ist. Sie startet erst nach 10 Sekunden ohne Treffer, und jeder Treffer schaltet sie wieder aus. Sind mehrere ausgerüstet, arbeitet die beste. Eine [Auto-Repair CPU](#auto-repair-cpu) schaltet sie dir wieder ein. Die Raten stehen unter [Kampf](/wiki/03-Mechanics/Combat.md). Während sie repariert, fliegen kleine Reparaturdrohnen aus dem Schiff, kreisen um es und bestrahlen die Hülle, eine für eine Repair Drone I, zwei für eine II, drei für eine III oder IV, und die Piloten in deiner Nähe sehen sie; wenn die Reparatur endet, docken sie wieder an.

## Cloaking CPU

Drücke den CLK-Slot, um dich zu tarnen. **Ein Druck ist eine Nutzung**, egal welches Paket, und die übrigen Nutzungen siehst du am Slot und im Hangar. Eine Tarnung hat **kein Zeitlimit**: Sie bleibt an, bis du sie ausschaltest oder etwas sie unterbricht.

- **Wer dich nicht sehen kann.** Piloten anderer Konzerne und Aliens sehen dein Schiff überhaupt nicht: Es ist weder auf ihrem Bildschirm noch in ihrer Zielliste, und niemand kann es anvisieren. Konzernpiloten anderer Konzerne ignorieren es ebenfalls.
- **Der Radarpunkt.** Jeder andere Pilot auf der Karte, außer denen deines eigenen Konzerns, sieht auf der Minikarte dort, wo du bist, einen schlichten **roten Punkt** und weiß daher, dass jemand Getarntes in der Nähe ist. Der Punkt hat weder Namen noch Schiff, Konzern oder ID und lässt sich nicht anklicken oder anvisieren; fährt man mit der Maus darüber, steht dort nur „Hier ist etwas getarnt“. Er ist rund, innerhalb eines Rings (Schiffe auf der Minikarte sind Quadrate), und der Ring „atmet“ langsam oder steht still, wenn du „Bewegung reduzieren“ aktiviert hast. Der Server aktualisiert ihn etwa zweimal pro Sekunde, und dein Spiel bewegt ihn dazwischen fließend. Er sagt, dass jemand da ist und wo, nicht wer: Ein Pilot, der gesehen hat, wie du dich getarnt hast, kann dem Punkt folgen, und die **Explosion einer Rakete**, die auf ihn gerichtet ist, trifft dich trotzdem.
- **Wer dich sehen kann.** Du siehst dein eigenes Schiff blass und mit Umriss. Piloten deines Konzerns sehen dich als blassen Geist; Clanmitglieder anderer Konzerne tun das nicht, weil ein Clan jeden aufnimmt, der sich bewirbt. Den Geist kann niemand anvisieren, nicht einmal dein Konzern.
- **Nicht tarnen kannst du dich** in einer Schutzzone, solange sich die CPU auflädt, oder innerhalb von **10 Sekunden** nach einem Treffer oder Schuss.
- **Was sie beendet.** Erneutes Drücken des Slots, deine erste Salve oder Rakete (sie trifft, und du wirst gesehen), das Betreten einer Schutzzone, das Ausscheiden der CPU aus der Konfiguration, die du fliegst, ein **EMP, der im Umkreis von 1.500 Einheiten** von dir ausgelöst wird, egal wer ihn eingesetzt hat (auch einer deines eigenen Konzerns, aber nicht einer aus deiner Gruppe), und der Flächenschaden einer Rakete, die dich trifft. Die Zeit beendet sie nicht, das Einsammeln von Fracht nicht (eine Kiste, die du nimmst, ist für alle weg, sie erfahren also, dass etwas in Reichweite dieser Stelle war, nicht wer), Fähigkeiten nicht, und die Strahlung des Schwarzen Lochs schadet einem getarnten Schiff, beendet aber seine Tarnung nicht. Ausloggen oder Sterben beendet sie, denn ein Schiff, das nicht geflogen wird, ist nicht getarnt.
- **Aufladung.** Nachdem eine Tarnung endet, egal wie, lädt sich die CPU **60 Sekunden** lang auf. Die Aufladung gehört dir, nicht dem Schiff: Sie läuft weiter, wenn du durch ein Portal springst, dich ausloggst oder stirbst. Jeder Druck kostet trotzdem eine Nutzung.
- **Aliens**, die hinter dir her waren, verlieren dich. Deine Abschussansprüche werden freigegeben, sobald du dich tarnst.
- **Raketen.** Niemand kann eine gelenkte Rakete auf dich aufschalten, und eine geradeaus fliegende Einzelziel-Rakete fliegt durch dich hindurch. Ein **Flächenschaden** trifft ein Schiff in seinem Bereich trotzdem und beendet dessen Tarnung, und die Piloten, die den Ort des Schiffs sehen können, bekommen ihn angezeigt, bevor die Schadenszahl erscheint. Das Abfeuern einer Rakete ist ein Schuss: Es beendet deine eigene Tarnung wie eine Salve (die CPU lädt sich dann die oben genannten 60 Sekunden auf) und hindert dich, ob getarnt oder nicht, 10 Sekunden danach daran, dich zu tarnen.
- **Das Schwarze Loch** verschluckt ein getarntes Schiff wie jedes andere, und die Karte bekommt es mit.
- **Was du siehst.** Dein Schiff wird durchsichtig und bekommt einen gestrichelten violetten Umriss, seine Drohnen verblassen mit ihm, und ein Chip oben auf dem Bildschirm sagt „Getarnt“ mit den übrigen Nutzungen (keine Sekunden: Es gibt keinen Timer). Der CLK-Slot zeigt die übrigen Nutzungen; solange du getarnt bist, leuchtet er violett und zeigt AN, und wenn die Tarnung endet, egal wie, dunkelt er ab und zählt die 60 Sekunden Aufladung herunter. Ein Druck, den der Server ablehnt (Aufladung, Schutzzone, ein Treffer oder Schuss in den letzten 10 Sekunden), lässt den Slot rot aufblitzen, und eine Meldung sagt dir, warum. Ein Verbündeter erscheint als blasser Geist mit einem Geistersymbol vor seinem Namen, und ein Pilot, der sich in deiner Nähe tarnt, verschwindet in einer Welle. Ziehe CLK aus den Extras der Aktionsleiste auf einen Slot, um es zu nutzen, wie REP.
- **Nutzungen** werden mit der CPU gespeichert. Ausloggen, Sterben oder ein Neustart des Spiels geben keine zurück, und eine Aktivierung, die du abbrichst, ist trotzdem verbraucht. Wenn die letzte Nutzung eines Pakets weg ist, ist es aufgebraucht, und sein Slot wird aus einer Reserve derselben CPU in deinem Inventar aufgefüllt, falls du eine besitzt.
- **Mehrere CPUs** in einer Konfiguration addieren sich nicht. Die mit den wenigsten verbleibenden Nutzungen wird zuerst benutzt.

S, M und L verhalten sich gleich: Die größeren Pakete sind nur pro Nutzung günstiger (500, 450 und 400 Thulium).

## Energetic Wall

Drücke den Slot WAL, und eine **Plasmawand** steht **an deinem Mauszeiger**, quer zur Linie von deinem Schiff dorthin: ein Streifen von 360 Einheiten Länge (etwa dreieinhalb Schiffsmodelle) und 10 Einheiten Breite. Ihre Mitte liegt höchstens **450 Einheiten** von der Mitte des Schiffs entfernt: Ein weiter entfernter Mauszeiger setzt sie 450 Einheiten weit auf die Linie, ein Mauszeiger näher als 120 Einheiten schiebt sie auf 120 hinaus. Solange der Slot bereit ist, zeigen eine blasse gepunktete Linie und ein Geisterumriss, wo sie stehen wird. Weiß das Spiel nicht, wo dein Mauszeiger ist, steht sie 220 Einheiten vor der Mitte des Schiffs, quer zur Flugrichtung. Eine Energetic Wall ist ein **Verbrauchsgut**, wie die [EMP Charge](/wiki/06-Items/Rockets.md#emp-charge): ein Stapel in deinem Inventar, der auf keinem Schiff einen Slot belegt (bis 0.4.22 war sie ein Extra). Ziehe sie aus den Verbrauchsgütern der Aktionsleiste auf einen Slot, um sie zu benutzen; die beiden Stufen sind zwei Einträge, ein Slot hält also eine Stufe. Sie ist zum Dahinterverstecken und zum Sperren einer Bahn da, nicht zum Hineinstellen.

- **Was sie aufhält.** Jeder Schuss, der sie kreuzt, trifft stattdessen die Wand, egal wer ihn abgegeben hat und von welcher Seite: eine Laser-Salve, eine Rakete, die Salve eines Aliens. Was dahinter steht, nimmt nichts, und die Trefferpunkte der Wand nehmen den Schaden. Die Explosion einer Rakete, die an der Wand losgeht, trifft die Schiffe auf ihrer nahen Seite und nicht die dahinter. Auch deine eigenen Schüsse: Durch deine eigene Wand kannst du nicht hinausschießen. Die N.I.K.E. und die Geschütze des Dormant Swamp fliegen darüber hinweg, wie über Asteroiden.
- **Was sie verbrennt.** Jedes Schiff, dessen Hülle den Streifen berührt, nimmt **2.500 Schaden pro Sekunde**, zuerst am Schild, auch dein eigenes, auch Aliens und Konzernpiloten. Ein Schiff in einer Schutzzone oder unter dem Schutz eines Respawns wird nicht verbrannt, und zwei Streifen auf einem Schiff addieren sich nicht.
- **Wie lange sie hält.** Eine Wand der Stufe 1 hat **30.000 Trefferpunkte**, eine der Stufe 2 **90.000**. Eine Wand verliert von selbst jede Sekunde ein Sechzigstel davon, also ist eine, auf die niemand schießt, nach **60 Sekunden** weg. Schüsse verkürzen das: Eine Wraith mit zwölf Helios Beams auf x4-Munition bringt eine Wand der Stufe 1 in etwa 3,5 Sekunden zu Fall.
- **Immer nur eine, ein Druck eine Wand.** Eine neue Wand ersetzt deine alte. Nach einem Druck lädt der Gegenstand **90 Sekunden** nach; die Wartezeit gehört dir, nicht dem Schiff: Sterben oder Ausloggen verkürzt sie nicht. Ein Druck verbraucht **eine Wand der Stufe, die der Slot hält**, und nur, wenn die Wand steht: Ein Druck, den das Spiel abweist (siehe unten), verbraucht nichts und startet keine Wartezeit. Ist von dieser Stufe keine mehr da, sagt es „Keine Energetic Wall mehr.“, und die andere Stufe wird nie an ihrer Stelle benutzt.
- **Wo nicht.** Nicht, solange dich eine Schutzzone oder ein Respawn schützt, nicht, wo der Streifen eine Schutzzone oder ein Tor berühren würde, nicht getarnt und nicht, wo die Mitte des Streifens außerhalb der Karte läge. Das Spiel sagt dir, welcher Fall es ist.
- **Abschüsse.** Ein Schiff, das die Wand zerstört, stirbt an Strahlung, und der Abschuss geht an den letzten feindlichen Piloten, der es innerhalb von 15 Sekunden getroffen hat, falls es einen gab. Wer die Wand aufgestellt hat, bekommt nichts gutgeschrieben, was er nicht selbst geschossen hat. Ein Alien, das die Wand zerstört, zahlt nichts: keine Belohnung, keine Beute.
- **Aliens umfliegen sie nicht.** Sie fliegen hindurch und verbrennen, oder sie bleiben auf ihrer Seite stehen und schießen auf die Wand.
- **Was du siehst.** Ein Streifen blauweißen Lichts mit hellen Strichen, die an ihm entlanglaufen, und einem Lichtpfosten an jedem Ende; er blitzt auf, wo ein Schuss einschlägt, und flackert, wenn er fast aufgebraucht ist. Eine Wand der Stufe 2 leuchtet stattdessen gelb, mit einem dickeren, helleren Kern und einem stärkeren Leuchten, ihr Streifen ist aber genauso 10 Einheiten breit wie bei einer Wand der Stufe 1. Eine dünne Lebensleiste daneben wird kürzer und färbt sich bernsteinfarben, dann rot; dein Slot zeigt die verbleibende Lebensdauer deiner Wand als Bogen und die Wartezeit als Schatten. Eine aufgestellte Wand flammt auf, eine abgeschossene bricht in Funken zusammen, und eine, deren Zeit ablief, verblasst. Auf deinem Slot steht außerdem die Zahl der Wände seiner Stufe, die dir bleiben.
- **Wie du sie bekommst und trägst.** Die Energetic Wall I gibt es im Shop für **250 Thulium** je Wand, und du trägst bis zu **20** davon in einem Stapel (was du in der [Auktion](/wiki/03-Mechanics/Auction.md) eingestellt hast, zählt mit). Die Energetic Wall II stellt die Montage her, **eine Wand je Herstellung**, für **600 Thulium**, 5 Ship Fragments und eine Power Core, sobald das Forschungszentrum sie erforscht hat (6 Stunden bei normaler Geschwindigkeit: [Forschung](/wiki/03-Mechanics/Research.md)); davon trägst du bis zu **10**. Wie Raketen gehen die Wände, die du trägst, mit der Saison verloren, wenn du sie nicht in den Transport-Cache legst; Wände im Transport-Cache lassen sich nicht benutzen. Eine selbst hergestellte Energetic Wall II kannst du in der Auktion verkaufen, eine Energetic Wall I, die der Shop verkauft, nie.

## CPUs des Forschungszentrums {#research-cpus}

Zwei der CPUs verlangen Dark Matter Plates, wie die letzte Stufe jeder Aufwertungskette: **Extra Slots CPU III** verlangt 4 (dazu 2 Ancient Control Units und 6 Orvium Reinforced Plates) und **Base CPU II** 4 (dazu eine Ancient Control Unit und 2 Orvium Reinforced Plates); erforsche also zuerst die Dark Matter Plate ([Dark Matter und Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md)).

<!-- research-cpus:begin -->
<!-- Generated from server/Resources/{Research,CpuConfig,SkylabConfig}.json and Data/Seeds/{items,recipes}.json by scripts/research-wiki.sh: don't edit by hand. -->

| CPU | Forschungsdauer | Braucht zuerst | Thulium zum Herstellen | Herstellungsdauer |
| :--- | :--- | :--- | ---: | ---: |
| [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30 min | – | 12.000 | 5 min |
| [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 10 h | [Extra Slots CPU I](/wiki/06-Items/Extras.md#extra-slots-cpus) | 30.000 | 10 min |
| [Extra Slots CPU III](/wiki/06-Items/Extras.md#extra-slots-cpus) | 1 d | [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate), [Extra Slots CPU II](/wiki/06-Items/Extras.md#extra-slots-cpus) | 75.000 | 15 min |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 3 h | – | 8.000 | 5 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 10 h | [Base CPU I](/wiki/06-Items/Extras.md#base-cpus), [Dark Matter Plate](/wiki/06-Items/Resources.md#dark-matter-plate) | 20.000 | 10 min |
| [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) | 1 d | [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 40.000 | 15 min |
| [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) | 6 h | – | 15.000 | 10 min |
| [Energetic Wall II](/wiki/06-Items/Extras.md#energetic-wall) | 6 h | – | 600 | 2 min |

Keine davon wird im Shop verkauft: Erforsche die Technologie und stelle die CPU dann in der Montage her. Zeige im Baum auf eine CPU, um zu sehen, was die Montage dafür verlangt.

### Extra Slots CPUs

- **Was sie tun.** Extra Slots CPU I, II und III geben jedem Schiff 3, 5 und 7 Extra-Slots mehr, also 6, 8 und 10 insgesamt bei einem Schiff mit 3 eigenen und 5, 7 und 9 bei einem mit 2. Eine höhere CPU ersetzt die vorige: II kommt nicht zu I dazu.
- **Installiert, nicht getragen.** Eine Extra Slots CPU ist kein Gegenstand: Holst du sie in der Montage ab, installiert sie sich in deinem Skylab, für jedes Schiff in beiden Konfigurationen, und sie belegt keinen Slot. Sie bleibt über den Wipe erhalten.
- **In Reihenfolge.** Stelle sie nacheinander her: II erst, wenn I installiert ist, III erst, wenn II installiert ist; bis dahin sagt dir die Montage, welche du zuerst installieren musst. Die drei kosten zusammen 117.000 Thulium: 12.000, 30.000 und 75.000.

### Jump CPU

- **Was sie tut.** Sie springt mit deinem Schiff in jeden Konzern-Sektor deiner Welt, den deines eigenen Konzerns wie die der anderen, deren Heimatsektoren eingeschlossen (`M`, `T` und `G`, Sektoren 1 bis 4), für **500 Thulium** pro Sprung. Sie hat keine Nutzungsgrenze: Du zahlst nur das Thulium. Sie führt nie in einen Gefahrensektor (`DS`) oder einen neutralen Sektor (`N`).
- **Der Sprung.** Drücke den Slot JMP, wähle den Sektor auf der Karte Sternensystem und bestätige: Das Schiff lädt 5 Sekunden lang auf und kommt dann an einem Tor dieses Sektors an, geschützt wie nach jedem Torsprung. Nach der Ankunft kühlt die CPU 30 Sekunden lang ab.
- **Nicht im Kampf.** Sie startet nicht innerhalb von 10 Sekunden nach einem Schuss oder Treffer, und ein Schuss oder Treffer beim Aufladen bricht den Sprung ab; dann wird nichts bezahlt. Getarnt kannst du nicht springen.
- **Nicht aus einem neutralen Sektor:** Ein Pilot in einem neutralen Sektor oder ohne Konzern kann sie nicht benutzen.
- Sie darf einen Gefahrensektor verlassen, wenn du nicht im Kampf bist.

### Base CPUs

- **Was sie tun.** Sie teleportieren dein Schiff zur Basis deines Konzerns, in die Schutzzone um die Station (`M-1`, `T-1` oder `G-1`, der Sektor mit Mission Control), ohne Thulium-Kosten. Du startest sie über den Slot BSE der Aktionsleiste.
- **Nicht im Kampf.** Eine Aufladung von 10 Sekunden, für beide gleich. Sie startet nicht innerhalb von 10 Sekunden nach einem Schuss oder Treffer, nicht getarnt und nicht, wenn du schon in der Schutzzone deiner Basis bist, und ein Schuss oder Treffer beim Aufladen bricht sie ab.

| CPU | Nutzungen | Abklingzeit |
| :--- | ---: | ---: |
| [Base CPU I](/wiki/06-Items/Extras.md#base-cpus) | 10 | 10 min |
| [Base CPU II](/wiki/06-Items/Extras.md#base-cpus) | 25 | 5 min |

- **Verbraucht, nicht aufgeladen.** Jede Nutzung nimmt der CPU eine ihrer Nutzungen, und eine CPU ohne verbleibende Nutzungen ist weg: Stelle eine neue her. Sind beide eingebaut, wird die bessere (II) zuerst verbraucht.

### Auto-Repair CPU

- **Was sie tut.** Sie schickt die Repair Drone aus deinen Extra-Slots von allein los, sobald du sie auch von Hand hättest losschicken können: Deine Hülle ist nicht voll, die Drohne ist nicht schon draußen und seit dem letzten Treffer sind 10 Sekunden vergangen. Eine Hüllengrenze musst du nicht einstellen.
- Sie belegt einen eigenen Extra-Slot und tut nichts ohne eine Repair Drone in einem Extra-Slot derselben Konfiguration. Eine Repair Drone in einem Fähigkeits-Slot schickt sie nie los (das ist die Schaltfläche Emergency Repair).
- **Stoppst du die Drohne von Hand,** lässt die CPU sie in Ruhe, bis deine Hülle wieder voll ist oder du die Drohne selbst losschickst.


<!-- research-cpus:end -->
