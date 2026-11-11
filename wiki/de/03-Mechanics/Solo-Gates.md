<!-- wiki-i18n source: 4d2749864875137f -->
<!-- wiki-i18n title: Solo-Tore -->
# Solo-Tore {#solo-gates}

<!-- wiki-search: solo gates; solo gate; gate; gates; galaxy gates; rift; rifts; alpha rift; beta breach; gamma foundry; delta siege; omega vault; chrono gate; chrono-gate; materializer; energy materializer; scan; spin; gate part; gate parts; guarantee; pity; consolation; wave; waves; nuke wave; skip; boss; lives; resume; abandon; speedrun; no death; challenge; achievement; thulium cap; solo-tore; solo-tor; galaxietore; torteil; torteile; energie-materialisator; scan; garantie; welle; wellen; leben; fortsetzen; aufgeben; ohne tod; herausforderung; erfolg; thulium-obergrenze -->

Die **Solo-Tore** sind fünf Tore der Galaxietore, die du allein fliegst: **Alpha Rift**, **Beta Breach**, **Gamma Foundry**, **Delta Siege** und **Omega Vault**. Jedes ist eine leere Arena für sich, in der Wellen von Aliens nacheinander auf dich zukommen und am Ende ein Boss wartet. Du baust ein Tor mit seinen **Teilen**, die du findest, indem du den Energie-Materialisator mit Thulium scannst, und ein Abschluss zahlt Credits, Thulium, Erfahrung, Ehre, Erz, Platten und Munition.

Ein Solo-Tor ist kein [Clan-Dungeon](/wiki/03-Mechanics/Dungeons.md). Ein Dungeon ist ein Labyrinth, das ein Clan für eine Gruppe öffnet, mit einem Kriegsherrn an seinem Ende; ein Solo-Tor ist eine Arena, in der nur du bist und in die niemand sonst mit dir hineinkann. Beide haben getrennte Regeln, Auszahlungen und Grenzen. Die Seite Galaxietore hat auch das **Chrono-Gate**, das kein Ort zum Fliegen ist, sondern das Tor, das für den Wipe deinen [Transport-Cache](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) öffnet: Seine Teile werden mit denselben Scans gefunden.

## Auf einen Blick {#at-a-glance}

<!-- solo-glance:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Tore**: 6: das Chrono-Gate und 5 Solo-Tore, Alpha Rift, Beta Breach, Gamma Foundry, Delta Siege und Omega Vault
- **Scan**: 100 Thulium pro Scan und 1, 5, 10 oder 100 Scans auf einmal
- **Chance auf ein Teil**: 13 % pro Scan. Das Tor, zu dem das Teil gehört, wird per Zufall gewählt, und jedes Tor bekommt 2,17 % der Scans. Ist das Chrono-Gate komplett, scheidet sein Anteil aus dem Rad aus, und die Solo-Tore behalten je 2,17 %
- **Garantie**: Nach 24 Scans in Folge ohne Teil steigt die Chance mit jedem Scan, und nach 47 findet der nächste Scan immer eines. Ein Teil eines beliebigen Tors beginnt die Zählung von vorn
- **Leben**: 3 pro Versuch; jeder Tod kostet eines
- **Countdown**: 5 s vor jeder Welle, auch vor der ersten und vor der des Bosses. Eine Welle hat keinen Timer und ein Lauf auch nicht
- **Arena**: Freier Raum von 8.000 × 6.000 Einheiten ohne Felsen, und du bist allein darin. Eine Welt hat 16 davon, und wenn alle belegt sind, kannst du nicht hinein
- **Aliens gleichzeitig**: Höchstens 60 einer Welle leben gleichzeitig, und 250 in einer optionalen Welle. Die übrigen warten auf Platz
- **Bosse**: Ein Boss kann 3 s lang nicht verletzt werden, wenn er die Phase wechselt
- **Thulium-Obergrenze**: Ein Tor zahlt höchstens 50 % des Thuliums zurück, das du für Scans ausgegeben hast. Der Rest wird gekappt, und das Ergebnis sagt, wie viel

