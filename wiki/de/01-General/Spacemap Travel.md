<!-- wiki-i18n source: 6ad05a3dc7e0e2f6 -->
<!-- wiki-i18n title: Reisen im All -->
# Reisen auf der Weltraumkarte {#spacemap-travel}

Die Weltraumkarte ist deine Navigationsoberfläche für die Reise durch das SpaceCorps-Universum. Jeder Konzern kontrolliert einen Teil des Weltraums, angeordnet in einer bestimmten Topologie, die sowohl sichere Erkundung als auch gefährliche PvP-Begegnungen ermöglicht.

![Galaxy Gates](../../img/wiki-img/shots/gates.jpg)
![Sector DS-1 as the game draws it](../../img/wiki-img/shots/sector-DS-1.jpg)
![Sector DS-2 as the game draws it](../../img/wiki-img/shots/sector-DS-2.jpg)
![Sector DS-3 as the game draws it](../../img/wiki-img/shots/sector-DS-3.jpg)
![Sector DS-4 as the game draws it](../../img/wiki-img/shots/sector-DS-4.jpg)
![Sector G-1 as the game draws it](../../img/wiki-img/shots/sector-G-1.jpg)
![Sector G-2 as the game draws it](../../img/wiki-img/shots/sector-G-2.jpg)
![Sector G-3 as the game draws it](../../img/wiki-img/shots/sector-G-3.jpg)
![Sector G-4 as the game draws it](../../img/wiki-img/shots/sector-G-4.jpg)
![Sector M-1 as the game draws it](../../img/wiki-img/shots/sector-M-1.jpg)
![Sector M-2 as the game draws it](../../img/wiki-img/shots/sector-M-2.jpg)
![Sector M-3 as the game draws it](../../img/wiki-img/shots/sector-M-3.jpg)
![Sector M-4 as the game draws it](../../img/wiki-img/shots/sector-M-4.jpg)
![Sector T-1 as the game draws it](../../img/wiki-img/shots/sector-T-1.jpg)
![Sector T-2 as the game draws it](../../img/wiki-img/shots/sector-T-2.jpg)
![Sector T-3 as the game draws it](../../img/wiki-img/shots/sector-T-3.jpg)
![Sector T-4 as the game draws it](../../img/wiki-img/shots/sector-T-4.jpg)
![The Star System map: the sectors, the PvP sectors, the gates and the company routes, with the portal ring that joins each company's x-4 sector to the next company's x-3 sector](../../img/wiki-img/shots/star-system.jpg)

## Der Aufbau des Universums {#the-universe-structure}

Das Universum besteht aus den drei großen Konzernsektoren (Mars, Terra, Galactic) und einer zentralen PvP-Zone.

- **x-1 (Heimatbasis)**: Die Startkarte jedes Konzerns (M-1, T-1, G-1). Die sicherste Zone.
- **x-2 -> x-3**: Expansionszonen mit immer stärkeren Aliens.
- **x-4 (Grenze)**: Das Tor zum PvP-Sektor und zu `x-3` eines anderen Konzerns (der Ring, siehe unten).
- **DS-x (Gefahrensektoren)**: Die zentrale PvP-Zone, die alle Konzerne verbindet: DS-1 bis DS-4.

Nur die Heimatbasen haben eine Station. Dort öffnet sich **Mission Control**, und ihre Schutzzone reicht 1.600 Einheiten weit um sie herum. Die Gefahrensektoren haben keine Station, auch `DS-1` nicht: Die einzigen Schutzzonen dort sind die Ringe von 660 Einheiten um die Sprungtore, und Mission Control lässt sich dort nicht öffnen; fliege für deine Missionen zurück zu deiner Basis.

Jede [Welt](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) (Alpha, Beta, Gamma) hat ihre eigene Kopie dieser ganzen Karte, und wo Piloten gegeneinander kämpfen dürfen, hängt von ihr ab: in Alpha nur in `x-4` und `DS-x`, in Beta überall außer in `x-1`, in Gamma überall. Die Galaxiekarte färbt die Sektoren nach der Regel deiner Welt.

## Visualisierung {#visualization}

Die Galaxiekarte unten zeigt den Aufbau des bekannten Universums in Echtzeit. Im Spiel ist dieselbe Karte das Fenster **Sternensystem**.

```spacemap

```

