<!-- wiki-i18n source: 0a2447734a603004 -->
<!-- wiki-i18n title: Spezialfähigkeiten -->
# Spezialfähigkeiten {#special-abilities}

<!-- wiki-search: special ability; special abilities; ability; abilities; mob; mobs; regenerate; mending; shield burst; hardened plating; plating; enrage; call reinforcements; reinforcements; clones; decoy; flee and return; flee; life drain; nova pulse; nova; rocket barrage; barrage; veil; sow mines; mines; split; fragments; boss steps; ladder; three steps; warning; tell; surprise; warlord; warden; leader; spezialfähigkeiten; regeneration; schildstoß; panzerhärtung; raserei; verstärkung rufen; klone; flucht und rückkehr; lebensentzug; nova-impuls; raketensalve; verschleierung; minen legen -->

Manche Aliens tragen eine **Spezialfähigkeit**: etwas, das sie einmal in ihrem Leben tun, wenn ihre Hülle zur Hälfte weg ist. Heilung, ein Schildstoß, eine Flucht, ein Hilferuf. Vorher zeigt sich nichts, jede Jagd kann also mit einer Überraschung enden. Diese Seite sagt, was jede Fähigkeit tut und wie du ihr begegnest. Die Bosse funktionieren anders: Sie ändern ihre Kampfweise in drei Schritten, während ihre Hülle sinkt, und die kleinen Aliens der letzten Stufe können in Bruchstücke zerfallen, wenn sie zu schnell zerstört werden.

## So funktioniert es {#how-it-works}

<!-- mob-rules:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Einmal.** Ein Alien mit einer Fähigkeit setzt sie einmal in seinem Leben ein: wenn in einem Kampf seine Hülle (nicht sein Schild) unter 50 % ihres Maximums fällt. Ein Treffer, der es von über dieser Grenze aus zerstört, lässt es nie feuern, und ein Alien, das in keinem Kampf ist, wartet, bis einer beginnt.
- **Erst eine Warnung.** Die Fähigkeit beginnt mit einer Warnung: ein Ring, der sich um das Schiff schließt, und ein Wort darüber. Eine Fähigkeit, deren Eintrag unten sagt, dass sie sofort beginnt, hat keine Warnung. Das Alien kann während der Warnung noch zerstört werden; dann geschieht nichts, und es zahlt wie sonst. Die leichten Arten (Seeker und Phantasm) sind schneller: Ihre Warnungen und ihre Wirkungen dauern nur 50 % so lang.
- **Vorher zeigt sich nichts.** Ein Alien mit einer Fähigkeit sieht bis ins Detail aus wie jedes andere, bis seine Warnung beginnt. Nichts im Spiel sagt, welches es ist, auch nicht der [Reiseführer](/wiki/03-Mechanics/Travelers-Guide.md).
- **Wer eine trägt.** Ein kleiner Teil der Aliens der Konzernsektoren und der Danger Sectors: je stärker die Stufe, desto größer der Anteil, und die Anführer der Schwärme (Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah und Boss Crystalys) tragen eher eine als die übrigen. Die Aliens der Deep Void, der Clan-Dungeons und der Solo-Tore tragen nie eine, ebenso wenig die Gefolgsleute eines Schwarms, die Wellen eines Wächters, die Dormant Force oder der Tesseract.
- **Es zahlt, was jedes Alien zahlt.** Ein Alien, das eine Fähigkeit einsetzt, zahlt, lässt fallen und zählt genau wie eines ohne: Die Fähigkeit fügt dem Abschuss nichts hinzu und kostet Zeit. Der Abschuss bleibt beim Piloten, der ihn hielt: Solange das Alien flieht, sich heilt oder sich verbirgt, läuft der Anspruch nicht ab.
- **Gerufene Schiffe und Kopien sind keine Abschüsse.** Die Schiffe, die ein Alien ruft, und die Kopien, die es macht, zahlen nichts, lassen nichts fallen und zählen für keine Quest, Statistik oder Rangliste. Höchstens 6 leben für einen Rufer und 24 auf einer Karte, und die eigenen Aliens der Karte kommen weiter pünktlich zurück.
- **Alle auf der Karte sehen es.** Die Piloten der Karte erfahren, wann eine Fähigkeit beginnt: Das Spiel zeichnet den Ring, das Wort und die Wirkung und spielt einen Ton.

<!-- mob-rules:end -->

