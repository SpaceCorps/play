<!-- wiki-i18n source: 0d92c80e748fc9b8 -->
<!-- wiki-i18n title: Pilotenfertigkeiten -->
# Pilotenfertigkeiten {#pilot-skills}

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; ep; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs; fertigkeiten; fertigkeitenbaum; pilotenfertigkeiten; erfahrung; stufenaufstieg; werte; attribute; masse; zähigkeit; reflexe; lasertechnik; raketentechnik; antimaterie; treffsicherheit; ausweichen; taktik; strahlungstechnik; triebwerkstheorie; forschung; gewinnung; fertigung; handel; stundengrenze; frachtraum -->

Dein Pilot hat einen **Fertigkeitenbaum**: eine Reihe von Werten, die mit dem aufsteigen, was du tust. Kämpfe, und deine Lasertechnik und deine Zähigkeit steigen; sammle aus deinem Skylab ein, und deine Gewinnung steigt. Jedes Level gibt einen kleinen dauerhaften Buff auf etwas, das du ohnehin tust, und nichts wird ausgegeben oder gewählt: Es gibt keine Punkte zu verteilen und nichts zurückzusetzen. Du steigerst, was du benutzt.

Der Baum gehört **dir**, nicht einem Schiff. Jedes Schiff, das du fliegst, hat deine Level, auch ein Schiff, das du morgen kaufst, und die Level bleiben durch jeden Wipe erhalten ([was bleibt](#what-is-kept)).

Ein neuer Pilot ist nicht bei voller Stärke. Auf Level 1 machen ein Laser und eine Rakete weniger Schaden, als die Gegenstandsseiten nennen, und Lasertechnik und Raketentechnik heben ihn mit jedem Level über die genannten Zahlen hinaus. Jede Zahl auf den Gegenstandsseiten ist die des Gegenstands selbst, vor deinen Fertigkeiten.

## Auf einen Blick {#at-a-glance}

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Werte**: 19 Werte: 4 Attribute und 15 Fertigkeiten in 5 Gruppen
- **Level**: 1 bis 100. Jeder Pilot beginnt jeden Wert auf Level 1, und es gibt nichts zu verteilen und nichts zurückzusetzen
- **Kosten eines Levels**: 40 EP von Level 1 auf 2, 875 EP von Level 50 auf 51, 19.157 EP von Level 99 auf 100; 313.258 EP insgesamt
- **Was ein Level bringt**: Ein Buff wächst geradlinig von seinem Wert auf Level 1 bis zu seinem Wert auf Level 100. Nichts ist gedeckelt
- **Dein Laser auf Level 1**: Er macht 100 % seines Schadens und trifft zu 80 %, also 80 % des Schadens, den die Gegenstandsseiten nennen
- **Deine Rakete auf Level 1**: Sie macht 100 % ihres Schadens und ist zu 10 % ein Blindgänger, also 90 % des Schadens, den die Gegenstandsseiten nennen
- **Ausweichen**: Jedes Pilotenschiff weicht 3 % der Treffer aus, denen man ausweichen kann, bevor eine Fertigkeit oder Formation etwas hinzufügt
- **Hüllenstufe**: Die Seltenheit deines Schiffs legt sie fest, wie die Tabelle unten zeigt. Die Größe deines Frachtraums und die EP von Masse folgen ihr
- **Frachtraum**: Er zählt die Ressourceneinheiten, die du nach dem Start aufsammelst, bis zu der Größe, die seine Hüllenstufe ihm gibt. Voll ist er ab 90 % davon, und ein voller Frachtraum lässt Masse ×1,5 zahlen. Nichts wird je abgelehnt
- **Weiche Stundengrenze**: Die meisten Werte zahlen nur bis zu einer Obergrenze pro Stunde volle EP, gezählt in der eigenen Einheit des Werts über die UTC-Uhrzeitstunde. Darüber zahlt ein Ereignis 25 % seiner EP
- **Training**: Die EP einer Fertigkeit zahlen auch 10 % ihrer selbst an ihr Attribut. Ein Attribut auf Level 100 trainiert seine Fertigkeiten 25 % schneller als auf Level 1

| Hüllenstufe | Seltenheit des Schiffs | Größe des Frachtraums |
| :--- | :--- | ---: |
| 1 | Minderwertig / Gewöhnlich | 60 |
| 2 | Ungewöhnlich | 120 |
| 3 | Selten | 250 |
| 4 | Episch | 500 |
| 5 | Mythisch / Legendär / Ewig | 1.000 |

<!-- skills-glance:end -->

## Die Werte {#the-stats}

Die Werte sind von zweierlei Art. Die **Attribute** (Masse, Zähigkeit, Reflexe und Instinkt) sind die Grundlagen eines Piloten. Die **Fertigkeiten** stehen in fünf Gruppen, und jede Fertigkeit wird von einem Attribut bestimmt, das die Tabellen in Klammern nennen: Die EP einer Fertigkeit füttern auch ihr Attribut, und ein hohes Attribut trainiert seine Fertigkeiten schneller ([wie EP ausgezahlt werden](#how-xp-is-paid)). Die Namen sind die der Seite Pilotenfertigkeiten im Spiel.

Die Tabellen nennen jeden Buff auf Level 1 und auf dem letzten Level; dazwischen wächst ein Buff geradlinig. Ein **Faktor** multipliziert eine Zahl: Einer über 1 macht sie größer, einer unter 1 kleiner. Die meisten Buffs ändern eine Zahl deines Schiffs, und der Tooltip einer Zahl, die eine Fertigkeit bewegt hat, hat eine Zeile, die sagt, wie viel davon aus deinen Fertigkeiten kommt.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Attribute {#attributes}

| Wert | Was er ändert | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Masse** | Hülle | +0 % | +20 % |
| **Zähigkeit** | Erlittener Schaden | ×1 | ×0,92 |
| **Reflexe** | Aufladetempo der Fähigkeiten | ×1 | ×1,1 |
| **Instinkt** | Chance jeder Beutezeile | +0 Punkte | +7,5 Punkte |
|  | Orvium und Velkonite aus den Kollektoren | ×1 | ×1,5 |

### Waffen {#weapons}

| Wert | Was er ändert | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Lasertechnik** (Reflexe) | Laserschaden | ×1 | ×1,3 |
|  | Chance, dass eine Lasersalve trifft | 80 % | 89 % |
| **Raketentechnik** (Reflexe) | Raketenschaden | ×1 | ×1,3 |
|  | Chance, dass eine Rakete ein Blindgänger ist | 10 % | 1 % |
| **Antimaterie** (Instinkt) | Dark Matter beim Aufsammeln | ×1 | ×1,25 |

### Kampf {#combat}

| Wert | Was er ändert | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Treffsicherheit** (Reflexe) | Wurfweite einer Mine | ×1 | ×1,15 |
|  | Geschwindigkeit einer geworfenen Mine | ×1 | ×1,15 |
| **Sabotage** (Reflexe) | Schaden von Giften und Minen | ×1 | ×1,3 |
|  | Dauer von Giften | ×1 | ×1,2 |
| **Ausweichen** (Reflexe) | Chance, einem Treffer auszuweichen, zusätzlich zu der des Schiffs | 0 % | 15 % |
| **Taktik** (Reflexe) | Dauer der Fähigkeiten | ×1 | ×1,2 |
| **Schildabsorption** (Zähigkeit) | Absorption deiner Schilde | +0 Punkte | +5 Punkte |

### Schiffssteuerung {#ship-control}

| Wert | Was er ändert | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Strahlungstechnik** (Zähigkeit) | Strahlungsdosis | ×1 | ×0,4 |
| **Triebwerkstheorie** (Masse) | Geschwindigkeit | +0 % | +10 % |
| **Forschung** (Instinkt) | Forschungspunkte je Einheit Treibstoff | ×1 | ×1,25 |

### Skylab

| Wert | Was er ändert | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Gewinnung** (Instinkt) | Was das Skylab herstellt | ×1 | ×1,3 |
| **Logistik** (Masse) | Was die Bank des Ressourcenlagers fasst | ×1 | ×1,4 |
| **Fertigung** (Reflexe) | Zeit einer Herstellung | ×1 | ×0,65 |

### Handel {#trading}

| Wert | Was er ändert | Level 1 | Level 100 |
| :--- | :--- | ---: | ---: |
| **Handel** (Instinkt) | Preise im Shop | ×1 | ×0,85 |
|  | Was der Shop beim Rückkauf zahlt | ×1 | ×1,1 |
|  | Einstellgebühr eines Auktionsangebots | ×1 | ×0,5 |


<!-- skills-buffs:end -->

## Wo du es merkst {#where-you-feel-it}

- **Laser.** Lasertechnik ändert den Schaden jeder Salve und die Chance, dass sie trifft; eine Salve, die danebengeht, zeigt ein schwebendes „Miss“ und verbraucht trotzdem ihre Munition ([Kampf](/wiki/03-Mechanics/Combat.md#laser-tech)). Die Reichweite deiner Laser ist die deines Schiffs: Treffsicherheit steigt durch deine Treffer mit anderer Munition als dem einfachen x1, wirkt aber nur auf Minen (unten).
- **Raketen.** Raketentechnik ändert den Schaden jeder Rakete und die Chance, dass eine ein Blindgänger ist ([Raketentechnik](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Treffer einstecken.** Zähigkeit nimmt von jedem Treffer, den du einsteckst, einen Anteil ab, Ausweichen erhöht die Chance, dass ein direkter Treffer nichts bewirkt, und Schildabsorption erhöht den Anteil eines Treffers, den deine Schilde nehmen ([Kampf](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). Masse erhöht deine Hülle.
- **Fähigkeiten.** Reflexe verkürzen die Abklingzeit deiner Fähigkeiten, und Taktik lässt sie länger wirken ([Fähigkeiten](/wiki/03-Mechanics/Abilities.md#pilot-skills)). Sabotage verstärkt die Gifte.
- **Minen.** Sabotage erhöht den Schaden einer Mine, und Treffsicherheit wirft sie schneller und weiter ([Extras](/wiki/06-Items/Extras.md#mine)).
- **Tempo.** Triebwerkstheorie erhöht dein Tempo, zusätzlich zu den Triebwerken und einem Afterburner ([Tempo](/wiki/03-Mechanics/Speed.md)).
- **Aufsammeln.** Instinkt erhöht die Chance jeder Beutezeile, so wie es ein Loot Luck Booster tut, und beide addieren sich; Antimaterie erhöht das Dark Matter, das du aufsammelst ([Frachtkisten](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Strahlung.** Strahlungstechnik senkt die Dosis des Schwarzen Lochs, der Kreise der Bagger, der Pulsare und der Aura der Unwakened ([Schwarzes Loch](/wiki/03-Mechanics/Black-Hole.md)).
- **Zuhause.** Gewinnung und Logistik ändern, was das [Skylab](/wiki/03-Mechanics/Skylab.md) herstellt und fasst, Instinkt erhöht seine beiden Kollektoren, Fertigung verkürzt die Herstellungen in der Montage, Forschung füllt das [Forschungszentrum](/wiki/03-Mechanics/Research.md) schneller, und Handel senkt die Preise im Shop, erhöht, was er beim Rückkauf zahlt, und senkt die Einstellgebühr eines Angebots in der [Auktion](/wiki/03-Mechanics/Auction.md).

## Wie EP ausgezahlt werden {#how-xp-is-paid}

Der Server zahlt EP für das, was du tust, wo immer du fliegst, in dieser Reihenfolge:

1. **Die Anti-Farm-Regel.** Ein Treffer von oder auf einen Konzernkameraden oder Gruppenkameraden zahlt nichts, und ebenso nichts, was einem Schiff in einer sicheren Zone oder unter dem Schutz eines Respawns angetan wird oder von ihm ausgeht. Die Sekunden von Masse, von niedriger Hülle (Zähigkeit) und von Triebwerkstheorie zählen nur, solange dein Schiff lebt, außerhalb eines Schutzes ist und du in der letzten Minute einen Befehl gegeben hast: Ein Schiff, das im Freien parkt, verdient nichts.
2. **Die weiche Stundengrenze.** Ein Wert mit Obergrenze zahlt bis dahin volle EP und darüber einen Anteil davon, gezählt in der eigenen Einheit des Werts (die Schüsse, die du abfeuerst, die Befehle, die du gibst, die EP, die er verdient hat) über die UTC-Uhrzeitstunde. Eine neue Anmeldung öffnet das Fenster nicht neu, und die Zahlen stehen in der Liste oben und in der Tabelle unten.
3. **Trainingstempo.** Das Attribut, das eine Fertigkeit bestimmt, erhöht die EP, die die Fertigkeit verdient, mit jedem Level des Attributs mehr (die Obergrenze wird davor gezählt, sie begrenzt also die Tätigkeit und nicht das Tempo).
4. **Der Anteil des Attributs.** Die Fertigkeit bekommt die EP, und ihr Attribut bekommt einen Anteil davon, der nie gedeckelt oder beschleunigt wird.

Die Tabelle nennt, was EP bringt, Wert für Wert. Die EP gelten für jede Einheit dessen, was in der zweiten Spalte steht.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Wert | Was EP bringt | EP | Weiche Stundengrenze |
| :--- | :--- | ---: | ---: |
| **Masse** | Je 10 s Flug mit einem Befehl in den letzten 1 min: die Hüllenstufe des Schiffs, plus 0,2 je eingebauter Platte, ×1,5 bei vollem Frachtraum | 1 | Keine |
| **Zähigkeit** | Je 1 % deiner maximalen Hülle, die du an einen Feind oder eine Gefahr verlierst | 1 | 300 EP pro Stunde |
|  | Je 10 s unter 25 % deiner maximalen Hülle | 5 |  |
| **Reflexe** | Je Befehl, den das Spiel annimmt: eine Fähigkeit, ein Extra, ein neues Ziel, ein Aufsammeln, eine Herstellung, ein Formationswechsel, eine Rakete oder ein Sprung. Ein neues Ziel zahlt höchstens einmal in 4 s, ein Aufsammeln höchstens einmal in 1 s und eine Rakete höchstens einmal in 1 s | 1 | 600 Befehle pro Stunde |
| **Instinkt** | Je Frachtkiste, die du von Hand oder mit einem Retriever aufsammelst | 2 | 600 EP pro Stunde |
|  | Je Gegenstand einer Questbelohnung, den du abholst | 10 |  |
|  | Das erste Mal, dass du einen Gegenstand von seltener Qualität oder besser aufsammelst (einmal je Gegenstand, für immer) | 25 |  |
| **Lasertechnik** (Reflexe) | Je Salve, die du abfeuerst | 0,1 | 1.800 Schüsse pro Stunde |
|  | Je Salve, die ein Schiff trifft | 0,1 |  |
| **Raketentechnik** (Reflexe) | Je Rakete, die du startest | 0,15 | 130 Raketen pro Stunde |
|  | Je Rakete, die ein Schiff trifft (einmal je Rakete, wie viele Schiffe ihre Explosion auch trifft) | 0,3 |  |
| **Antimaterie** (Instinkt) | Je Einheit Dark Matter, die du beim Aufsammeln erhältst | 2,2 | Keine |
| **Treffsicherheit** (Reflexe) | Je Treffer einer Salve mit anderer Munition als dem einfachen x1 (×1,5 in den ersten 10 min jeder Munitionsart in einer Uhrzeitstunde) | 0,1 | 3.000 Treffer pro Stunde |
|  | Je Treffer einer Mine und je Sekunde, die ein Feind in deiner Energetic Wall verbringt | 0,1 |  |
| **Sabotage** (Reflexe) | Je Treffer einer Mine und je Sekunde, die ein Feind in deiner Energetic Wall verbringt | 0,5 | 1.200 EP pro Stunde |
|  | Je Sekunde, die ein Gift von dir auf einem Feind wirkt | 0,05 |  |
| **Ausweichen** (Reflexe) | Je feindlichen Angriff auf dich, der danebengeht oder dem du ausweichst | 1 | 600 EP pro Stunde |
| **Taktik** (Reflexe) | Je Fähigkeit, die du mit einem Feind in Laserreichweite drückst | 2 | 600 EP pro Stunde |
| **Schildabsorption** (Zähigkeit) | Je 1 % deiner maximalen Schildpunkte, die Treffer von Feinden aufnehmen | 0,1 | 300 EP pro Stunde |
| **Strahlungstechnik** (Zähigkeit) | Je Sekunde in einem Strahlungsband | 0,2 | Keine |
|  | Je 1 % deiner maximalen Hülle, den die Strahlung nimmt | 1 |  |
| **Triebwerkstheorie** (Masse) | Je Sekunde Flug über 80 % der Geschwindigkeit deines Schiffs, doppelt so viel unter einem Afterburner | 0,1 | Keine |
| **Forschung** (Instinkt) | Je Forschungspunkt, den das Forschungszentrum verbrennt | 0,1 | Keine |
|  | Je Technologie, die du abschließt | 50 |  |
| **Gewinnung** (Instinkt) | Je Ressourceneinheit, die dein Skylab herstellt, ausgezahlt beim Einsammeln | 0,1 | Keine |
| **Logistik** (Masse) | Je Ressourceneinheit, die du in die Bank des Skylab einzahlst | 0,05 | Keine |
| **Fertigung** (Reflexe) | Je Sekunde Herstellungszeit, die du abschließt, ausgezahlt beim Einsammeln | 0,1 | Keine |
| **Handel** (Instinkt) | Je Handel in der Auktion oder im Shop, gezählt als der dekadische Logarithmus von 1 plus seinem Wert in Credits (ein Thulium ist so viel wert, wie die Auktion es bewertet) | 2 | 600 EP pro Stunde |

<!-- skills-xp:end -->

Während du fliegst, zeigt der Flugbildschirm die EP, die du verdienst, in kurzen Zeilen, alle paar Sekunden gesammelt, und ein Banner sagt dir, wenn ein Wert aufsteigt und was sich geändert hat (das Spielprotokoll behält eine Zeile dafür). Ein Wert, der seine ersten EP verdient, wird einmal angekündigt. Die Tooltips der Zahlen, die Fertigkeiten bewegt haben, sagen es auch, in einer eigenen Pilot-Zeile, und die Kachel „Schaden“ des Hangars lässt die Fertigkeiten weg und sagt das: Sie wirken, wenn du feuerst.

## Aufstieg {#levelling-up}

Ein Level kostet mehr EP als das davor, um einen festen Anteil, die ersten Level kommen also schnell und die letzten dauern lange. Jeder Wert hat dieselbe Kurve. Der Buff, den du auf einem Level hast, ist für jeden Piloten gleich: Nur das Tempo, mit dem du ihn erreichst, hängt davon ab, was du tust.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Level | EP für das Level | EP insgesamt ab Level 1 | Anteil jedes Buffs |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | 1,01 % |
| 10 | 66 | 468 | 9,09 % |
| 25 | 170 | 2.174 | 24,24 % |
| 50 | 822 | 12.851 | 49,49 % |
| 75 | 3.968 | 64.397 | 74,75 % |
| 100 | 19.157 | 313.258 | 100 % |

<!-- skills-curve:end -->

## Die Seite Pilotenfertigkeiten {#the-pilot-skills-page}

Die Seite **Pilotenfertigkeiten** ist eine Seite der Station mit einer eigenen Zeile in der Seitenleiste. Sie ist ein kompaktes Blatt für den ganzen Baum: Die Attribute und die fünf Gruppen von Fertigkeiten stehen nebeneinander in Spalten (drei auf einem breiten Bildschirm, weniger auf einem schmalen), je Wert eine Zeile mit seinem Level am rechten Rand und einer dünnen EP-Leiste darunter. Ein Wert, der noch keine EP verdient hat, ist grau und hat einen Strich als Level. Halte den Mauszeiger auf eine Zeile, um zu sehen, was der Wert tut, welches Attribut ihn bestimmt oder welche Fertigkeiten er trainiert, seine EP und was ihn wachsen lässt. Klicke auf eine Zeile, um ihre Details unter ihrer Spaltenreihe zu öffnen: dieselben Worte, die EP-Leiste und einen Regler, um jedes Level von 1 bis zum letzten vorab anzusehen, mit einer kleinen Tabelle, was der Wert auf Level 1, auf deinem Level jetzt, auf dem Level, das du ansiehst, und auf dem letzten Level ändert. Es ist immer nur ein Wert geöffnet; klicke die Zeile erneut an, nutze die Schaltfläche zum Schließen oder drücke Esc, um ihn wegzulegen. Die Zeile in der Seitenleiste trägt ein Abzeichen, wenn ein Wert aufgestiegen ist, seit du die Seite zuletzt geöffnet hast, und eine Karte im Booster-Fenster fasst zusammen, was deine Fertigkeiten ändern.

Im Flug ist dasselbe Blatt das Fenster **Pilotenfertigkeiten**. Öffne es mit der Schaltfläche Pilotenfertigkeiten der Werkzeugleiste (auf einem breiten Bildschirm) oder mit seiner Taste, standardmäßig K (Einstellungen, Steuerung). Es ist ein Fenster wie die anderen: Du kannst es verschieben und in der Größe ändern, und es merkt sich seinen Platz und ob es offen war. Es zeigt nur deine Fertigkeiten: Die Level ändern sich, wenn die EP-Zeilen des Flugs eintreffen, und ein Klick auf eine Zeile öffnet dieselben Details im Fenster.

## Was bleibt {#what-is-kept}

- **Durch jeden Wipe.** Der Baum ist ein Teil deines Accounts: Ein Wipe ändert kein Level und keine EP, und der Transport-Cache hat damit nichts zu tun ([Was du behältst](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **Auf den regionalen Servern.** Die EP, die du beim Fliegen auf Singapore oder US East verdienst, werden deinen Fertigkeiten gutgeschrieben, wenn du heimkehrst, auch bei einem Wert, den du dort zum ersten Mal benutzt hast, und die Stundengrenze, die du dort aufgebraucht hast, geht mit dir. Die Seite Pilotenfertigkeiten eines Piloten, der dort fliegt, liest die Zahlen des regionalen Servers, mit den EP, die sein Schiff seit seiner letzten Speicherung verdient hat.
- **Bis der Account gelöscht wird.** Wer einen Account löscht, löscht auch seine Level.

Die Buffs haben keine Decke außer dem letzten Level: Ein Pilot, der alles gesteigert hat, ist so stark, wie die Tabellen sagen.