Ist eine [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) ausgerüstet, wählt die Karte auch dein Ziel: Drücke den Slot der CPU in der Aktionsleiste (**JMP**), und das Fenster Sternensystem öffnet sich im Auswahlmodus. Die Sektoren, zu denen dich die CPU bringen kann, leuchten; dein eigener Sektor und die Gefahrensektoren nicht. Zeige auf einen leuchtenden Sektor, um den Preis zu lesen, klicke ihn an und bestätige den Sprung, wenn die Karte danach fragt (500 Thulium).

## So reist du {#how-to-travel}

Auf der Weltraumkarte reist du über **Sprungtore** (Portale). Die [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) ist der andere Weg: Sie braucht kein Tor (siehe das Ende dieser Seite).

1. **Portal finden**: Portale liegen meist in den Ecken oder an den Rändern einer Karte.
2. **Navigation**: Flieg mit deinem Schiff nah an das Portal heran.
3. **Aktivierung**: Drücke **'J'** im Umkreis von 500 Einheiten um das Portal, um den Sprung zu starten.
4. **Abwarten**: Der Sprung **dauert 3 Sekunden**. Währenddessen füllt sich ein Balken über deiner Aktionsleiste („Springe…“), und das Portal leuchtet heller, während es sich auflädt; andere Piloten sehen dieselbe Aufladung am Portal, wenn du springst. Dein Schiff fliegt weiter, aber du musst bis zum Ende der Zeit im Umkreis von 500 Einheiten um das Portal bleiben: Fliegst du aus der Reichweite, wird der Sprung abgebrochen („Das Portal ist zum Springen zu weit entfernt.“, und der Balken wird rot). Drückst du während des Sprungs noch einmal **'J'**, passiert nichts, außer dass dir das Spiel genau das sagt.
5. **Ziel**: Du kommst am zugehörigen Portal der Zielkarte an.

### Springen unter Beschuss {#jumping-under-fire}

- **Außerhalb der Gefahrensektoren** unterbricht ein Angriff, ob von Aliens oder von anderen Piloten, deinen Sprung **nicht**: Er wird abgeschlossen.
- **In den Gefahrensektoren (`DS-1` bis `DS-4`)** kannst du nicht hinausspringen, solange du angegriffen wirst. Hat ein Pilot oder ein Alien dein Schiff (seine Schilde oder seine Hülle) in den letzten **10 Sekunden** getroffen, startet der Sprung nicht („Du wirst angegriffen: Aus einem Gefahrensektor kannst du nicht springen.“), und ein Treffer während des Sprungs bricht ihn ab (der Balken wird rot, und das Spiel sagt dir, warum). Schaden durch die Strahlung des Schwarzen Lochs ist kein Angriff, ebenso wenig ein Schuss, den eine Schutzzone abgefangen hat. Ein Treffer, den du auf der Karte eingesteckt hast, von der du gesprungen bist, folgt dir nicht durch das Portal: Du kommst mit weißer Weste an.
- Du tust eins nach dem anderen: Während eines Sprungs kannst du keine [Frachtkiste](/wiki/03-Mechanics/Cargo.md) einsammeln, und wer einen Sprung startet, bricht ein begonnenes Einsammeln ab.
- Schließt du das Spiel oder kehrst du mitten im Sprung zur Basis zurück, wird er abgebrochen: Du kommst nicht an.
- **Der Warp einer CPU lädt wie ein Portalsprung.** Eine Jump CPU lädt 5 Sekunden lang und eine Base CPU 10, mit einem Balken über der Aktionsleiste. Ein Schuss, den du abgibst, oder ein Treffer, den du einsteckst, bricht den Warp in jedem Sektor ab (nichts wird bezahlt oder verbraucht), und keine der beiden CPUs startet innerhalb von 10 Sekunden nach einem Schuss oder Treffer. Drücke den Slot der CPU noch einmal, um ihn selbst abzubrechen.

### Sprungverbindungen {#jump-links}

- **Die Konzernschleife**: Mars, Terra und Galactic sind gleich aufgebaut. Die Verbindungen laufen `1 <-> 2 <-> 3` sowie `2 <-> 4` und `3 <-> 4`. So entsteht eine Schleife zwischen den Nebenkarten (`x-2` und `x-3`) und der Grenzkarte (`x-4`), während `x-1` als sicherer Einstiegspunkt am Ende hängt und nur mit `x-2` verbunden ist: Deine Startkarte hat nur ein Portal.
- **Zugangstore zu den Gefahrensektoren**: Die Grenzkarte (`x-4`) jedes Konzerns ist direkt mit seinem eigenen Gefahrensektor verbunden:
  - `M-4` ist mit `DS-1` verbunden
  - `T-4` ist mit `DS-2` verbunden
  - `G-4` ist mit `DS-3` verbunden