## Die zwölf Fähigkeiten {#the-twelve-abilities}

Eine Fähigkeit beginnt mit einer **Warnung**, außer ihr Eintrag sagt, dass sie sofort beginnt: ein Ring, der sich um das Schiff schließt, und ein Wort darüber. Die Zeiten und Zahlen unten gelten für die schweren Arten. Wo eine Zahl mehrere Werte hat, gelten sie für die in Klammern genannten Stufen, den griechischen Buchstaben vor dem Namen eines Aliens.

<!-- mob-abilities:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

### Regeneration {#regenerate}

Es bleibt stehen und stellt über 6 s 15 % / 20 % / 25 % / 30 % (α / β / γ / δ) seiner Hülle und seines Schilds wieder her, und feuert dabei nichts. Schaden, der zusammen 10 % seiner Hülle und seines Schilds ausmacht, unterbricht es, und es behält, was es bis dahin hergestellt hat.

- **Warnung**: 1,5 s
- **Das Wort über dem Schiff**: HEILT
- **Getragen von**: jedes Alien
- **Antwort**: Mit Raketen oder vielen Schiffen niederbrennen, oder es während der Warnung zerstören.

### Schildstoß {#shield-burst}

Eine frische Schildschicht von 15 % / 20 % / 30 % / 40 % (α / β / γ / δ) seiner maximalen Hülle kommt auf seinen Schild. Solange sie steht, nimmt sie jeden Punkt eines Treffers auf; sie ist weg, wenn sie verbraucht ist oder nach 10 s.

- **Warnung**: 1 s
- **Das Wort über dem Schiff**: SCHILD HOCH
- **Getragen von**: jedes Alien
- **Antwort**: Munition und Raketen, die Schilde durchdringen, kommen besser durch. Oder schieß auf ein anderes Alien, bis sie weg ist.

### Panzerhärtung {#hardened-plating}

Für 7 s / 8 s / 10 s (β / γ / δ) nimmt es von jedem Treffer nur 50 %, Hülle und Schild gleichermaßen: doppelt so zäh. Es kämpft weiter, und die Zahlen deiner Treffer werden grau.

- **Warnung**: 1,5 s
- **Das Wort über dem Schiff**: PANZERT
- **Getragen von**: die schweren Arten (Bulwark, Goombah und Crystalys) und die schweren Schwarmanführer (Pirate Boss und Boss Phantasm), ab β
- **Antwort**: Abwarten, währenddessen ein anderes Alien treffen und die Stöße für danach aufsparen.

### Raserei {#enrage}

Für 10 s ist sein Schaden mit ×1,3 / ×1,4 / ×1,5 / ×1,75 (α / β / γ / δ) multipliziert und seine Geschwindigkeit mit ×1,25.

- **Warnung**: 1 s
- **Das Wort über dem Schiff**: RASEREI
- **Getragen von**: jedes Alien
- **Antwort**: Halte den Schild oben, bleib in Bewegung und außerhalb seiner Reichweite.

### Verstärkung rufen {#call-reinforcements}

4 / 6 (γ / δ) kleinere Aliens kommen vom nächsten Kartenrand herein, in 2 Wellen im Abstand von 3 s. Die Art, die kommt: Phantasm (gerufen von Bulwark und Goombah); Bulwark (gerufen von Crystalys). Zusammen haben sie 45 % / 60 % (γ / δ) seiner Hülle und seines Schilds und feuern 50 % seiner Salve. Sie zahlen nichts, lassen nichts fallen und zählen für nichts, und sie gehen nach 45 s oder wenn der Rufer zerstört wird.

- **Warnung**: 2 s
- **Das Wort über dem Schiff**: RUFT HILFE
- **Getragen von**: die schweren Arten (Bulwark, Goombah und Crystalys) und die schweren Schwarmanführer (Boss Phantasm und Boss Goombah), ab γ
- **Antwort**: Zerstöre den Rufer: Seine Schiffe gehen mit ihm. Eine Waffe mit Flächenwirkung räumt sie ab.

### Klone {#clones}

3 (γ / δ) Kopien von ihm erscheinen um es herum, mit seinem Namen und seinem Aussehen. Zusammen haben sie 18 % (γ / δ) seiner Hülle und seines Schilds; sie feuern nichts und zahlen nichts, und sie halten 15 s oder bis das echte zerstört wird. Das echte trägt einen dünnen Ring, solange die Kopien da sind, und das Zielfenster nennt eine Kopie Attrappe.

