<!-- wiki-i18n source: 8e594dc8a7d6e482 -->
<!-- wiki-i18n title: Raketen -->
# Raketen {#rockets}

Raketen sind eine zweite Waffe neben deinen Lasern: ein Schuss alle paar Sekunden, der weit härter trifft als eine Lasersalve. Zwölf Raketen in vier Arten, je drei Stufen, zwei weitere, die nur die Montage herstellt, und **ein Nachladetimer von 5 Sekunden, den alle gemeinsam haben**, egal welche du abfeuerst. Die gewöhnlichen und seltenen Raketen kaufst du mit **Credits**, die vier epischen mit **Thulium**. Eine [Drohnenformation](/wiki/03-Mechanics/Formations.md) kann den Schaden einer Rakete erhöhen und den Timer länger oder kürzer machen: siehe [Drohnenformationen und Raketen](#drone-formations-and-rockets).

## In einer Minute {#in-one-minute}

- **Zwölf Raketen zum Kaufen.** Vier Arten (Lancet, Rivet, Ember, Scatter), je drei Stufen. Die gewöhnlichen und seltenen kosten Credits, die epischen Thulium. Zwei weitere Raketen, die N.U.K.E. und die N.I.K.E., stellt die Montage her.
- **Jede Rakete würfelt ihren Schaden.** Beim Abfeuern wählt das Spiel eine Zahl zwischen dem niedrigsten und dem höchsten Schaden der Rakete (eine Lancet I: 1.700 bis 2.100). Dein Schiff, deine Laser, Verstärker und Booster ändern nichts, nur eine Drohnenformation tut es. Die Raketen, die Aliens abfeuern, würfeln nicht: Sie richten eine feste Zahl an ([Gegen die Aliens](#against-the-aliens)).
- **Explosionen sind in der Mitte am stärksten.** Ember- und Scatter-Raketen explodieren und treffen jedes Schiff im Ring: die volle Zahl im Zentrum, die Hälfte davon am Rand.
- **Ein Timer für alle.** Nach jedem Abschuss wartest du 5 Sekunden bis zum nächsten, egal welche Rakete es ist.
- **Gelenkt oder geradeaus.** Eine gelenkte Rakete (Lancet, Ember) braucht ein Ziel, das du ausgewählt hast. Eine geradeaus fliegende (Rivet, Scatter) fliegt zu deinem Cursor.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
```
<!-- item-tree:end -->

## Die vier Arten {#the-four-kinds}

| | Einzelziel: trifft ein Schiff | Flächenschaden: platzt, trifft alles in der Nähe |
| :--- | :--- | :--- |
| **Gelenkt**: erfasst das gewählte Ziel und steuert ihm nach | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Geradeaus**: fliegt zu deinem Cursor | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Jede Art ist eine **Familie**, benannt nach ihrer gewöhnlichen Rakete, und die Stufe ist eine römische Ziffer: **Lancet I**, **Lancet II** und **Lancet III** sind die gewöhnliche, die seltene und die epische gelenkte Einzelziel-Rakete, und die Familien Rivet, Ember und Scatter folgen demselben Muster. Der Code einer Rakete auf ihrer Kachel in der Raketenauswahl und im Hangar besteht aus den drei Buchstaben ihrer Familie und ihrer Ziffer (LNC II, RVT III, EMB I, SCT II); die zwei Raketen, die es nur in der Montage gibt, behalten ihre Namen und Codes (N.U.K.E., NUK; N.I.K.E., NIK).

- **Gelenkte** Raketen brauchen beim Start ein gewähltes Ziel innerhalb ihrer **Aufschaltreichweite**. Sie steuern ihm mit begrenzter Wendigkeit nach, ein schnelles Schiff weit weg kann einer billigen also davonfliegen. Stirbt das Ziel, verlässt es die Karte oder erreicht es eine Schutzzone, fliegt die Rakete geradeaus weiter und sucht sich kein anderes.
- **Geradeaus** fliegende Raketen brauchen kein Ziel und ignorieren das gewählte: Sie fliegen immer zu deinem **Cursor**, zu dem Punkt darunter in der Flugansicht. **Klicke auf den Slot einer Geradeaus-Rakete, um sie scharf zu machen** (der Slot bekommt einen weißen Rahmen und ein Fadenkreuz, und dein Mauszeiger wird über dem Weltraum zum Fadenkreuz), dann **klicke in den Weltraum**: Die Rakete fliegt zu dem Punkt, den du angeklickt hast, und dein Schiff bleibt, wo es ist. Esc, ein Rechtsklick oder derselbe Slot noch einmal macht sie wieder unscharf. Laden die Raketen noch nach, sagt dir der Klick nur das, und die Rakete bleibt scharf. Die Zahlentasten und **Rakete feuern** feuern sofort zu dem letzten Punkt, den der Cursor in der Flugansicht hatte; war der Cursor noch nicht dort, fliegen sie in die Richtung, in die dein Schiff **zeigt**. Sie fliegen geradeaus, ein Schiff, das mit hoher Geschwindigkeit kreuzt, kann ihnen also ausweichen.
- Eine **Einzelziel**-Rakete trifft das erste Schiff, das sie treffen darf (eine gelenkte nur ihr Ziel). Eine **Flächenschaden**-Rakete explodiert neben dem ersten Schiff, auf das sie trifft, an dem Punkt, auf den du sie gerichtet hast, oder wo ihr Flug endet, und trifft jedes Schiff innerhalb ihres **Explosionsradius**: vollen Schaden im Zentrum, die Hälfte davon am Rand. Der Ring, den die Explosion auf der Karte zeichnet, ist ihre genaue Reichweite.
- **Asteroiden.** Eine Rakete, die auf einen [Asteroiden](/wiki/03-Mechanics/Asteroid-Mining.md) abgefeuert wird, trifft diesen Asteroiden und sonst nichts, und eine Rakete, die nicht auf einen abgefeuert wurde, fliegt durch jeden Asteroiden. Die zwölf Raketen des Shops und die N.U.K.E. können einen zerbrechen; die N.I.K.E. nicht.

## Die zwölf Raketen {#the-twelve-rockets}

Jede Rakete hat **ihren eigenen Schaden, der beim Abfeuern ausgewürfelt wird**: irgendwo zwischen ihrer niedrigsten und ihrer höchsten Zahl, und die Tabelle zeigt beide und den Durchschnitt. Er hängt nicht von deinem Schiff, deinen Lasern und deren Verstärkern, deinen Boostern, deiner Munition oder deinen Drohnen ab, und eine Rakete trifft nie kritisch. Nur eine **Drohnenformation** verändert ihn: Die Tabelle hier gibt den Schaden ohne Formation an (siehe [Drohnenformationen und Raketen](#drone-formations-and-rockets)). Eine Einzelziel-Rakete richtet den ausgewürfelten Schaden an dem Schiff an, das sie trifft; eine Explosion würfelt einmal und richtet das an **jedem Schiff darin** an, die ganze Zahl im Zentrum und die Hälfte davon am Rand. Die *Schilddurchdringung* wird für diesen Treffer von der Absorption deines Ziels abgezogen (die Absorption eines Schiffs ist der Anteil eines Treffers, den seine Schilde nehmen, siehe [Schildmechanik](/wiki/03-Mechanics/Shields.md#shield-penetration)): Die 35 % einer Lancet III lassen den Schilden eines Schiffs mit 80 % 45 % des Treffers und schicken die anderen 55 % in die Hülle. Eine Explosion hat keine.

| Name | Art | Seltenheit | Schaden | Durchschnitt | Schilddurchdringung | Explosionsradius | Aufschaltreichweite | Reichweite | Geschwindigkeit | Preis | Maximal tragbar |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Gelenkt, Einzelziel | Gewöhnlich | 1.700–2.100 | 1.900 | 10 % | – | 700 | 1.040 | 520 | 500 Credits | 5.000 |
| **Lancet II** | Gelenkt, Einzelziel | Selten | 3.500–4.200 | 3.850 | 25 % | – | 1.000 | 1.584 | 660 | 800 Credits | 2.000 |
| **Lancet III** | Gelenkt, Einzelziel | Episch | 5.200–6.200 | 5.700 | 35 % | – | 1.300 | 2.296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Geradeaus, Einzelziel | Gewöhnlich | 2.200–2.700 | 2.450 | 5 % | – | – | 1.080 | 900 | 500 Credits | 5.000 |
| **Rivet II** | Geradeaus, Einzelziel | Selten | 4.500–5.250 | 4.875 | 25 % | – | – | 1.120 | 700 | 800 Credits | 2.000 |
| **Rivet III** | Geradeaus, Einzelziel | Episch | 7.000–8.000 | 7.500 | 35 % | – | – | 1.100 | 500 | 5 Thulium | 500 |
| **Ember I** | Gelenkt, Flächenschaden | Gewöhnlich | 1.200–1.400 | 1.300 | – | 170 | 700 | 1.000 | 500 | 500 Credits | 5.000 |
| **Ember II** | Gelenkt, Flächenschaden | Selten | 2.400–2.900 | 2.650 | – | 230 | 920 | 1.500 | 600 | 800 Credits | 2.000 |
| **Ember III** | Gelenkt, Flächenschaden | Episch | 3.500–4.500 | 4.000 | – | 300 | 1.150 | 2.030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Geradeaus, Flächenschaden | Gewöhnlich | 1.500–1.750 | 1.625 | – | 210 | – | 1.088 | 640 | 500 Credits | 5.000 |
| **Scatter II** | Geradeaus, Flächenschaden | Selten | 3.000–3.500 | 3.250 | – | 290 | – | 1.080 | 540 | 800 Credits | 2.000 |
| **Scatter III** | Geradeaus, Flächenschaden | Episch | 4.500–5.500 | 5.000 | – | 400 | – | 1.092 | 420 | 5 Thulium | 500 |

Je teurer die Stufe, desto härter trifft eine Rakete, desto weiter reicht sie, desto mehr Schilddurchdringung hat sie und desto weniger kannst du tragen; die teuren geben auch den meisten Schaden für ihren Preis. Eine Geradeaus-Rakete richtet für denselben Preis ein Viertel bis ein Drittel mehr Schaden an als die gelenkte Rakete ihrer Stufe und Art (23 bis 32 % im Schnitt), weil du zielen musst. Eine Flächenschaden-Rakete richtet etwa zwei Drittel der Einzelziel-Rakete ihrer Stufe und Art an (66 bis 70 % im Schnitt: eine Ember gegenüber einer Lancet, eine Scatter gegenüber einer Rivet), an jedem Schiff, das sie erfasst. Im Zentrum einer Explosion ist der Schaden voll und fällt in einer geraden Linie auf **die Hälfte davon am Rand**: Ein Schiff, dessen Hülle auf halbem Weg zum Rand liegt, nimmt 75 %, eines mit der Hülle außerhalb des Rings nichts. Ein Schuss richtet im Schnitt die Mitte seines Bereichs an, 89 bis 94 % seiner Höchstzahl; die Tabelle unten, die Raketen zählt, rechnet damit.

## Was sie kosten {#what-they-cost}

Eine gewöhnliche Rakete kostet 500 Credits, eine seltene 800 Credits und eine epische 5 Thulium, in jeder Art. Bei jedem Timer abgefeuert sind das 6.000 Credits pro Minute für eine gewöhnliche Rakete, 9.600 für eine seltene und 60 Thulium für eine epische, gegenüber den 1.800 Credits pro Minute, die die drei Laser einer Ostirion bei x1 verbrennen. Ein voller Vorrat sind 5.000 gewöhnliche Raketen (2.500.000 Credits), 2.000 seltene (1.600.000 Credits) oder 500 epische (2.500 Thulium): Du kaufst so viele, wie du willst, bis zu dieser Zahl, und die *maximal tragbare Menge* einer Rakete ist die einzige Grenze dafür, wie viele du hältst. Raketen wiegen nichts: Sie nehmen im Transport-Cache keinen Platz ein. Eine Rakete alle 5 Sekunden sind nur zwölf pro Minute, eine Rakete ist also der Burst obendrauf zu deinen Lasern: die billigen für die schwachen Aliens, die teuren für die großen Kämpfe. Was du in der [Auktion](/wiki/03-Mechanics/Auction.md#limits) eingestellt hast und die Lose, die du dort anführst, zählen zu diesem Limit, wenn du eine Rakete kaufst oder auf sie bietest.

Der Shop listet die Raketen Art für Art auf, jede unter ihrem Namen, die gewöhnliche zuerst und die epische zuletzt; der Hangar, der Transport-Cache und die Raketenauswahl nutzen dieselbe Reihenfolge.

## Gegen die Aliens {#against-the-aliens}

Die Raketen, die man braucht, um ein Alien abzuschießen, eine Raketenart nach der anderen, jede Rakete würfelt den Durchschnitt ihres Bereichs (Alpha; Aliens in Beta und Gamma sind 1,5- und 2-mal so stark). Eine Explosion zählt so, wie das Schiff sie abbekommt, neben dem sie platzt, knapp vor dem Zentrum (87 bis 93 % des Schadens im Zentrum). Der Schild eines Aliens nimmt 80 % eines Treffers, abzüglich der Schilddurchdringung der Rakete. Beim niedrigsten Wurf braucht ein Abschuss bis zu 15 % mehr Raketen, als die Tabelle sagt (eine Lancet I braucht 48 für einen Goombah, nicht 43), beim besten bis zu 13 % weniger (39). Eine Rivet II, eine Lancet III und eine Rivet III zerstören einen Phantasm bei jedem Wurf mit einem Treffer; eine Rivet I braucht bei einem Wurf ab 2.600 zwei und darunter drei.

| Raketen bis zum Abschuss | Seeker (1.600) | Phantasm (5.200) | Bulwark (26.000) | Goombah (80.000) | Crystalys (416.000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 14 | 43 | 219 |
| **Lancet II** | 1 | 2 | 7 | 19 | 109 |
| **Lancet III** | 1 | 1 | 5 | 11 | 73 |
| **Rivet I** | 1 | 3 | 11 | 33 | 170 |
| **Rivet II** | 1 | 1 | 6 | 15 | 86 |
| **Rivet III** | 1 | 1 | 4 | 8 | 56 |
| **Ember I** | 2 | 5 | 24 | 71 | 369 |
| **Ember II** | 1 | 3 | 12 | 34 | 177 |
| **Ember III** | 1 | 2 | 8 | 23 | 116 |
| **Scatter I** | 2 | 4 | 18 | 56 | 287 |
| **Scatter II** | 1 | 2 | 9 | 27 | 141 |
| **Scatter III** | 1 | 2 | 6 | 18 | 90 |

- Die **gewöhnlichen** Einzelziel-Raketen schießen einen Seeker bei jedem Wurf mit einem Treffer und einen Phantasm mit dreien ab (eine Lancet I braucht bei ihrem niedrigsten Wurf einen vierten); sie sind die Alltagsraketen der ersten Sektoren. Die **seltenen** sind für den Bulwark und den Goombah: Sieben Lancet-II-Raketen brauchen für einen Bulwark etwa 30 Sekunden Timer. Die **epischen** Einzelziel-Raketen schießen einen Goombah mit acht (Rivet III) bis elf (Lancet III) ab. Die Flächenschaden-Raketen sind ihren Preis wert, wenn mehrere Aliens dicht beieinander stehen: Eine Scatter III, die über einem Rudel aus fünf Phantasms platzt (alle innerhalb von 250 Einheiten um das Ziel, auf das du gezielt hast), richtet auf einen Schlag etwa 21.000 Schaden im Rudel an.
- Ein Abschuss allein mit Raketen ist eine echte Ausgabe, kein Weg zum Reichtum: Eine Einzelziel-Rakete kostet zwischen 15 % (eine Rivet II bei einem Phantasm) und 95 % (eine Lancet I bei einem Crystalys) dessen, was der Abschuss zahlt (Credits, und Thulium zu je 200 Credits), und die schwachen Flächenschaden-Raketen kosten bei den starken Aliens mehr, als der Abschuss zahlt (eine Ember I bei einem Bulwark: 120 %). Den **Crystalys** allein mit einer Raketenart abzuschießen, braucht 56 bis 369 Raketen und mindestens viereinhalb Minuten Timer; ein voller Vorrat von 500 epischen Raketen reicht für vier bis acht davon. Das stärkste Alien braucht einen Plan: deine Laser mit x2-Munition, eine Rakete mittlerer Stufe alle 5 Sekunden ab der ersten Sekunde und die großen Raketen unten als Burst.
- Der Lohn eines Abschusses ist derselbe, egal wie er erzielt wurde (den größten findest du auf der Seite des [Crystalys](/wiki/04-Aliens/Crystalys.md)), ein Raketenabschuss lohnt sich also, wenn er dir Zeit spart und weniger kostet, als er zahlt.
- **Auch Aliens feuern Raketen.** Der Pirate Boss sowie die Dormant Force und die Pulses der [Schwärme](/wiki/05-Swarms/Swarms.md) und die Siege Wardens der [Clans](/wiki/03-Mechanics/Clans.md#clan-wardens) schießen gerade Rivet-Raketen auf den Piloten, der sie angegriffen hat, mit demselben 5-Sekunden-Timer. **Die Rakete eines Aliens würfelt nicht und nutzt nicht die Bereiche oben**: Sie richtet feste 2.500 (Rivet I), 5.000 (Rivet II) oder 7.500 (Rivet III) an, in Beta und Gamma mehr, wo Aliens 1,5- und 2-mal so stark sind (die Rakete eines Clan Wardens ist in jeder Welt dieselbe). Ein Schiff, das in Bewegung bleibt, weicht ihnen aus. Die Bosse der Schwärme lassen in ihren Kisten außerdem Raketen fallen.

## Die nur herstellbaren Raketen {#the-craft-only-rockets}

Zwei Raketen gibt es nicht im Shop. Die **Montage** stellt sie her, und für sie gelten alle Regeln unten (der gemeinsame Timer, Schutzzonen, dein Konzern). Beide sind Geradeaus-Raketen: Sie fliegen zu dem Punkt unter deinem Cursor, wie jede Geradeaus-Rakete (das Spiel sendet die Richtung des Cursors, egal was du gewählt hast; nur ein alter 0.4.3-Client, der keine Richtung sendet, lässt den Server sie auf das gewählte Ziel fliegen, sonst auf den Punkt unter seinem Cursor, sonst in die Richtung, in die das Schiff zeigt). Sie würfeln zwischen **90 % und 100 %** ihrer Höchstzahl, ein engeres Band als das der zwölf, sodass das, was sie unten mit einem Treffer zerstören, auch beim niedrigsten Wurf gilt.

| Name | Art | Seltenheit | Schaden | Schilddurchdringung | Explosionsradius | Reichweite | Geschwindigkeit | Maximal tragbar | Hergestellt aus |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Geradeaus, Flächenschaden | Legendär | 45.000–50.000 | – | 900 | 1.200 | 300 | 10 | 1 N.U.K.E. pro Herstellung: 150.000 Credits, 3.000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Geradeaus, Einzelziel | Mythisch | 67.500–75.000 | 35 % | – | 4.050 | 900 | 20 | 5 N.I.K.E. pro Herstellung: 100.000 Credits, 1.500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: die größte Explosion im Spiel. Eine Explosion von 900 Einheiten, die doppelte Reichweite der 400 der Scatter III und das Fünffache ihrer Fläche: 45.000 bis 50.000 an jedem Schiff darin im Zentrum, zum Rand hin fallend auf die Hälfte davon, 22.500 bis 25.000. Sie ist langsam (vier Sekunden im Flug). Eine N.U.K.E. löscht jeden Seeker und Phantasm in ihrer gesamten Explosion aus, dazu einen Bulwark innerhalb von 830 Einheiten um die Detonation (934 beim besten Wurf), fast die ganze Explosion; sie nimmt mehr als die Hälfte eines Goombah und ein Neuntel eines Crystalys. Gegen Piloten ist sie der größte Treffer, den es gibt: siehe die Regeln unten. Der Ring auf der Karte ist ihre genaue Reichweite.
- **N.I.K.E.**: eine Einzelziel-Rakete wie eine Rivet I, mit 67.500 bis 75.000 Schaden und einer Schilddurchdringung von 35 %: **Sie trifft das erste Schiff, das sie berührt, und ist darin aufgebraucht.** Sie ist auch die Rakete, die [Dark Matter](/wiki/03-Mechanics/Black-Hole.md) erzeugt: Auf das Schwarze Loch in der Mitte von Gefahrensektor 4 abgefeuert, wird sie verschluckt, wenn sie den Ereignishorizont überquert, und das Loch gibt Dark Matter zurück. Sie fliegt 4.050 Einheiten in 4,5 Sekunden: Feuere sie von irgendwo zwischen dem Rand der Strahlung und 4.380 Einheiten vom Zentrum ab. Von weiter draußen bleibt sie zu kurz und ist verschwendet. Fünf N.I.K.E.s ergeben etwa zehn Dark Matter.
- **Der Haken.** Eine N.I.K.E., die unterwegs auf ein Schiff trifft, einen Rivalen, der auf der Schusslinie wartet, oder irgendetwas anderes, das sie verletzen darf, trifft es mit 67.500 bis 75.000 und ist weg: Das Schwarze Loch bekommt nichts, und du auch nicht. Sonst streift nichts im Ring des Lochs umher, was sie versehentlich treffen könnte (Aliens und Konzernpiloten halten sich fern): nur Piloten, die für Dark Matter hineingeflogen sind oder am Rand auf dich warten. Sie fliegt durch deinen eigenen Konzern, durch Schiffe in einer Schutzzone und durch Schiffe, die du noch nicht verletzen darfst. Verlässt du die Karte nach dem Abfeuern, fliegt sie weiter, ohne jemanden zu verletzen, und erzeugt trotzdem dein Dark Matter.
- Die Montage startet keine Herstellung, nach der du mehr als die *maximal tragbare Menge* einer Rakete halten würdest, eingereihte Aufträge mitgezählt.

## Abfeuern {#firing}

1. Kaufe Raketen im Shop (die Kategorie **Raketen**), bis zur *maximal tragbaren Menge* jeder: Credits für die gewöhnlichen und seltenen, Thulium für die epischen.
2. Öffne **Raketen** über der Aktionsleiste und ziehe die gewünschten auf Slots. Die Auswahl zeigt eine Spalte pro Art und eine Zeile pro Stufe, mit dem, was du von jeder trägst. Darunter liegt eine eigene Zeile, **Spezial · nur Montage**, für die N.U.K.E. und die N.I.K.E. (ein kleiner Hammer markiert die, von der du keine trägst).
3. Drücke die Taste des Slots. Ein Klick auf den Slot einer **gelenkten** Rakete feuert sie auf dein gewähltes Ziel ab; ein Klick auf den Slot einer **Geradeaus**-Rakete macht sie scharf, und dein nächster Klick in den Weltraum feuert sie dorthin ab. Die Taste **Rakete feuern** (standardmäßig `R`, in Einstellungen › Steuerung neu belegbar) feuert die Rakete, die du zuletzt abgefeuert hast, oder die erste auf der Leiste.
4. Ein Ladekreis läuft über **jeden** Raketen-Slot, für die 5 Sekunden bis zum nächsten Start, mit den verbleibenden Sekunden in der Mitte. Ein Druck davor sagt dir nur, dass die Raketen nachladen (ein Druck in der letzten Zehntelsekunde feuert trotzdem). Eine Drohnenformation kann die Wartezeit auf 3,65 bis 6,75 Sekunden bringen (siehe unten).

Fahre mit der Maus über einen Raketen-Slot, um seine Zahlen zu sehen (ihr niedrigster und höchster Schaden; der Shop und der Hangar nennen dasselbe) und in der Welt ihren Aufschaltring (grün, wenn das gewählte Ziel in Reichweite ist) oder ihre Linie und ihren Explosionskreis. Eine Rakete, die auf **dich** aufgeschaltet ist, lässt den Rand deines Bildschirms rot aufblitzen.

Die **N.U.K.E.** zeichnet ihre Explosion auf der Karte, bevor du feuerst (den Kreis von 900 Einheiten am Zielpunkt), und wenn sie losgeht, einen weißen Blitz über der Ansicht, einen Ring, der in etwa einer Sekunde bis zur genauen Reichweite hinausläuft und zwei weitere stehen bleibt, eine Wolke, die wie ein Pilz aufsteigt, und ein Beben der Kamera, das umso stärker ist, je näher du bist. **Bildschirmwackeln reduzieren** entfernt das Beben, und **Bewegung reduzieren** verkürzt den Blitz auf eine Drittelsekunde mit weniger als der Hälfte seines Lichts (beides in den Einstellungen unter Grafik); eine niedrigere Partikelqualität dünnt die Wolke aus und lässt die Funken weg, nie den Blitz oder den Ring. Die **N.I.K.E.** wird wie eine Rivet I gezielt, über die Linie von deinem Schiff zum Cursor, und das Spiel verweigert sie nie, weil du weit vom Schwarzen Loch entfernt bist oder auf einer Karte ohne ein solches: Wohin sie fliegt, beurteilst du selbst. Ihre Karte zeigt neben ihrem Schaden **Schwarzes Loch: Erzeugt Dark Matter**. Sie hinterlässt eine violette Spur, um die sich Funken winden; ein Schiff, auf das sie trifft, nimmt den Treffer wie von jeder Rakete, und überquert sie stattdessen den Horizont, flammt das Loch auf.

## Drohnenformationen und Raketen {#drone-formations-and-rockets}

Eine getragene [Drohnenformation](/wiki/03-Mechanics/Formations.md) ist das Einzige, was eine Rakete verändert. Alle Schadenszahlen auf dieser Seite gelten für ein Schiff ohne Formation.

- **Schaden.** Der Raketenbonus von Ballista (+55 %), Bodkin (+29 %) und Asterism (+24 %) multipliziert den Schaden aller 14 Raketen, auch von N.U.K.E. und N.I.K.E. Testudos Preis auf allen Schaden zählt bei Raketen, und Cullers Schaden gegen Aliens zählt bei einer Rakete, die ein Alien trifft. Alle Faktoren einer Rakete zusammen enden bei ×1,59.
- **Nachladen.** Asterism macht den gemeinsamen Timer um 35 % länger (6,75 Sekunden), Cordon um 11 % länger (5,55) und Redoubt um 27 % kürzer (3,65), aber nie kürzer als der Flug der Rakete plus ein Moment: 4,1 Sekunden nach einer N.U.K.E. und 4,6 nach einer N.I.K.E. Die Wartezeit steht beim Abfeuern fest, ein späterer Formationswechsel verkürzt sie also nicht, und der Ladekreis über den Raketen-Slots folgt ihr.
- **Die Grenzen der beiden Großen halten.** Mit der besten Formation trifft eine N.I.K.E. mit bis zu 116.250, was ein frischer Paragon (128.000) überlebt, und eine N.U.K.E. mit bis zu 77.500, was ein Goombah (80.000) überlebt.
- **Ausweichen.** Asterisms 7 % Ausweichen geben einer direkten Rakete, die dich trifft, eine Chance von 7 %, gar keinen Schaden anzurichten, und über deinem Schiff erscheint ein schwebendes „Verfehlt“; eine Flächenexplosion zielt nicht und wird nie abgewehrt.
- **Durchdringung.** Gemini und Stiletto addieren ihre Punkte zur Schilddurchdringung einer direkten Rakete (eine Explosion hat keine), insgesamt bis zu 40 %. Ein Lasertreffer geht bis zu 50 % ([Laser & Munition](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

## Regeln {#rules}

- Du brauchst **keinen ausgerüsteten Laser**, um eine Rakete abzufeuern, und deine Laser ändern weder ihren Schaden noch ihre Reichweite: Eine gelenkte Rakete erfasst ein Ziel innerhalb ihrer eigenen Aufschaltreichweite, eine Geradeaus-Rakete fliegt ihre eigene Strecke. Ist kein Laser ausgerüstet, zeigt die Kachel „Reichweite“ im Hangar einen Strich, und nur deine Raketen feuern.
- Pro Start wird eine Rakete verbraucht, ob sie trifft oder nicht.
- Raketen folgen den Regeln der Laser: Nichts in einer **Schutzzone** wird verletzt, kein Pilot wird verletzt, bevor das **Friedensprotokoll** endet oder wo ein Sektor PvP verbietet, und **dein eigener Konzern und deine eigene Gruppe werden von deinen Raketen nie verletzt**, weder durch Direkttreffer noch durch Explosion.
- Das Abfeuern einer Rakete beendet deinen eigenen Schutzzonen-Schutz sofort. Es ist ein Schuss: Es beendet auch deine eigene **Tarnung**, und die Cloaking CPU lädt sich dann eine Minute lang auf, wie nach jedem Ende einer Tarnung. Getarnt oder nicht, ein Start hindert dich in den 10 Sekunden danach daran, dich zu tarnen (siehe [Extras](/wiki/06-Items/Extras.md)).
- Ein Schiff, das **getarnt** ist oder sich in den **3 Sekunden seines EMP** befindet, kann nicht anvisiert werden: Eine gelenkte Rakete wird abgewiesen, und eine, die schon auf es zufliegt, verliert die Zielerfassung und fliegt geradeaus weiter. Eine geradeaus fliegende Einzelziel-Rakete fliegt durch ein solches Schiff hindurch. Ein **Flächenschaden** braucht keine Zielerfassung, er trifft die Schiffe, die er erfasst, also getarnt oder nicht, und beendet eine Tarnung (siehe [Extras](/wiki/06-Items/Extras.md)).
- **Nichts begrenzt, was eine Rakete einem Piloten antut.** Das Schiff eines anderen Piloten nimmt den vollen Schaden: zuerst den Schild (seine Absorption abzüglich der Schilddurchdringung der Rakete), dann die Hülle. Die kleinen Schiffe halten nicht lange durch. Auf den serienmäßigen Schilden (Light, 45 % Absorption) zerstört eine N.I.K.E. bei jedem Wurf eine frische Protos, Kitefin oder Ostirion mit einem Treffer (eine Paragon verliert 47 bis 53 % ihrer Hülle, eine Wraith etwa ein Fünftel), und eine N.U.K.E. zerstört eine Protos überall in ihrer Explosion, eine Kitefin innerhalb von etwa 50 Einheiten um die Detonation (beim besten Wurf 220) und nichts Größeres mit einer Explosion. Zwei Lancet-III-Raketen oder zwei Rivet-III-Raketen zerstören bei jedem Wurf eine Protos; eine Wraith braucht zwischen 45 und 70 davon. Das Friedensprotokoll, die Schutzzonen und dein Konzern sind das, was zwischen einem Piloten und einer Rakete steht. Diese Zahlen gelten für ein Schiff ohne Formation; eine Raketenformation erhöht sie um bis zu 55 % (siehe [Drohnenformationen und Raketen](#drone-formations-and-rockets)).
- Nur der **Direkttreffer** einer Rakete beansprucht ein Alien (siehe [Kampf](/wiki/03-Mechanics/Combat.md)); der Rand einer Explosion kann ein beanspruchtes Alien verletzen, ohne es zu stehlen. Jedes Alien, das eine Explosion verletzt, auch ein schlafendes, wendet sich gegen dich, wie bei einem Lasertreffer (ein Seeker oder ein Goombah, die nur zurückschlagen, eingeschlossen); eines, das die Explosion verfehlt, bleibt schlafen.
- Der Timer gehört dir: Er übersteht einen Sprung, ein erneutes Verbinden, einen Schiffswechsel und ein zerstörtes Schiff.

Die zwölf Raketen der ersten Tabelle werden gekauft (Credits für die gewöhnlichen und seltenen, Thulium für die epischen); die N.U.K.E. und die N.I.K.E. werden hergestellt.

Siehe auch: [Laser & Munition](/wiki/06-Items/Lasers.md), [Kampf](/wiki/03-Mechanics/Combat.md), [Das Schwarze Loch](/wiki/03-Mechanics/Black-Hole.md).