- **Der Ring**: Die Grenzkarte (`x-4`) jedes Konzerns hat ein weiteres Tor, und zwar zu `x-3` des **nächsten Konzerns**; jedes `x-3` hat das Tor zurück. Die drei Verbindungen bilden einen Ring um die Gefahrensektoren, sodass jeder Konzern einen Weg hinaus und einen Weg hinein hat:
  - `M-4` ist mit Terras `T-3` verbunden
  - `T-4` ist mit Galactics `G-3` verbunden
  - `G-4` ist mit Mars’ `M-3` verbunden

  Der Ring steht jedem Piloten offen, für welchen Konzern er auch fliegt: Er ist ein zweiter Reiseweg zwischen den Karten der Konzerne, der die PvP-Zone nicht durchquert. Ein Ringtor steht in einer eigenen Ecke, abseits der anderen Tore seiner Karte, mit der üblichen Schutzzone von 660 Einheiten um sich, und der Sprung funktioniert wie an jedem Tor. Wo du auf der anderen Seite angegriffen werden darfst, hängt wie überall von deiner Welt ab: In Alpha ist `T-3` kein PvP-Sektor, `T-4` aber schon, in Beta sind es beide, in Gamma jeder Sektor.
- **Invasionsrouten (Reisen zwischen Konzernen)**: Es gibt zwei Wege durch die Tore in das Gebiet eines anderen Konzerns. Der kurze ist der Ring: Ein Mars-Pilot fliegt von `M-4` durch das Ringtor in Terras `T-3` (drei Sprünge von der Mars-Basis aus, `M-1` → `M-2` → `M-4` → `T-3`) und weiter nach `T-4` oder `T-2`; Galactics `G-4` führt ebenso in Mars’ `M-3` und Terras `T-4` in Galactics `G-3`. Der lange Weg durchquert die PvP-Zone: von `M-4` in den Gefahrensektor `DS-1`, durch das Sprungtor nach `DS-2` und über `T-4` in den Terra-Raum; um Galactic zu erreichen, wechselt man durch das Sprungtor nach `DS-3` und dringt über `G-4` ein.
- **Das Gefahrensektor-Dreieck**: `DS-1`, `DS-2` und `DS-3` sind alle miteinander verbunden. Jeder von ihnen hat das Tor eines Konzerns (Mars in `DS-1`, Terra in `DS-2`, Galactic in `DS-3`); `DS-4` hat keines.
- **Das Zentrum**: Alle drei äußeren Gefahrensektoren (`DS-1`, `DS-2` und `DS-3`) sind direkt mit der Zentralkarte **`DS-4`** verbunden, der gefährlichsten und lohnendsten PvP-Zone des Universums. Genau in ihrer Mitte hängt ein **Schwarzes Loch**: Die Portale und die Flugrouten zwischen ihnen halten großen Abstand, doch ein Schiff, das hineinfliegt, spürt erst seine Strahlung, dann seinen Sog und wird an seinem Ereignishorizont zerstört. Siehe [Das Schwarze Loch](/wiki/03-Mechanics/Black-Hole.md).

### Die Jump CPU {#the-jump-cpu}

Die [Jump CPU](/wiki/06-Items/Extras.md#jump-cpu) bringt dein Schiff ohne Tor in jeden Konzern-Sektor deiner Welt, für 500 Thulium pro Sprung, auch in die Heimatsektoren der Feinde. Sie führt nie in einen Gefahrensektor, startet nicht im Kampf, und du erforschst sie zuerst im Forschungszentrum des Skylab ([Forschung](/wiki/03-Mechanics/Research.md)). Die [Base CPUs](/wiki/06-Items/Extras.md#base-cpus) bringen dich auf dieselbe Weise nach Hause. Eine Warp-CPU, also die Jump CPU oder eine Base CPU, wird verweigert, solange du einen Missionsgegenstand trägst („Mit einem Missionsgegenstand an Bord kannst du keine Warp-CPU benutzen.“): Fliege durch die Tore nach Hause ([Missionsgegenstände](/wiki/03-Mechanics/Quests.md#quest-items)).