- **Warnung**: 1 s
- **Das Wort über dem Schiff**: KLONT
- **Getragen von**: jedes Alien, ab γ
- **Antwort**: Folge dem Ring und der sich bewegenden Hüllenleiste des echten, oder nimm eine Waffe mit Flächenwirkung.

### Flucht und Rückkehr {#flee-and-return}

Es fliegt mit ×2 Geschwindigkeit für 5 s / 6 s / 7 s / 8 s (α / β / γ / δ) von seinen Angreifern weg und wendet sich dann gegen den ersten Piloten, der es getroffen hat. Es verlässt nie die Karte und betritt keine Schutzzone, es kann die ganze Zeit getroffen werden, und der Pilot, der seinen Abschuss hielt, behält ihn.

- **Warnung**: 0,5 s
- **Das Wort über dem Schiff**: FLIEHT
- **Getragen von**: jedes Alien
- **Antwort**: Jage es, oder triff es mit Raketen, während es fliegt.

### Lebensentzug {#life-drain}

Für 10 s feuert es sonst nichts: Einmal pro Sekunde saugt es jedes Schiff in seiner Reichweite mit einer vollen Salve aus, der nichts ausweicht, und heilt 75 % / 100 % / 100 % (β / γ / δ) des Schadens, den es anrichtet, höchstens 20 % seiner Hülle insgesamt.

- **Warnung**: 1 s
- **Das Wort über dem Schiff**: SAUGT
- **Getragen von**: die schweren Arten (Bulwark, Goombah und Crystalys) und die schweren Schwarmanführer (Pirate Boss, Boss Phantasm, Boss Goombah und Boss Crystalys), ab β
- **Antwort**: Einen Felsen oder eine Wand in die Linie bringen, tarnen oder aus seiner Reichweite fliegen.

### Nova-Impuls {#nova-pulse}

Ein Ring wächst während der Warnung auf dem Boden um es. Ist der Ring voll, trifft er jedes Schiff darin einmal, mit 4 / 5 (γ / δ) seiner Salven. Sein Radius in Einheiten ist 700 / 800 (γ / δ).

- **Warnung**: 2,5 s
- **Das Wort über dem Schiff**: NOVA
- **Getragen von**: die schweren Arten (Bulwark, Goombah und Crystalys) und die schweren Schwarmanführer (Pirate Boss, Boss Phantasm und Boss Goombah), ab γ
- **Antwort**: Flieg aus dem Ring, bevor er sich füllt: Es ist der eine Stoß, dem du ausweichen kannst.

### Raketensalve {#rocket-barrage}

