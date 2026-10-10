<!-- wiki-i18n source: 0f9ae19e1c5f8f9d -->
<!-- wiki-i18n title: Kampf -->
# Kampfmechanik {#combat-mechanics}

Dieser Abschnitt beschreibt, wie Schaden in SpaceCorps berechnet, angewendet und repariert wird, wenn es zum Gefecht kommt.

![The death screen: respawn at the nearest portal or on the spot, each with its lock](../../img/wiki-img/shots/death.jpg)
![The flight screen in a fight: ship and pilot windows, the target, the hotbar, the chat, the log and the minimap](../../img/wiki-img/shots/hud-fight.jpg)
![The Target window: the alien, its distance, hull and shield](../../img/wiki-img/shots/hud-target.jpg)

## Schadensberechnung {#damage-calculation}

Wenn ein Schiff seine Laser abfeuert, berechnet der Server den Schaden in dieser Reihenfolge:

### 1. Grundschaden & Zufallsschwankung {#1-base-damage-random-variance}

Der Grundschaden aller ausgerüsteten Laser (einschließlich der Laser auf Drohnen) und ihrer eingesetzten Laserverstärker wird summiert.
- **Zufallswurf**: Der tatsächliche Schaden einer Salve wird zufällig zwischen **80 %** und **100 %** des gesamten Grundschadens ausgewürfelt.
  - Formel: `Roll = (0.8 + (Random * 0.2)) * BaseDamage`

### 2. Kritische Treffer {#2-critical-hits}