<!-- solo-glance:end -->

## Torteile finden {#finding-gate-parts}

Öffne die Seite **Galaxietore** und scanne mit dem Energie-Materialisator. Jeder Scan wird in Thulium bezahlt und findet höchstens ein Teil, und das Teil gehört zu einem der sechs Tore, per Zufall gewählt. Du brauchst eine Anzahl Teile eines Tors, um es zu bauen, und die Teile gehören dir, bis du sie einsetzt. Ein Scan ohne Teil ist nicht verloren: Er zahlt eine Belohnung ([unten](#a-spin-without-a-part)). Jeder Scan wird berechnet, auch bei einem fertigen Chrono-Gate. Ist das Chrono-Gate komplett, findet sein Anteil an den Scans nichts, und die Solo-Tore behalten ihre eigene Chance, ein Teil eines Solo-Tors kostet also mit oder ohne es dasselbe.

Die Tabelle gibt die Kosten jedes Tors in Teilen und was sie im Schnitt **mit der Garantie** kosten (ein Scan ist eine Lotterie, ein glücklicher Pilot zahlt also weniger und ein unglücklicher mehr, bis zur längsten Reihe von Scans, die die Garantie zulässt).

<!-- solo-parts:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Tor | Teile bis zum Abschluss | Chance auf ein Teil pro Scan | Scans im Schnitt | Thulium im Schnitt |
| :--- | ---: | ---: | ---: | ---: |
| **Chrono-Gate** | 2 | 2,17 % | 91 | 9.093 |
| **Alpha Rift** | 11 | 2,17 % | 500 | 50.011 |
| **Beta Breach** | 26 | 2,17 % | 1.182 | 118.208 |
| **Gamma Foundry** | 54 | 2,17 % | 2.455 | 245.508 |
| **Delta Siege** | 87 | 2,17 % | 3.955 | 395.541 |
| **Omega Vault** | 108 | 2,17 % | 4.910 | 491.017 |

<!-- solo-parts:end -->

Die Teile des Chrono-Gates fallen beim Wipe auf null zurück, und du findest sie jede Saison neu. **Die Teile der Solo-Tore bleiben**, ebenso der Zähler der Garantie und die Aufzeichnung dessen, was du für Scans ausgegeben hast und was die Tore zurückgezahlt haben; der Wipe nimmt nichts davon ([Tore und der Wipe](#gates-and-the-wipe)).

### Ein Scan ohne Teil {#a-spin-without-a-part}

Die meisten Scans finden kein Teil. Jeder von ihnen zahlt eine Belohnung, gewählt nach den Chancen unten: Laser-Munition des zweiten Multiplikators oder besser, einen Raketenstapel der zweiten oder dritten Stufe und hin und wieder einen [Spezialgegenstand](/wiki/06-Items/Special-Items.md) oder einen [Container](/wiki/06-Items/Containers.md). Eine Belohnung, die nicht gegeben werden kann (du besitzt zum Beispiel schon die Höchstzahl dieses Spezialgegenstands), wird mit demselben Wurf zu einem Stapel Munition oder Raketen, ein Scan zahlt also nie weniger als seine Tabelle. Die Belohnung ist deutlich weniger wert, als der Scan kostet: Die Tore sind eine Thulium-Senke.

<!-- solo-prizes:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Belohnung | Chance pro Scan |
| :--- | ---: |
| Ein Container: Chroma Archive | 0,01 % |
| Ein Spezialgegenstand: Magic Hammer | 0,2 % |
| Ein Spezialgegenstand: Schematics | 0,2 % |
| Ein Spezialgegenstand: Philosopher's Stone | 0,2 % |
| Ein Spezialgegenstand: Forger's Seal | 0,2 % |
| Ein Spezialgegenstand: Workforce Contract | 0,2 % |
| Ein Spezialgegenstand: Tinkerer's Badge | 0,1 % |
| Laser-Munition: Advanced Plasma ×75 | 12,88 % |
| Laser-Munition: Antimatter Battery I ×62 | 8,59 % |
| Laser-Munition: Ultra Core ×40 | 8,59 % |
| Laser-Munition: Antimatter Battery II ×29 | 4,29 % |
| Laser-Munition: Dark Matter Ammo I ×31 | 4,29 % |
| Laser-Munition: Experimental Fusion Core ×17 | 2,15 % |
| Laser-Munition: Dark Matter Ammo II ×17 | 2,15 % |
| Raketen: Lancet II ×4 | 8,59 % |
| Raketen: Rivet II ×4 | 8,59 % |
| Raketen: Ember II ×4 | 8,59 % |
| Raketen: Scatter II ×4 | 8,59 % |
| Raketen: Lancet III ×1 | 2,15 % |
| Raketen: Rivet III ×1 | 2,15 % |
| Raketen: Ember III ×1 | 2,15 % |
| Raketen: Scatter III ×1 | 2,15 % |

<!-- solo-prizes:end -->

## Hineingehen {#going-in}

Du **baust** ein Tor auf der Seite Galaxietore und **springst** durch sein Portal hinein. Das Bauen geht von der Station aus, mit angedocktem Schiff: Du musst nicht fliegen. Es braucht:

- die Teile des Tors: Sie werden **einmal beim Bauen** genommen, und ein abgelehntes Bauen nimmt nichts;
- keinen anderen offenen Solo-Lauf: Du hast einen Lauf zugleich, und ein Lauf, den du verlassen hast, wird wieder durch sein Portal betreten oder aufgegeben, bevor du ein anderes Tor baust;
- den Heimserver (die regionalen Server haben keine Tore).

Das gebaute Tor steht in deinem **Heimatsektor** (`M-1`, `T-1` oder `G-1`, je nach deinem Konzern) als ein nach ihm benanntes Portal, und die Seite Galaxietore sagt dir, wo es steht. **Starte, fliege zum Portal und springe** hindurch wie durch jedes Portal. Ein Rift in deiner Welt muss frei sein, wenn du hineingehst: Jede Welt hat eine Anzahl davon, und wenn alle belegt sind, wartest du.

Du landest allein in der Mitte einer leeren Arena. Niemand kann dich darin angreifen, und die Jump CPU und die Base CPU funktionieren nicht.

## Wie ein Lauf abläuft {#how-a-run-goes}

1. **Vor jeder Welle kommt ein Countdown**, auch vor der ersten und vor der des Bosses. Eine Welle hat keinen Timer und der Lauf auch nicht: Er dauert so lange, wie du brauchst.
2. **Eine Welle** erscheint auf einem Ring um dich und fliegt auf dich zu, im Tempo des Tors. Nur so viele von ihr leben gleichzeitig, und die übrigen warten auf Platz. Sie endet, wenn ihr letztes Alien tot ist.
3. **Dein Fortschritt wird nach jeder Welle gespeichert.** Wenn du gehst, beginnt eine laufende Welle bei deiner Rückkehr wieder ganz von vorn.
4. **Eine optionale Welle** ist eine riesige Welle Seeker, und Delta Siege und Omega Vault haben je eine. Während ihres Countdowns kannst du sie überspringen: Sie gilt dann als erledigt und zahlt **nichts**. Kämpfst du sie, zahlen ihre Abschüsse wie die jeder Welle.
5. **Die letzte Welle ist der Boss.** Er wechselt die Phase, wenn seine Hülle fällt, und bei jedem Wechsel kann er einen Moment lang nicht verletzt werden. Stirbt der Boss, ist der Lauf abgeschlossen, und der Abschluss wird sofort ausgezahlt.

**Leben.** Ein Tod kostet ein Leben und schickt dich wie jeder andere Tod zu deiner Basis; der Lauf wartet auf dich, ohne dass eine Uhr läuft. Solange der Lauf offen ist und du außerhalb der Arena bist, steht **das Portal deines Tors in deinem Heimatsektor**, und ein Sprung hindurch bringt dich wie **Fortsetzen** mit den Leben, die du noch hast, in der gespeicherten Welle wieder hinein; es verlangt keine neuen Teile. Ist dein letztes Leben weg, endet der Versuch, aber der Lauf bleibt bei der letzten abgeschlossenen Welle offen, und das erneute Hineingehen füllt deine Leben wieder auf. **Verlassen**, ein Abmelden oder ein Weltwechsel hält den Lauf an, ohne ein Leben zu kosten. Ein Neustart des Servers hält deinen Lauf ebenfalls offen. **Aufgeben** gibt den Lauf auf: Seine Teile sind weg, und die Aliens, die du getötet hast, werden so bezahlt, wie sie stehen. **Fortsetzen** geht nur mit einem fliegenden Schiff: Nach einem Tod wartet die Schaltfläche auf dem Ergebnisbildschirm, mit einer Zeile, die sagt warum, bis du wieder respawnt hast. Ein respawntes Schiff kehrt mit begrenzter Hülle zurück; liegt deine Hülle unter der Hälfte, warnt dich der Ergebnisbildschirm, und **Fortsetzen** bringt dich trotzdem so zurück, wie du bist. Die Reparaturschiffe an deiner Basis reparieren dich innerhalb ihrer Aura.

Jede Welt kämpft dasselbe Tor: Stärke und Auszahlung der Aliens hängen nicht von der Welt ab, in der du fliegst.

### Die Wellen {#the-waves}

Die Aliens sind die des Spiels (Seeker, Phantasm, Bulwark, Goombah und Crystalys), vom Tor härter oder weicher gemacht. Die geplante Zeit ist die, die das Tor für einen Piloten auf dem Startlevel der Lasertechnik vorsieht ([Pilotenfertigkeiten](/wiki/03-Mechanics/Pilot-Skills.md)); ein Pilot, der seine Lasertechnik gesteigert hat, ist früher fertig.

<!-- solo-waves:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Tor | Wellen, die des Bosses eingeschlossen | Aliens in den Wellen | Boss | Geplante Zeit |
| :--- | ---: | :--- | :--- | :--- |
| **Alpha Rift** | 10 | 60 Seeker, 160 Phantasm | Enhanced Phantasm | 10 bis 15 min |
| **Beta Breach** | 14 | 80 Seeker, 180 Phantasm, 80 Bulwark, 20 Goombah | Enhanced Bulwark | 15 bis 25 min |
| **Gamma Foundry** | 18 | 100 Phantasm, 120 Bulwark, 100 Goombah, 8 Crystalys | Elite Crystalys | 25 bis 35 min |
| **Delta Siege** | 22 | 250 Seeker, 200 Phantasm, 180 Bulwark, 140 Goombah, 15 Crystalys | Siege Construct | 35 bis 45 min |
| **Omega Vault** | 26 | 250 Seeker, 250 Phantasm, 200 Bulwark, 200 Goombah, 25 Crystalys | Omega Guardian | 50 bis 60 min |

- **Delta Siege**: Welle 18 (250 Seeker) ist optional: Du kannst sie überspringen, solange ihr Countdown läuft, und sie zahlt nichts
- **Omega Vault**: Welle 17 (250 Seeker) ist optional: Du kannst sie überspringen, solange ihr Countdown läuft, und sie zahlt nichts; die Wellen 22 bis 24 sind Elite, mit ×1,5 Hülle, Schild und Schaden

<!-- solo-waves:end -->

### Die Bosse {#the-bosses}

Ein Boss ist das Schiff eines Aliens, vergrößert, mit einer eigenen Hülle, einem eigenen Schild und einer eigenen Salve, die keine Einstellung des Tors oder der Welt ändert. Eine Phase beginnt, wenn die Hülle des Bosses auf die Zahl in der Tabelle fällt: Sein Schild kann neu gesetzt werden, seine Salve oder sein gesamter Schaden ändern sich, und er kann eine Bewegung beginnen. Jede Bewegung wird angekündigt: Ein Kreis, ein Ring oder eine Markierung auf deinem Schiff zeigt einen Moment vor dem Einschlag, wohin es geht. Die Aliens, die ein Boss ruft, zahlen nichts und lassen nichts fallen.

<!-- solo-bosses:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Boss | Tor | Hülle | Schild | Laser-Salve |
| :--- | :--- | ---: | ---: | ---: |
| **Enhanced Phantasm** | Alpha Rift | 330.000 | 530.000 | 5.700–7.000 |
| **Enhanced Bulwark** | Beta Breach | 690.000 | 170.000 | 4.500–5.500 |
| **Elite Crystalys** | Gamma Foundry | 620.000 | 250.000 | 3.800–4.700 |
| **Siege Construct** | Delta Siege | 1.150.000 | 1.730.000 | 3.400–4.200 |
| **Omega Guardian** | Omega Vault | 1.340.000 | 840.000 | 2.600–3.200 |

| Boss | Phase | Verbleibende Hülle | Was er tut |
| :--- | :--- | :--- | :--- |
| **Enhanced Phantasm** | Enhanced Phantasm | 100 % bis 0 % | Er schießt nur. |
| **Enhanced Bulwark** | Shielded | 100 % bis 50 % | Sein Schild wird auf ×4 des eigenen Schilds des Bosses gesetzt. |
|  | Second attack | 50 % bis 0 % | Seine Salve ist ×1,3. Er feuert 4 Raketen Dormant Lance auf dich ab, je 61.000, eine alle 0,5 s, in einer Salve alle 30 s. |
| **Elite Crystalys** | Elite | 100 % bis 50 % | Er schießt nur. |
|  | Reinforced | 50 % bis 0 % | Sein Schild wird auf ×2 des eigenen Schilds des Bosses gesetzt. Alle 10 min ruft er 10 Goombah herbei, höchstens 10 davon am Leben; sie zahlen nichts und lassen nichts fallen. |
| **Siege Construct** | Siege Construct | 100 % bis 0 % | Alle 1 min lässt er 3 Salven von 8 Meteoren niedergehen, je 5.500 auf alles im Umkreis von 420 Einheiten um den Einschlag, 50 % davon auf dich gezielt; jeder Kreis zeigt 3 s vor dem Einschlag. Er feuert 6 Raketen Dormant Lance auf dich ab, je 9.000, eine alle 0,5 s, in einer Salve alle 1 min. |
| **Omega Guardian** | Shield Fortress | 100 % bis 70 % | Sein Schild wird auf ×1,5 des eigenen Schilds des Bosses gesetzt. Alle 40 s ruft er 6 Bulwark herbei, höchstens 12 davon am Leben; sie zahlen nichts und lassen nichts fallen. |
|  | Swarm Protocol | 70 % bis 35 % | Alle 25 s ruft er 12 Phantasm herbei, höchstens 24 davon am Leben; sie zahlen nichts und lassen nichts fallen. Alle 30 s trifft eine Explosion von 140.000 alles im Umkreis von 700 Einheiten um den Boss; der Ring zeigt 2 s vor dem Einschlag. |
|  | Overload | 35 % bis 0 % | Sein Schild wird auf ×0,1 des eigenen Schilds des Bosses gesetzt. Sein gesamter Schaden ist ×2,5. Nach 2 min in der Phase wird sein gesamter Schaden noch einmal mit ×2 multipliziert. Alle 25 s trifft eine Explosion von 28.000 alles im Umkreis von 700 Einheiten um den Boss; der Ring zeigt 2 s vor dem Einschlag. |

<!-- solo-bosses:end -->

## Was ein Abschluss zahlt {#what-a-clear-pays}

Ein Abschluss zahlt seine Tabelle **einmal**, auf einen Schlag, in dem Moment, in dem der Boss stirbt: die Credits, das Thulium, die Erfahrung und die Ehre, das Erz, die Platten und Power Cores und die Munition. Die Erfahrung zählt für deine PvE-Rangpunkte, wie die eines Dungeons.

<!-- solo-pay:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Tor | Credits | Thulium | EP | Ehre |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 450.000 | 5.000 | 70.000 | 1.000 |
| **Beta Breach** | 1.500.000 | 12.000 | 180.000 | 2.500 |
| **Gamma Foundry** | 4.000.000 | 25.000 | 400.000 | 5.500 |
| **Delta Siege** | 8.000.000 | 40.000 | 800.000 | 10.000 |
| **Omega Vault** | 15.000.000 | 60.000 | 1.500.000 | 20.000 |

- **Alpha Rift**: Ship Fragment ×300, Nyxite ×300, Daraxium ×400; Munition: Advanced Plasma ×20.000, Ultra Core ×5.000, Experimental Fusion Core ×20.000
- **Beta Breach**: Ship Fragment ×700, Nyxite ×750, Daraxium ×800, Cataclysite ×400, Quorvium ×100; Munition: Advanced Plasma ×50.000, Ultra Core ×20.000, Experimental Fusion Core ×30.000
- **Gamma Foundry**: Ship Fragment ×1.150, Nyxite ×1.000, Cataclysite ×900, Quorvium ×400, Power Core ×15; Munition: Advanced Plasma ×30.000, Ultra Core ×60.000, Experimental Fusion Core ×50.000
- **Delta Siege**: Ship Fragment ×2.000, Nyxite ×1.750, Cataclysite ×1.500, Quorvium ×1.000, Reinforced Hull Plate ×70, Power Core ×40, Ancient Control Unit ×3; Munition: Advanced Plasma ×40.000, Ultra Core ×90.000, Experimental Fusion Core ×75.000
- **Omega Vault**: Ship Fragment ×3.250, Nyxite ×2.750, Cataclysite ×2.250, Quorvium ×1.600, Reinforced Hull Plate ×150, Power Core ×80, Ancient Control Unit ×10; Munition: Advanced Plasma ×50.000, Ultra Core ×100.000, Experimental Fusion Core ×100.000

<!-- solo-pay:end -->

**Das Thulium wird auf eine Obergrenze gekappt.** Die Tore dürfen nicht mehr als einen Anteil des Thuliums zurückzahlen, das du für Scans ausgegeben hast, gezählt über alle deine Tore und alle deine Scans (der Anteil steht in der Liste ganz oben). Was ein Abschluss und seine Aliens darüber hinaus zahlen würden, wird gekappt, und der Ergebnisbildschirm sagt, wie viel. Credits, Erfahrung, Ehre, Erz, Platten und Munition werden nie gekappt.

### Die Aliens {#the-aliens}

Jedes Alien, das du in einem Tor tötest, zahlt mit den Zahlen, die es in Alpha hat, in welcher Welt du auch fliegst: Kein Weltmultiplikator, kein Booster und kein Premium-Bonus ändert sie. Eine Welle zahlt für ihre Aliens **einmal** je Lauf, wie oft du auch gehst und zurückkommst. Die Auszahlung kommt mit dem Ende jedes Abschnitts des Laufs: wenn du gehst, stirbst, keine Leben mehr hast, aufgibst oder abschließt. Die Abschüsse eines Abschnitts bleiben nur beim Wipe und bei einem Neustart des Servers unbezahlt, während du drin bist (dein Lauf bleibt offen, aber die Abschüsse dieses Abschnitts gehen verloren). Die Abschüsse in einem Tor zählen für nichts anderes: nicht für die Missionen, die Abschussstatistik, die Zähler der Erfolge, den Kill-Feed oder die Erfahrung deiner Drohnen und P.E.T.s. Die Erfahrung, die sie zahlen, zählt dagegen für deine PvE-Rangpunkte, wie die Erfahrung eines Abschlusses. Die Beute der Aliens kommt mit der Auszahlung, direkt in dein Inventar.

<!-- solo-kills:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

| Alien | Credits | Thulium | EP | Ehre |
| :--- | ---: | ---: | ---: | ---: |
| **Seeker** | 1.000 | 4 | 100 | 2 |
| **Phantasm** | 3.000 | 12 | 300 | 6 |
| **Bulwark** | 5.000 | 25 | 800 | 10 |
| **Goombah** | 15.000 | 75 | 3.000 | 24 |
| **Crystalys** | 75.000 | 200 | 12.000 | 52 |

| Tor | Credits | Thulium | EP | Ehre |
| :--- | ---: | ---: | ---: | ---: |
| **Alpha Rift** | 540.000 | 2.160 | 54.000 | 1.080 |
| **Beta Breach** | 1.320.000 | 5.980 | 186.000 | 2.520 |
| **Gamma Foundry** | 3.000.000 | 13.300 | 522.000 | 4.616 |
| **Delta Siege** | 4.975.000 | 21.400 | 829.000 | 7.640 |
| **Omega Vault** | 6.875.000 | 29.000 | 1.160.000 | 10.100 |

<!-- solo-kills:end -->

## Herausforderungen und Erfolge {#challenges-and-achievements}

Zwei optionale Herausforderungen können bei jedem Abschluss gewonnen werden, und sie zahlen je einen Erfolg und **kein Thulium**. Ein Abschluss **ohne Tod** ist einer ohne jeden Tod im ganzen Lauf, über alle Male, die du hineingegangen bist. Ein **Speedrun** ist ein Abschluss innerhalb der kürzesten geplanten Zeit des Tors, gezählt nach der Zeit, die du in der Arena verbringst. Die anderen sechs Erfolge gibt es fürs Abschließen jedes Tors und aller fünf:

<!-- solo-achievements:begin -->
<!-- Generated from server/Resources/SoloGates.json (and Rockets.json, SpecialItems.json, Containers.json, Achievements.json, Data/Seeds/aliens.json, client/locales/<language>/achievements.toml) by scripts/solo-gates-wiki.sh: don't edit by hand. -->

- **Riss geschlossen** (Gewöhnlich): Schließe den Alpha Rift im Alleingang ab.
- **Bresche versiegelt** (Ungewöhnlich): Schließe den Beta Breach im Alleingang ab.
- **Gießerei stillgelegt** (Selten): Schließe die Gamma Foundry im Alleingang ab.
- **Belagerung gebrochen** (Selten): Brich die Delta Siege im Alleingang.
- **Tresor geknackt** (Episch): Knacke den Omega Vault im Alleingang.
- **Torwächter** (Legendär): Schließe alle fünf Solo-Tore ab: Alpha, Beta, Gamma, Delta und Omega.
- **Unantastbar** (Selten): Schließe ein Solo-Tor ab, ohne ein Leben zu verlieren.
- **Gegen die Uhr** (Selten): Schließe ein Solo-Tor in höchstens seiner kürzesten Zeit ab: 10, 15, 25, 35 oder 50 Minuten für Alpha bis Omega.

<!-- solo-achievements:end -->

## Gegenstände aus einem Tor {#items-from-a-gate}

Was ein Tor dir gibt, ist **handelbar**: Das Erz, die Platten, die Power Cores, die Munition und die Beute der Aliens können wie ein Drop oder eine Questbelohnung in der [Auktion](/wiki/03-Mechanics/Auction.md) angeboten werden, mit denselben Ausnahmen wie für jeden Gegenstand. Die Belohnungen eines Scans ohne Teil sind es nicht: Sie kommen von einem Scan, nicht von einem Tor.

## Tore und der Wipe {#gates-and-the-wipe}

- **Der Wipe beendet jeden offenen Lauf** und gibt dir seine Teile zurück. Ein Lauf geht nicht in die nächste Saison weiter.
- **Durch den Wipe bleiben:** die Teile der fünf Solo-Tore, der Zähler der Garantie und die Aufzeichnung dessen, was du für Scans ausgegeben hast und was die Tore zurückgezahlt haben, die Obergrenze für das Thulium gilt also über die Saisons hinweg. Die Erfolge gehören dir für immer.
- **Beim Wipe verloren:** die Teile des Chrono-Gates, wie zuvor. Deine Scans kaufen sie neu.
- **Das Löschen eines Accounts** löscht die Teile, den Zähler und die Aufzeichnung.