Über 3 s feuert es 4 / 6 / 8 (β / γ / δ) [Rivet-Raketen](/wiki/06-Items/Rockets.md#the-twelve-rockets) auf sein Ziel: Rivet I / II / II (β / γ / δ). Sie fliegen geradeaus und werden nicht gelenkt.

- **Warnung**: 1,5 s
- **Das Wort über dem Schiff**: SALVE
- **Getragen von**: die schweren Arten (Bulwark, Goombah und Crystalys) und die schweren Schwarmanführer (Boss Phantasm und Boss Goombah), ab β
- **Antwort**: Bleib in Bewegung: Die Raketen fliegen geradeaus. Ein Felsen im Weg hält sie auf.

### Verschleierung {#veil}

Für 6 s / 8 s (γ / δ) kann ein Schiff, das weiter als 700 Einheiten von ihm entfernt ist, es nicht anvisieren, und eine gehaltene Zielerfassung geht verloren. Näher als das wird es wie gewohnt gesehen. Es kämpft weiter, und eine Explosion trifft es trotzdem.

- **Warnung**: keine, es beginnt sofort.
- **Das Wort über dem Schiff**: TARNT
- **Getragen von**: die schweren Arten (Bulwark, Goombah und Crystalys) und die schweren Schwarmanführer (Pirate Boss, Boss Phantasm, Boss Goombah und Boss Crystalys), ab γ
- **Antwort**: Geh bis auf 700 Einheiten heran.

### Minen legen {#sow-mines}

Es legt 4 / 6 / 8 (β / γ / δ) Minen auf einen Ring von 500 Einheiten um die Stelle, an der sein Ziel stand. Eine Mine ist 3 s nach der Landung scharf, hält 30 s und geht einmal los, unter dem ersten Pilotenschiff, das darüber fliegt, mit 2 / 3 / 3 (β / γ / δ) der Salven des Aliens. Eine Mine verletzt nie ein Alien.

- **Warnung**: 1,5 s
- **Das Wort über dem Schiff**: VERMINT
- **Getragen von**: die schweren Arten (Bulwark, Goombah und Crystalys) und die schweren Schwarmanführer (Pirate Boss, Boss Phantasm, Boss Goombah und Boss Crystalys), ab β
- **Antwort**: Flieg um sie herum: Sie sind auf dem Boden eingezeichnet und werden spät scharf.


<!-- mob-abilities:end -->

## Aufspaltung {#splitting}

<!-- mob-split:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Die kleinen Aliens der letzten Stufe können zerfallen, wenn sie zu schnell zerstört werden. Das gilt für Seeker, Phantasm, Bulwark, Goombah und Crystalys der Stufe δ und für kein anderes Alien, und es ist keine der Fähigkeiten oben: Ein Alien kann beides haben.

- **Wann**: Ein Pilot zerstört es innerhalb von 5 s nach dem ersten Schaden, den es nahm. Nicht jedes Alien, das so schnell stirbt, zerfällt.
- **Was herauskommt**: 3 Aliens derselben Art und Stufe, 70 % seiner Größe, jedes mit 25 % seiner Hülle und seines Schilds und einer vollen Salve, um die Stelle, an der es zerstört wurde. Sie gehen auf den Piloten los, der es zerstört hat, und gehen nach 180 s.
- **Es sind gewöhnliche Aliens**: Jedes zahlt, was seine Art zahlt, lässt fallen, was sie fallen lässt, und zählt für Quests und Statistiken. Sie tragen keine Fähigkeit und zerfallen nie.
- **Grenzen**: Höchstens 60 Bruchstücke leben auf einer Karte, und sie halten die eigenen Aliens der Karte nicht auf.
- **Was das bedeutet**: Eine Crew, die ihre Aliens schnell genug zerstört, kann bis zu 4 Abschüsse aus einem Alien holen. Eine Crew, die das nicht tut, bekommt davon nichts.

<!-- mob-split:end -->

## Die drei Schritte der Bosse {#the-bosses-three-steps}

Jeder Boss ändert seine Kampfweise in drei Schritten: wenn der Kampf beginnt, wenn seine Hülle unter zwei Drittel fällt und wenn sie unter ein Drittel fällt. Ein Schritt geschieht einmal und nie wieder rückwärts, außer wenn der Boss von vorn beginnt, wie unten steht.

<!-- mob-ladders:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

- **Eine Pause bei jedem Schritt.** Beginnt nach dem ersten ein Schritt, der etwas bewirkt, kann der Boss 1,5 s lang nicht verletzt werden (3 s beim Dungeon-Warlord und den Bossen der Solo-Tore).
- **Auch eine Spezialfähigkeit.** Pirate Boss, Boss Seeker, Boss Phantasm, Boss Goombah und Boss Crystalys können zusätzlich eine Spezialfähigkeit tragen (Dormant Force und Tesseract nie): Sie kommt zwischen dem zweiten und dem dritten Schritt; würden beide gleichzeitig beginnen, wartet der spätere höchstens 3 s. Es ist nie eine Fähigkeit, die die Schritte des Anführers selbst nutzen.
- **Von vorn.** Der Tesseract beginnt seine Schritte von vorn, sobald er sich ganz geheilt hat.

### Die Schwarmanführer {#the-swarm-leaders}

| Anführer | Am Anfang | Unter zwei Dritteln | Unter einem Drittel |
| :--- | :--- | :--- | :--- |
| **Pirate Boss** | Feuert einen Fächer aus 3 Raketen im Abstand von 12 Grad auf den ersten Piloten, der es getroffen hat. | Ruft 5 weitere Pirate Scouts auf einmal, höchstens 10 am Leben. Sie zahlen nichts und gehen nach 45 s. | Fliegt mit ×1,8 Geschwindigkeit für 10 s zum nächsten Tor und wendet sich dann gegen die Piloten. |
| **Boss Seeker** | Seine Seeker Slaves heilen es ×2 so schnell für 8 s. | 2 Kopien von ihm erscheinen, und das echte trägt einen Ring. | Fliegt für 4 s von den Piloten weg und wendet sich dann wieder zu. |
| **Boss Phantasm** | Jeder seiner Phantasm Guards baut eine Schildschicht von 10 % der eigenen Hülle auf. | 3 Kopien von ihm erscheinen, und das echte trägt einen Ring. | Springt etwa 2.500 Einheiten von den Piloten weg, und seine Phantasm Guards kommen heil um es zurück. |
| **Boss Goombah** | Nimmt für 6 s nur 50 % von jedem Treffer. | Sein Schaden ist für 10 s mit ×1,5 multipliziert und seine Geschwindigkeit mit ×1,25. | Heilt 25 % seiner Hülle und seines Schilds (ein Schadensstoß unterbricht es), und seine Goombah Guards heilen es währenddessen ×2 so schnell. |
| **Boss Crystalys** | Nimmt für 8 s nur 50 % von jedem Treffer. | Ein Ring von 700 Einheiten trifft jedes Schiff darin mit 4 seiner Salven, und es feuert 4 Raketen. | Heilt 20 % seiner Hülle und seines Schilds (ein Schadensstoß unterbricht es), und 3 weitere Crystalys Guards kommen, höchstens 6 am Leben. |
| **Dormant Force** | Nimmt 70 % von jedem Treffer, solange einer seiner Dormant Pulses lebt. | Seine Dormant Pulses feuern für 15 s alle 2,5 s eine Rakete. | Solange alle seine Dormant Pulses leben, heilen sie es 6 s lang um 5 % seiner Hülle pro Sekunde. |
| **Tesseract** | – | 20 weitere Facets kommen auf einmal, über ihrer üblichen Zahl. | – |

### Die Clan-Wächter {#the-clan-wardens}

| Wächter | Am Anfang | Unter zwei Dritteln | Unter einem Drittel |
| :--- | :--- | :--- | :--- |
| **Brood Warden** (I, II, III) | Alle 4 Drohnen kommen auf einmal an seine Seite. | Seine Drohnen heilen es für 15 s ×1,5 so schnell. | 2 weitere Drohnen kommen, über ihrer üblichen Zahl, für 30 s. Sie zahlen nichts. |
| **Siege Warden** (I, II, III) | – | Feuert seine Rakete für 20 s ×2 so oft. | Heilt 15 % seiner Hülle und seines Schilds (ein Schadensstoß unterbricht es). |
| **Wrath Warden** (I, II, III) | – | Seine Laser treffen ×1,25 so hart. | Seine Laser treffen insgesamt ×1,5 so hart, nicht zusätzlich zum Schritt davor. |

### Der Dungeon-Warlord {#the-dungeon-warlord}

- **Unter zwei Dritteln**: Die Pause zwischen seinen Fähigkeiten sinkt auf 4 s und ihre Wartezeiten auf ×0,75.
- **Unter einem Drittel**: Die Pause sinkt auf 2 s, die Wartezeiten auf ×0,5 und sein Schaden steigt auf ×1,25; es wirkt eine freie Meteor-Salve, und sein Swarm kommt nie schneller zurück als alle 120 s.
- **Eine Pause bei jedem Schritt.** Beginnt ein Schritt, kann der Warlord 3 s lang nicht verletzt werden.

### Die Bosse der Solo-Tore {#the-solo-gate-bosses}

Die sechs Bosse der Solo-Tore haben ebenfalls drei Schritte, ihre Phasen: Sie stehen in der Tabelle [der Bosse](/wiki/03-Mechanics/Solo-Gates.md#the-bosses) des Artikels Solo-Tore.

<!-- mob-ladders:end -->

## Mehr dazu {#where-to-read-more}

- [Kampf](/wiki/03-Mechanics/Combat.md#who-an-alien-fights): gegen wen ein Alien kämpft und wer seinen Abschuss bekommt.
- [Schwärme](/wiki/05-Swarms/Swarms.md): die Anführer und ihre Schritte, ein Artikel für jeden Schwarm.
- [Clan-Warden](/wiki/03-Mechanics/Clans.md#fighting-a-warden), der [Dungeon-Warlord](/wiki/03-Mechanics/Dungeons.md#the-warlord) und die [Bosse der Solo-Tore](/wiki/03-Mechanics/Solo-Gates.md#the-bosses).
- [Reiseführer](/wiki/03-Mechanics/Travelers-Guide.md): was du über ein Alien gelernt hast. Er sagt nie, welches eine Fähigkeit trägt.