Jede Salve hat eine Chance, ein kritischer Treffer zu sein.
- **Krit-Chance**: Die durchschnittliche Krit-Chance der ausgerüsteten Laser plus die Summe der Krit-Chancen aller ausgerüsteten Laserverstärker.
- **Krit-Multiplikator**: Ist ein Schuss kritisch, wird der Schadenswurf mit **1,5x** multipliziert. Die Schadenszahl einer kritischen Salve wird in Eisblau angezeigt, größer und mit einem „!“ (siehe [Schadens- und Heilungszahlen](#damage-and-heal-numbers)).
- Quantum Laser I und II haben keine eigene Krit-Chance: Ihre Verstärker geben sie ihnen.
- **Fester Krit-Schaden**: Fester kritischer Schaden von Laserverstärkern wird nach dem Multiplikator addiert.
  - Formel: `CritDamage = (Roll * 1.5) + FixedCritDamage`

### 3. Globale Multiplikatoren {#3-global-multipliers}

Zuletzt werden globale Multiplikatoren (etwa aktive Booster, zum Beispiel die +10 % eines Laser Damage Booster, oder Multiplikatoren der Lasermunition wie x2, x3, x4) angewendet, um den endgültigen Schaden zu erhalten:
- Formel: `FinalDamage = Damage * AmmoMultiplier * (1.0 + BoosterDamagePercent)`
- Eine getragene [Drohnenformation](/wiki/03-Mechanics/Formations.md) kann das Ergebnis noch einmal multiplizieren: zum Beispiel Auger +21 % Laserschaden, Gyre −11 % und gegen Aliens Culler +12 % (ein eigener Faktor, nicht Teil des Booster-Prozentsatzes).
- Die Munition **Siphon Battery** hat den Multiplikator x1, aber ein anderes Ziel: Ihr Schaden geht allein vom Schild des Ziels ab (nie von der Hülle, egal wie hoch die Absorption) und fließt in deinen eigenen Schild, bis zu deinem Maximum. Siehe [Laser & Munition](/wiki/06-Items/Lasers.md).

### 3b. Raketen {#3b-rockets}

Eine [Rakete](/wiki/06-Items/Rockets.md) hat ihren eigenen Schaden (eine Lancet I 1.700 bis 2.100, eine Lancet III 5.200 bis 6.200, eine N.U.K.E. 45.000 bis 50.000), der beim Abfeuern einmal ausgewürfelt wird und für jedes Schiff derselbe ist: Deine Laser, Verstärker, Booster und deine Munition ändern ihn nicht, und es gibt keinen kritischen Treffer. Alle Raketen teilen sich einen **3-Sekunden**-Timer. Eine Rakete mit Einzelziel hat eine **Schilddurchdringung**: Sie wird von der Absorption deines Ziels abgezogen (siehe „Schaden nehmen“ weiter unten); eine Explosion trifft jedes Schiff in ihrem Radius, die volle Zahl im Zentrum und die Hälfte davon am Rand. Nichts begrenzt, was eine Rakete dem Schiff eines Piloten nimmt: erst den Schild, dann die Hülle. Raketen verletzen nie deinen eigenen Konzern oder deine eigene [Gruppe](/wiki/03-Mechanics/Groups.md), egal welchen Konzernen ihre Mitglieder angehören. Eine getragene [Drohnenformation](/wiki/03-Mechanics/Formations.md) ist das Einzige, was beides verändert: Eine Raketenformation erhöht den Schaden jeder Rakete (bis zu +55 %), und einige machen den Timer länger oder kürzer. [Asteroiden](/wiki/03-Mechanics/Asteroid-Mining.md) nehmen durch Raketen Schaden und durch Laser mit 5 % dessen, was eine Salve einem Schiff antut (deine Verstärker, Booster, Munition und kritischen Treffer zählen, danach wird die Panzerung des Asteroiden abgezogen); Drohnen richten bei ihnen nichts aus, und ein Asteroid im Weg eines Schusses nimmt den Treffer anstelle des Schiffs dahinter ([Deckung](/wiki/03-Mechanics/Asteroid-Mining.md#cover)).

### 4. Dem Ziel zugewandt {#4-facing-the-target}

Ein Schiff oder Alien, das ein Ziel anvisiert hat und feuert, dreht sich dem Ziel zu, in welche Richtung es auch fliegt (kreisend, zurückweichend oder stillstehend), und dreht sich wieder auf seinen Kurs, wenn es aufhört zu feuern.

### 5. Reichweite {#5-range}

Ein Schiff feuert eine Salve pro Sekunde, solange sein Ziel innerhalb seiner **Reichweite** ist, und hält das Feuer, solange das Ziel weiter entfernt ist: Das Feuer kostet dann keine Munition, bis das Ziel wieder nah genug ist, und das Zielfenster zeigt „Außer Reichweite“. Die Reichweite ist **der Durchschnitt der Reichweiten all deiner Laser** (auch der Laser in deinen Drohnen), auf die nächste Einheit gerundet, und sie ist eine einzige Zahl für das ganze Schiff: Innerhalb davon feuert jeder Laser, außerhalb keiner. Ein weitreichender Laser neben kurzen verlängert deine Reichweite also nicht: Ein Starfire-III (850) und zwei Quantum Laser II (700) ergeben 750. Ein Schmiede-Buff auf die Reichweite zählt auf seinem eigenen Laser, bevor der Durchschnitt gebildet wird. Ein Schiff ohne Laser kann seine Laser nicht abfeuern, und der Hangar zeigt dafür keine Reichweite an (einen Strich); seine Raketen feuern trotzdem, jede mit ihrer eigenen Reichweite (siehe [Raketen](/wiki/06-Items/Rockets.md)). Die eigene Reichweite jedes Lasers steht unter [Laser & Munition](/wiki/06-Items/Lasers.md).

## Schadens- und Heilungszahlen {#damage-and-heal-numbers}

Ein Treffer erscheint als Zahl, die über dem Schiff schwebt, das er trifft. **Deine eigenen Zahlen** werden immer angezeigt: der Schaden, den du austeilst, der Schaden, den du nimmst, und deine eigenen Reparaturen. **Das Schiff unter deiner Zielerfassung** zeigt mehr: jeden Treffer und jede Heilung, die es bekommt, **aus jeder Quelle**. Das heißt: die Laser, Raketen und Drohnen anderer Piloten, Aliens, Clan Wardens sowie die eigenen Reparaturen und die Schildregeneration des Schiffs. Wenn jemand anderes auf dein Ziel schießt, siehst du seinen Schaden.

- **Farben.** Gold: Schaden an einem Alien oder einem gegnerischen Piloten. Rot mit einem Minus: Schaden an einem Schiff, das du schützt (ein Pilot deines eigenen Konzerns oder deiner Gruppe), und der Schaden, den du selbst nimmst. Grün mit einem Plus: eine Heilung, etwa eine Emergency Repair, eine Repair Drone oder ein Schild, der zurückkommt. Blasssilbernes „Miss“: ein direkter Treffer, den die Ausweichchance einer Formation abgelenkt hat. Eine kritische Salve ist größer und endet auf „!“ (eisblau, wenn sie ein Alien oder einen Gegner trifft).
- **Deine bleiben heller.** Die Zahlen anderer auf deinem Ziel sind etwas kleiner und blasser und stehen in einer Spalte rechts vom Schiff, damit sie deine nie verdecken.
- **Eine Zahl für eine Menge.** Treffer, die zusammen landen, werden zu einer Zahl mit einer Anzahl dahinter addiert (`×35`). Vierzig Piloten, die auf ein Schiff feuern, ergeben etwa zwei Zahlen pro Sekunde und nie mehr als sieben. Heilungen erscheinen einmal pro Sekunde.
- **Nur das Schiff unter dem Kreis.** Jedes andere Schiff zeigt nur deine eigenen Treffer und die Treffer auf dich. Die Strahlung des Schwarzen Lochs und der Schilddrain einer Formation haben keine Zahlen: Sie zeigen sich nur auf den Balken.
- **Die Einstellung.** Einstellungen › Oberfläche › **Schaden anderer auf meinem Ziel anzeigen**, standardmäßig an. Ausgeschaltet siehst du nur deine eigenen Zahlen. **Bewegung reduzieren** hält jede Zahl ruhig: Keine ploppt auf oder steigt.

---

## Abschussbelohnungen: Der erste Treffer sichert den Anspruch {#kill-rewards-first-hit-claims}

Die Belohnungen eines Aliens gehen an den Piloten, der zuerst auf es geschossen hat, nicht an den, der den letzten Treffer landet.

- **Beanspruchen**: Der erste Pilot, dessen Schuss ein Alien beschädigt, beansprucht es. Jeder Treffer von dir erneuert deinen Anspruch.
- **Verlieren**: Triffst du das Alien **10 Sekunden** lang nicht, verfällt dein Anspruch, und der nächste Pilot, der es trifft, beansprucht es. Dein Anspruch endet auch, wenn dein Schiff zerstört wird oder du die Karte verlässt (durch ein Portal oder durch Ausloggen), und eine Rückkehr innerhalb der 10 Sekunden bringt ihn nicht zurück.
- **Der Abschuss**: Wird das Alien zerstört, bekommt der Pilot, der seinen Anspruch hält, alles: Credits, Thulium, EP, Ehre, den Abschuss für Quests und Wipe-Punkte und die [Frachtkiste](/wiki/03-Mechanics/Cargo.md). Ein Pilot, der ein Alien erledigt, das ein anderer beansprucht hat, bekommt nichts, und das Spielprotokoll sagt es. Zahlt dein Anspruch und ein anderer Pilot landet den letzten Treffer, nennt das Spielprotokoll diesen Piloten und sagt, dass dein Anspruch dir die Belohnung bringt.
- **Rangpunkte**: Der Abschuss bringt dem Piloten, der den Anspruch hält, außerdem PvE-Punkte für seine Rangliste, und zwar mehr für ein zäheres Alien: 1 für einen Seeker, 2 für einen Phantasm, 4 für einen Bulwark, 7 für einen Goombah und 16 für einen Crystalys (der Artikel jedes Aliens nennt seinen eigenen Wert). Sie gehören allein dem Piloten: Der Gruppenanteil an den Belohnungen enthält sie nicht.
- **So siehst du es**: Wählst du ein Alien aus, das ein anderer Pilot beansprucht hat, zeigt das Zielfenster *Beansprucht von* diesem Piloten und *Keine Belohnung*.
- [Konzernpiloten](/wiki/03-Mechanics/Company-Pilots.md) beanspruchen nie ein Alien, und ein Alien, das sie erledigen, zahlt trotzdem an den Piloten, der seinen Anspruch hält.
- Ein Pilot in einer [Gruppe](/wiki/03-Mechanics/Groups.md) teilt, was sein Anspruch einbringt, mit den Gruppenmitgliedern, die nah dran sind und schießen; der Anspruch selbst gehört allein dem Piloten.
- **Die Anführer der [Schwärme](/wiki/05-Swarms/Swarms.md), die Dormant Pulses und die [Clan Wardens](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot) sind die Ausnahme**: Ein Schwarm-Boss, jede Dormant Pulse und jeder Clan Warden werden nach dem Schaden bezahlt, den jeder Pilot ihnen zugefügt hat, nicht nach dem ersten Treffer, und ihre Frachtkiste geht an den Piloten mit dem meisten Schaden ([so zahlt ein Boss-Abschuss](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Die übrigen Begleiter, die Pirate Scouts und die Seeker Slaves, zahlen wie jedes Alien nach dem Anspruch. Die PvE-Punkte eines Schwarmschiffs stehen auf der Seite Schwärme.

---

## Aliens, die sich nur wehren {#aliens-that-only-fight-back}

Der Seeker und der Goombah beginnen nie einen Kampf. Jeder wendet sich gegen einen Piloten, der ihn trifft (ein Treffer, der Schaden verursacht; das Feuer eines anderen Aliens reizt ihn nie), kämpft gegen den Piloten, den der Abschnitt [Gegen wen ein Alien kämpft](#who-an-alien-fights) beschreibt, und lässt **10 Sekunden**, nachdem ihn zuletzt jemand getroffen hat, von diesem Piloten ab. Wird er **30 Sekunden** lang in Ruhe gelassen, repariert sich seine Hülle jede Sekunde um 2 % ihres Maximums. Die anderen Aliens (Phantasm, Bulwark, Crystalys) gehen auf jeden ungeschützten Piloten los, der in ihren Aggro-Radius kommt (700, 700 und 900 Einheiten), und reparieren ihre Hülle nie; der Schild jedes Aliens lädt sich ab 15 Sekunden nach seinem letzten Treffer wieder auf.

---

## Gegen wen ein Alien kämpft {#who-an-alien-fights}

Ein Alien kämpft weiter gegen **den Piloten, der zuerst auf es geschossen hat**, solange es diesen Piloten noch verfolgen kann: Der Pilot ist auf der Karte, nicht in einer Schutzzone, nicht getarnt und nicht im Zeitfenster seines EMP, am Leben und hat das Alien in den letzten **10 Sekunden** getroffen (jeder Treffer startet die 10 Sekunden neu: eine Lasersalve, eine Rakete oder der Rand einer Explosion gleichermaßen). Solange das gilt, bringen die Schüsse anderer Piloten das Alien nie von ihm ab, egal wie nah sie sind oder wie oft sie treffen, sodass ein Pilot ein Alien festhalten kann, während andere auf es schießen.

Scheidet der erste Pilot aus (er verlässt die Karte, erreicht eine Schutzzone, tarnt sich oder steht im Zeitfenster seines EMP, wird zerstört oder trifft das Alien 10 Sekunden lang nicht mehr), wendet sich das Alien dem **nächsten** der Piloten zu, die in den Kampf eingestiegen sind, in der Reihenfolge, in der sie zum ersten Mal auf es geschossen haben, nicht dem, der es zuletzt getroffen hat. Ein Pilot, der ausgeschieden ist und erneut auf es schießt, reiht sich hinten in die Warteschlange ein. Ein Alien merkt sich die ersten **32** Piloten, die auf es geschossen haben; ein 33. Schütze nimmt an der Warteschlange nicht teil, bis einer von ihnen ausscheidet, und in einer Menge beliebiger Größe bleibt das Alien beim Ersten.

[Konzernpiloten](/wiki/03-Mechanics/Company-Pilots.md) kommen nach jedem Spieler: Ein Alien kämpft nur so lange gegen einen Konzernpiloten, wie kein Spieler, den es noch verfolgen kann, auf es geschossen hat; ein Spieler, der auf ein Alien schießt, gegen das ein Konzernpilot kämpft, übernimmt es, und ein Konzernpilot zieht ein Alien nie von einem Spieler ab. Nichts davon ändert, wer die Belohnungen des Aliens bekommt: Das entscheidet der Anspruch ([Abschussbelohnungen](#kill-rewards-first-hit-claims)).

---

## Aliens verlieren das Interesse {#aliens-lose-interest}

Kein Alien folgt dir quer über die Karte. Ein Alien, das du **triffst**, verliert aber nicht das Interesse, es kämpft gegen dich: In den **10 Sekunden** nach deinem letzten Treffer (jeder Treffer startet die 10 Sekunden neu, ob Lasersalve, Rakete oder der Rand einer Explosion) fliegt es mit seinem eigenen Tempo auf dich zu, wann immer du außerhalb seiner Angriffsreichweite bist (Seeker 600, Phantasm und Bulwark 700, Goombah 800, Crystalys 900), und rückt weiter vor und feuert, bis du in Reichweite bist. Es gibt keine Grenze dafür, wie weit es dir folgt, solange du es weiter triffst. Ein Laser, der weiter reicht als die Waffe des Aliens (ein Starfire-III reicht 850 Einheiten weit, ein Helios Beam 900), erlaubt dir nicht, es von dort aus zu treffen, wo es nicht antworten kann, und ein schnelleres Schiff hält es nur so lange hinter dir, wie du weiterschießt. Es lässt dich trotzdem sofort fallen, wenn du eine Schutzzone erreichst, dich tarnst oder die Karte verlässt.

Treffen mehrere Piloten dasselbe Alien, bleibt es bei dem, der als Erster auf es geschossen hat (siehe [Gegen wen ein Alien kämpft](#who-an-alien-fights)): Es rückt auf diesen Piloten vor und feuert, sodass eine Gruppe, die knapp außerhalb seiner Reichweite um es herumsteht, es nicht von einem zum anderen hetzen kann, ohne dass es je antwortet.

Ein Alien, das dich zu seinem Ziel gemacht hat (ein Phantasm, Bulwark oder Crystalys, dem du nahe gekommen bist, oder ein beliebiges Alien, auf das du geschossen hast) und das du seit 10 Sekunden nicht getroffen hast, lässt von dir ab, sobald eines davon zutrifft:

- **Du hast nie auf es geschossen:** Du bist mehr als **1.200 Einheiten** von ihm entfernt, oder es ist **2.000 Einheiten** weit von dem Punkt geflogen, an dem die Verfolgung begann.
- **Du hast in der letzten Minute auf es geschossen:** Du bist mehr als **2.500 Einheiten** von ihm entfernt, oder es ist **3.000 Einheiten** weit von dem Punkt geflogen, an dem die Verfolgung begann. Ein Kampf, den du begonnen hast, bleibt fair.

Ein Alien, das von dir ablässt, streift von dort aus weiter, wo es steht, nie dorthin, wo es dich zuletzt gesehen hat (auch nicht, wenn du dich tarnst oder einen EMP auslöst), und wählt dich **8 Sekunden** lang nicht wieder als Ziel, es sei denn, du schießt auf es. Jedes Alien entscheidet für sich, deshalb lichtet sich ein gemischtes Rudel, während du wegfliegst. Aliens folgen dir nie in eine Schutzzone oder durch ein Tor, und die, die dich in deren Nähe verloren haben, ziehen jeweils ihres Weges davon, damit sie nicht als Haufen dort warten. Ein Alien verliert sein Interesse nie innerhalb seiner Angriffsreichweite und seines Aggro-Radius, plus 100 Einheiten.

Aliens schieben sich nicht gegenseitig auseinander: Ein Rudel, das hinter einem Piloten her ist, rückt vor, ohne Platz zwischen seinen Schiffen zu lassen, und ein Rudel, das seinen Piloten verloren hat, löst sich nur auf, indem jedes Alien seinen eigenen Weg wählt. Von einem **Schiff** halten Aliens aber Abstand: Sie landen nie in der Hülle eines Piloten, und ein Pilot, der sich auf eines stellt, schiebt es mit.

Schneller zu fliegen hilft dir nur bis zu einem gewissen Punkt: Eine Protos (160) ist nicht schneller als irgendein Alien, das jagt (Phantasm 160, Bulwark 175, Crystalys 230), also beendet die Verfolgungsgrenze die Jagd, nicht dein Tempo.

---

## Schaden nehmen & Schutzzonen {#taking-damage-safe-zones}

Wird dein Schiff von einem Feind oder NPC getroffen, wird der Schaden so verarbeitet:

### 1. Schildabsorption {#1-shield-absorption}

Eingehender Schaden wird nach der **durchschnittlichen Absorption** deines Schiffs auf Schilde und Trefferpunkte aufgeteilt: dem Durchschnitt der Absorption deiner Schilde, jeweils mit der ihrer Schildzellen, plus dem Schildabsorptions-Boost aus dem Saison-Shop (siehe [Schildmechanik](/wiki/03-Mechanics/Shields.md)). Sie ist **nicht auf 100 % begrenzt**: Was die Schilde von einem Treffer nehmen, ist deine Absorption **abzüglich der Schilddurchdringung des Angreifers**, zwischen 0 % und 100 %.
- **Absorption** (z. B. 80 % für den besten Schild mit den besten Zellen, 56 % für einen Basic Shield Core mit zwei Absorption Shield Cell I) jedes Treffers wird von den Schilden genommen, abzüglich der Durchdringung des Treffers: Die 35 % einer Lancet III lassen 45 % auf den Schilden eines Schiffs mit 80 %, und der Rest (dort 55 %) trifft direkt die HP.
- **Schilddurchdringung** kommt von direkten Raketen (10 bis 35 %) und der Lasermunition x3 und x4 (5 % und 10 %); Aliens haben keine. Ein Schiff über 100 % (etwa 112 %) hält einen ganzen Treffer gegen eine Durchdringung bis zur Differenz aus (dort 12 %). Die Penetration Amps der Laser des Schützen (+3 % bis +12 % pro Slot) und eine Drohnenformation kommen dazu, und nichts begrenzt die Summe.
- Ein Schild, der für seinen Anteil zu niedrig ist, gibt die Differenz an die HP weiter; sind die Schilde ganz erschöpft, trifft **100 %** des gesamten restlichen Schadens die HP.
- Aliens haben keinen Absorptionswert: Ihre Schilde nehmen 80 % jedes Treffers (abzüglich der Durchdringung des Treffers), ihre Hülle den Rest.
- **Drohnenformationen.** Rampart erhöht deine Absorption um 17 % (Shrike senkt sie um 6 %), und Asterism gibt jedem direkten Treffer auf dich eine Chance von 7 %, gar keinen Schaden anzurichten (ein schwebendes „Verfehlt“ erscheint), und die Treffer, die ankommen, teilen sich Schild und Hülle wie gewohnt. Gemini (+9 Punkte) und Stiletto (+16) addieren Durchdringung zu deiner eigenen Munition und zu direkten Raketen, ohne Obergrenze ([Drohnenformationen](/wiki/03-Mechanics/Formations.md)). Bei einem Laser zählen auch seine Amps mit.

### 2. Immunität in Schutzzonen {#2-safe-zone-immunity}

Die Heimatbasis jedes Konzerns (X-1-Karten) enthält Schutzzonen.
- Betrittst du eine Schutzzone, ist dein Schiff vollständig immun gegen Schaden.
- **Aggro-Bruch**: Wenn du einen Feind angreifst, verlierst du sofort deine Schutzzonen-Immunität, auch wenn du dich tatsächlich in einer befindest.
- Ein Ring um jede Station und jedes Portal schützt dich, sobald seit deinem letzten Treffer 5 Sekunden und seit deinem letzten Schuss 15 vergangen sind. Solange er dich schützt und du nicht im Kampf bist, lässt dich das Hangar-Fenster dein Schiff wechseln, ohne das Spiel zu verlassen: siehe [Der Hangar im Flug](/wiki/03-Mechanics/Hangar.md).
- Stationen gibt es nur in den Heimatbasen (`x-1`). Die Gefahrensektoren (`DS-1` bis `DS-4`) haben keine: Dort sind die Ringe um die Portale die einzigen Schutzzonen.

### 3. Unter Beschuss in einem Gefahrensektor {#3-under-attack-in-a-danger-sector}

Ein Sprung durch ein Portal dauert 3 Sekunden (siehe [Reisen auf der Weltraumkarte](/wiki/01-General/Spacemap%20Travel.md)). In den Gefahrensektoren (`DS-1` bis `DS-4`) kann ein Pilot, dessen Schiff in den letzten **10 Sekunden** von einem anderen Piloten oder einem Alien getroffen wurde, keinen starten, und ein Treffer bricht einen laufenden Sprung ab. Überall sonst unterbrechen Angriffe nie einen Sprung, und nichts unterbricht das Einsammeln einer [Frachtkiste](/wiki/03-Mechanics/Cargo.md).

---

## Erholung & Reparatur {#recovery-repair}

Um sich vom Kampf zu erholen, können Piloten auf passive Regeneration und aktive Hilfsdrohnen setzen:

### 1. Passive Schildregeneration {#1-shield-passive-regeneration}

- **Funktion**: Stellt pro Sekunde so viele Schildpunkte wieder her, wie die Aufladerate deines Schilds beträgt.
- **Verzögerung**: Wird durch Kampf unterbrochen; die passive Regeneration setzt erst nach **15 Sekunden** ohne Schaden wieder ein.
- **Drohnenformationen**: Adamant und Redoubt geben jede Sekunde Schild zurück, auch im Kampf (siehe [Drohnenformationen](/wiki/03-Mechanics/Formations.md)).

### 1b. Siphon Battery

Die Munition [Siphon Battery](/wiki/06-Items/Lasers.md) schreibt den Schild, den sie einem Ziel entzieht, sofort deinem eigenen gut, bis zu deinem Maximum. Schild zu gewinnen ist kein erlittener Schaden, deshalb verzögert es deine passive Regeneration nicht.

### 2. Repair Drones (Hüllenreparatur) {#2-repair-drones-hull-repair-}

- **Funktion**: Rüstest du eine Repair Drone aus (unter den Extras im Hangar), schaltest du sie über die Aktionsleiste ein (zieh sie aus der Extras-Auswahl auf einen Slot), und sie repariert deine Hülle (HP). Jeder Treffer schaltet sie aus, und bei voller Hülle hört sie auf. Ist eine [Auto-Repair CPU](/wiki/06-Items/Extras.md#auto-repair-cpu) ausgerüstet, musst du die Repair Drone nicht erneut einschalten: Die CPU schickt sie von selbst los, sobald die Verzögerung weiter unten vorbei ist, es sei denn, du hast sie von Hand gestoppt.
- **Reparaturrate**: Stellt pro Sekunde einen Prozentsatz deiner maximalen Trefferpunkte wieder her (nur die beste ausgerüstete Drohne zählt, sie addieren sich nicht):
  - **Repair Drone I**: 1,5 % max. HP / s
  - **Repair Drone II**: 2,25 % max. HP / s
  - **Repair Drone III**: 3,5 % max. HP / s
  - **Repair Drone IV**: 5 % max. HP / s
- **Verzögerung**: Repair Drones beginnen erst nach **10 Sekunden** ohne Schaden, die Hülle auszubessern.
- **In einem Fähigkeits-Slot** repariert eine Repair Drone nicht von selbst: Sie gibt dir **Emergency Repair**, eine Schaltfläche, die über zehn Sekunden einen Anteil deiner maximalen Trefferpunkte heilt, auch unter Beschuss (siehe [Fähigkeiten](/wiki/03-Mechanics/Abilities.md)).

---

## Tarnung und der EMP {#cloaking-and-the-emp}

Ein Schuss braucht eine Zielerfassung. Zwei [Extras](/wiki/06-Items/Extras.md) entziehen deinem Schiff diese Zielerfassung:

- **Cloaking CPU**: Solange du getarnt bist (es gibt kein Zeitlimit), sehen Piloten anderer Konzerne, Aliens und Konzernpiloten dein Schiff nicht und können es nicht anvisieren; sie sehen einen einfachen roten Punkt auf der Minikarte dort, wo du bist. Deine erste Salve beendet die Tarnung, und du kannst dich eine Minute lang nicht erneut tarnen, auch nicht innerhalb von 10 Sekunden nach einem Treffer oder Schuss.
- **EMP Charge**: 3 Sekunden lang kann dich niemand anvisieren, und jede Zielerfassung, die schon auf dir liegt, bricht sofort ab. Sie beendet jede Tarnung im Umkreis von 1.500 Einheiten um den Piloten, der sie auslöst, außer denen seiner eigenen Gruppe. Sie verbirgt dich nicht, und sie ist keine Unverwundbarkeit: Sie stoppt, was eine Zielerfassung braucht.

Eine Rakete ist auch ein Schuss: Sie beendet deine eigene Tarnung, und der Flächenschaden der Rakete eines anderen trifft ein getarntes Schiff trotzdem und beendet dessen Tarnung, weil eine Explosion keine Zielerfassung braucht (siehe [Raketen](/wiki/06-Items/Rockets.md)). Der EMP stoppt aufgeschaltete Laser und gelenkte Raketen, keine Explosion.

Keines von beiden ändert einen Abschuss-Anspruch: Ein Anspruch ist die Vorgeschichte, wer ein Alien getroffen hat, keine Zielerfassung, und die Tarnung gibt deinen frei.
