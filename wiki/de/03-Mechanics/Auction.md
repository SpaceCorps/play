<!-- wiki-i18n source: d7e1133b56dbdf93 -->
<!-- wiki-i18n title: Auktion -->
# Auktion {#auction}

Die Auktion ist der Markt der Piloten und zugleich die stündlichen Lose des Spiels, auf einer Seite des Stationsmenüs. Wie der Shop ist sie eine Seite der Station: Du nutzt sie angedockt, nicht im Flug. Sie hat vier Bereiche. **Markt** zeigt, was andere Piloten verkaufen. **Lose** sind die eigenen Angebote des Spiels, eines pro Stunde. **Meine Angebote** zeigt, was du selbst verkaufst. **Verlauf** zeigt deine Verkäufe, deine Käufe und die Lose, die du gewonnen hast, und wie dein Handel gelaufen ist.

<!-- market-glance:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Du brauchst **Level 5**, um die Auktion zu nutzen: zum Einstellen, Kaufen und Bieten.
- Ein Angebot wird je Posten in ganzen Credits oder in ganzem Thulium bepreist (nicht beides) und nie unter dem Mindestpreis der Sorte. Einen **Höchstpreis gibt es nicht**.
- Ein Preis in Thulium beträgt mindestens den Mindestpreis in Credits geteilt durch 1.000, aufgerundet, und gilt nur für Sorten, deren Mindestpreis 1 Thulium oder mehr ergibt. Mehr macht der Kurs nicht: **1 Thulium = 1.000 Credits ist eine Regel für den Mindestpreis, kein Wechselkurs.** Nichts wird getauscht, kein Wert wird angezeigt, und Credits und Thulium werden nie zusammengezählt.
- 80 Sorten lassen sich einstellen, und 79 davon können auch in Thulium bepreist werden.
- Ein Angebot läuft 24 / 72 / 168 Stunden, wie du es wählst: Die Auswahl ist auf jedem Level dieselbe.
- Die **Einstellgebühr** beträgt 1 % des Preises für jeweils 24 Stunden Laufzeit, mindestens 50 Credits oder 1 Thulium. Du zahlst sie beim Einstellen; sie wird nie erstattet, auch nicht, wenn du das Angebot zurückziehst.
- Ab Level 10 beträgt die Einstellgebühr 1,5 %.
- Die **Steuer** beträgt 5 % des Preises. Sie wird von dem abgezogen, was der Verkäufer erhält, wenn das Angebot verkauft wird.
- Einstellgebühr und Steuer werden vernichtet: Sie gehen an niemanden.
- Ab Saisontag 28 bis zum Wipe gibt es weder Einstellgebühr noch Steuer.
- Ab Saisontag 30 ist die Auktion bis zum Start der neuen Saison geschlossen: Nichts kann eingestellt, gekauft oder mit Geboten belegt werden. Deine Angebote kannst du weiterhin zurückziehen.
- Jede Währung hat ein eigenes Limit dafür, wie viel du in 24 Stunden verkaufen und wie viel du kaufen kannst (Leveltabelle unten). Gewonnene Lose zählen nicht mit.
- Zwischen zwei Piloten, von denen einer vom anderen kauft, gehen in 24 Stunden höchstens 8.000.000 Credits oder 40.000 Thulium über.

<!-- market-glance:end -->

## Handelbare Gegenstände {#marketable-items}

Verkaufen kannst du nur Gegenstände, die du **verdient** hast. Alles, was du verdienst, trägt im [Hangar](/wiki/03-Mechanics/Inventory.md#marketable-items) ein kleines Etikett, **Handelbar**: was du im All aufsammelst (Beute von Aliens, Schwärmen, Wardens und dem Schwarzen Loch: [Frachtkisten](/wiki/03-Mechanics/Cargo.md)), was eine Mission auszahlt ([Quests](/wiki/03-Mechanics/Quests.md#rewards)) und alles, was die Montage und die Schmiede herstellen. Was du im Shop **gekauft**, in einem Los gewonnen, auf dem Markt gekauft, über einen Bonuscode, ein Einladungspaket oder das Starterpaket bekommen oder als Erstattung zurückerhalten hast, ist nicht handelbar und kann nie wieder verkauft werden, damit nichts nur zum Weiterverkauf gekauft wird. Auch die Platten aus der Schmiede des Skylab sind nicht handelbar; die Reinforced Plates, die eine Mission auszahlt, sind es. Auch die Munition und die Raketen, die der Munitionsdrucker und die Raketenfabrik des Skylab herstellen, sind nicht handelbar.

Das Etikett ist eine Anzahl von Einheiten, kein Schalter: Ein Munitionsstapel kann gekaufte und verdiente Schuss enthalten, und die Karte zeigt „Handelbar (3 von 5)“. Wenn du einen Teil eines Stapels verbrauchst (Schießen, Herstellen), gehen zuerst die einfachen Einheiten weg, sodass die handelbaren am längsten halten. Beim Zusammenführen zweier Stücke in der [Schmiede](/wiki/06-Items/Forge.md#merge) bleibt das Etikett nur, wenn beide Stücke es hatten, und die Vorschau sagt das; ein fehlgeschlagener Schritt der Schmiede gibt seine Materialien als einfache Einheiten zurück.

Der Chip **Nur Handelbares** im Hangar zeigt nur, was du verkaufen kannst, und der **Auktionshammer** neben dem Mülleimer eines markierten Gegenstands öffnet das Verkaufsblatt der Auktion dafür. In der Montage sagt ein Rezept, dessen Ergebnis handelbar ist, das dazu, und bei einem Material, das dir fehlt, öffnet ein Link die Auktion mit dem Namen im Suchfeld.

Als die Auktion kam (0.4.12), wurden die Ausrüstung, die du schon besaßt und die der Shop nicht verkauft, sowie die Ressourcen einmalig markiert. Nicht markiert wurden diese, weil der Shop sie einmal verkauft hat oder weil das, was du besitzt, gekaufte und verdiente Stücke mischt: der Quantum Laser III, die Absorption Shield Cells II und III, die Impulse Thrusters II und III, die beiden Reinforced Plates und die älteste Base CPU I jedes Piloten (die des Starterpakets). Neue davon, die du verdienst oder herstellst, sind markiert.

## Was verkauft werden kann {#what-can-be-sold}

<!-- market-kinds:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Typ | Sorten, die du verkaufen kannst | Anzahl |
| :--- | :--- | ---: |
| **Laser** | Quantum Laser I, Quantum Laser II, Quantum Laser III, Starfire-III, Helios Beam | 5 |
| **Laserverstärker** | Damage Amp I, Crit Amp I, Penetration Amp I, Damage Amp II, Crit Amp II, Penetration Amp II, Damage Amp III, Crit Amp III, Penetration Amp III, Damage Amp IV, Crit Amp IV, Penetration Amp IV | 12 |
| **Schildkerne** | Light Shield Core, Basic Shield Core, Heavy Shield Core | 3 |
| **Triebwerke** | Engine I, Engine II, Engine III | 3 |
| **Adaptive Cores** | Adaptive Core I, Adaptive Core II, Adaptive Core III | 3 |
| **Schildzellen** | Absorption Shield Cell I, Capacity Shield Cell I, Absorption Shield Cell II, Capacity Shield Cell II, Absorption Shield Cell III, Capacity Shield Cell III, Absorption Shield Cell IV, Capacity Shield Cell IV | 8 |
| **Schubdüsen** | Impulse Thruster I, Momentum Thruster I, Impulse Thruster II, Momentum Thruster II, Impulse Thruster III, Momentum Thruster III, Impulse Thruster IV, Momentum Thruster IV | 8 |
| **Lasermunition** | Standard Battery (in Posten zu 100), Siphon Battery (in Posten zu 10), Advanced Plasma (in Posten zu 10), Ultra Core (in Posten zu 10), Experimental Fusion Core | 5 |
| **Raketen** | Ember I, Lancet I, Rivet I, Scatter I, Ember II, Lancet II, Rivet II, Scatter II, Ember III, Lancet III, Rivet III, Scatter III | 12 |
| **Extras** | Repair Drone I, Repair Drone II, Repair Drone III, EMP Charge, Repair Drone IV, Cloaking CPU S, Base CPU I, Cloaking CPU M, Auto-Repair CPU, Cloaking CPU L, Base CPU II | 11 |
| **Ressourcen** | Cataclysite (in Posten zu 100), Ship Fragment (in Posten zu 100), Daraxium (in Posten zu 100), Nyxite (in Posten zu 100), Quorvium (in Posten zu 10), Reinforced Hull Plate (in Posten zu 10), Power Core, Velkonite Reinforced Plate, Dark Matter, Orvium Reinforced Plate | 10 |

<!-- market-kinds:end -->

Schiffe, Drohnen, Drohnenformationen, Booster und Abos können nie verkauft werden, ebenso wenig die Ancient Control Unit, die Erze Velkonite und Orvium, die Dark Matter Plate, die Jump CPU, die Extra Slots CPUs, die N.U.K.E. und die N.I.K.E. Dark Matter Plates gibt es in der Auktion gar nicht, weder als Ware noch als Preis. Ein Gegenstand, der ausgerüstet, in einen anderen Gegenstand eingesetzt ist, Module enthält oder im [Transport-Cache](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) liegt, kann nicht eingestellt werden, ebenso wenig eine benutzte Cloaking CPU, EMP Charge oder Base CPU. Munition und Raketen werden von der Station aus verkauft: Lande zuerst dein Schiff.

## Verkaufen {#selling}

Drücke **Gegenstand verkaufen** (oder den Auktionshammer im Hangar), wähle, was du verdient hast (ein Auswahlmenü für Kategorien grenzt die Liste ein, mit denselben Kategorien wie im Markt), entscheide dich für Credits oder Thulium, lege den Preis eines Postens fest und wie lange das Angebot läuft: 1, 3 oder 7 Tage. Das Blatt zeigt den Mindestpreis, drei Chips, die einen Preis eintragen (**Minimum**; **Schnellverkauf**, einen unter dem niedrigsten Angebot im Moment; und **Fair**, der Preis des letzten Verkaufs), sowie Einstellgebühr, Steuer und das, was du erhältst, noch bevor du einstellst. Unter dem Preis zeigt **Ähnliche Angebote** in einem Diagramm, zu welchen Preisen derselbe Gegenstand mit derselben Verzauberung gerade angeboten wird, in der Währung, die du gewählt hast: Dein Preis ist eine Linie darin, der Mindestpreis, der letzte Verkauf und der Preis im Shop sind markiert, eine Zeile in Worten sagt, wo dein Preis stünde, und darunter stehen die drei günstigsten Angebote. Ein Stück ist ein Posten zu eins; Munition und manche Ressourcen werden in Posten zu 10 oder 100 verkauft, und du verkaufst eine ganze Zahl von Posten. Was du einstellst, verlässt dein Inventar und wird vom Server gehalten, bis es sich verkauft, du es zurückziehst oder es abläuft; dann kommt es mit seinem Etikett zurück. Du kannst jederzeit zurückziehen, auch in den letzten Tagen einer Saison. Ein Angebot ist eine Momentaufnahme: Um einen Preis zu ändern, ziehe das Angebot zurück und stelle es neu ein (die Einstellgebühr wird dann erneut fällig).

Jede Sorte hat einen **Mindestpreis**, und es gibt **keinen Höchstpreis**: Verlange, was du willst. Die Tabelle zeigt den Mindestpreis einiger Sorten.

<!-- market-bands:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Sorte | Verkauft in Posten zu | Mindestpreis, Credits | Mindestpreis, Thulium |
| :--- | ---: | ---: | ---: |
| Quantum Laser II | 1 | 32.000 | 32 |
| Quantum Laser III | 1 | 210.000 | 210 |
| Helios Beam | 1 | 1.600.000 | 1.600 |
| Absorption Shield Cell IV | 1 | 1.100.000 | 1.100 |
| Heavy Shield Core | 1 | 870.000 | 870 |
| Impulse Thruster IV | 1 | 980.000 | 980 |
| EMP Charge | 1 | 40.000 | 40 |
| Cloaking CPU S | 1 | 400.000 | 400 |
| Ultra Core | 10 | 800 | 1 |
| Lancet I | 1 | 200 | 1 |
| Ship Fragment | 100 | 600 | 1 |
| Dark Matter | 1 | 33.000 | 33 |

<!-- market-bands:end -->

Ein Preis in Thulium folgt einer einzigen Regel: der Mindestpreis in Credits geteilt durch den Kurs, aufgerundet. Der Kurs ist kein Wert, den das Spiel dem Thulium beimisst. Er legt nur fest, wie der Mindestpreis in Thulium berechnet wird, und deshalb kann ein Angebot in Thulium für einen Piloten mit Thulium günstig sein. Die meisten Verkäufer werden Credits verlangen. Jede Sorte außer **Quorvium** kann in Thulium bepreist werden, auch die günstigen (Munition, Raketen, die gewöhnlichen Ressourcen): Ihr Mindestpreis ist dann 1 Thulium, der kleinste Schritt. Nur Quorvium gibt es allein in Credits, weil 1 Thulium mehr wäre, als ein Posten davon wert ist.

Deine **offenen Angebote** (und ein Angebot, das ein Admin angehalten hat) belegen Plätze. Mit steigendem Level bekommst du mehr Plätze, bis zu einem Höchstwert, und du darfst pro Tag mehr verkaufen und kaufen. Wie lange ein Angebot laufen darf, ist auf jedem Level gleich.

<!-- market-limits:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Level | Offene Angebote | Längste Laufzeit | Pro Tag, Credits | Pro Tag, Thulium | Einstellgebühr je 24 h |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 5 | 20 | 168 h | 4.500.000 | 22.500 | 1 % |
| 6 | 40 | 168 h | 6.000.000 | 30.000 | 1 % |
| 7 | 70 | 168 h | 7.500.000 | 37.500 | 1 % |
| 8 | 100 | 168 h | 8.500.000 | 42.500 | 1 % |
| 9 | 100 | 168 h | 10.000.000 | 50.000 | 1 % |
| 10 | 100 | 168 h | 15.000.000 | 75.000 | 1,5 % |
| 11 | 100 | 168 h | 15.000.000 | 75.000 | 1,5 % |
| 12 | 100 | 168 h | 15.000.000 | 75.000 | 1,5 % |
| 13 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 14 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 15 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 16 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 17 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 18 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 19 | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |
| 20 und höher | 100 | 168 h | 20.000.000 | 100.000 | 1,5 % |

<!-- market-limits:end -->

## Gebühren {#fees}

Ein Angebot kostet eine **Einstellgebühr**, die beim Einstellen fällig wird und nie erstattet wird, und ein Verkauf kostet eine **Steuer**, die von dem abgezogen wird, was der Verkäufer erhält. Beide werden in der Währung des Angebots gezahlt und **vernichtet**: Sie gehen an niemanden, also gewinnt keiner dadurch, dass er mit sich selbst handelt. In den letzten zwei Tagen einer Saison gibt es weder Einstellgebühr noch Steuer.

<!-- market-fees:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| Angebot | Preis | Einstellgebühr | Steuer | Der Verkäufer erhält |
| :--- | ---: | ---: | ---: | ---: |
| Quantum Laser III: Level 6, 24 h | 210.000 Credits | 2.100 Credits | 10.500 Credits | 199.500 Credits |
| Quantum Laser III: Level 10, 72 h | 210 Thulium | 10 Thulium | 10 Thulium | 200 Thulium |
| Helios Beam: Level 12, 168 h | 2.500.000 Credits | 262.500 Credits | 125.000 Credits | 2.375.000 Credits |
| Helios Beam: Level 12, 168 h, in den letzten Tagen einer Saison | 2.500.000 Credits | 0 Credits | 0 Credits | 2.500.000 Credits |

<!-- market-fees:end -->

## Kaufen {#buying}

Der **Markt** zeigt, was andere Piloten verkaufen. Grenze die Liste mit den **Kategorie-Chips** ein (einer für jede Art von Gegenstand, mit der Zahl der Angebote darin), suche nach Namen, filtere nach Verzauberung und Währung und sortiere nach Preis, danach, was zuerst endet, oder danach, was am neuesten ist. Wähle ein Angebot, um zu sehen, was es ist, wer es verkauft, wie lange es läuft und wie sein Preis zum letzten Verkauf, zum niedrigsten Preis im Moment und zum Preis im Shop steht. Ein Stapel wird in ganzen Posten gekauft. Ein großer Kauf fragt noch einmal nach. Der Verkäufer wird sofort bezahlt, abzüglich der Steuer; du zahlst weder Einstellgebühr noch Steuer. Was du kaufst, ist **nicht handelbar**: Die Seite sagt neben **Kaufen für …** „Du erhältst: nicht handelbar“, weil nur verkauft werden kann, was du verdienst. Dein eigenes Angebot kannst du nicht kaufen. Ein Angebot, das sich verkauft, während du es ansiehst, meldet „Dieses Angebot ist nicht mehr da.“

## Limits

Jede Währung hat ein eigenes Tageslimit dafür, wie viel du verkaufen und wie viel du kaufen kannst, gezählt über die letzten 24 Stunden, und ein Limit dafür, was zwischen zwei Piloten fließt, damit ein zweiter Account kein schneller Weg ist, ein Vermögen zu verschieben. Credits und Thulium werden nie zusammengezählt: Wer für Thulium verkauft, verbraucht sein Thulium-Limit und sonst nichts. Das Verkaufsblatt warnt dich, wenn ein Verkauf dein Tageslimit fürs Verkaufen überschreiten würde, und wenn ein Kauf dein Tageslimit fürs Kaufen überschreiten würde, sagt der Markt es dir und sperrt **Kaufen für …**. Die Limits wachsen mit dem Level, und Premium ändert keines davon. Gewonnene Lose zählen nicht mit.

Raketen in einem Angebot, in einem Los, das du anführst, und in deinem Frachtraum zählen alle zur größten Zahl einer Rakete, die du tragen darfst: Mit einem Angebot lässt sich nicht mehr tragen, als der Stapel des Shops erlaubt.

## Meine Angebote und Verlauf {#my-listings-and-history}

**Meine Angebote** zeigt deine Plätze und jedes Angebot mit seinem Zustand (offen, verkauft, abgebrochen, abgelaufen, zurückgegeben oder angehalten), einer Schaltfläche **Zurückziehen**, **Erneut einstellen** für ein beendetes und einem Chip **Unterboten**, wenn ein anderes Angebot derselben Sache weniger verlangt. Ein Angebot, das abgelaufen ist, kommt von selbst in dein Inventar zurück. Der **Verlauf** beginnt mit deinem Handel der letzten 30 Tage: deine Verkäufe und Käufe, was du eingenommen und ausgegeben hast, die Gebühren und Steuern, die du bezahlt hast, dein Gesamtergebnis, dein bester Verkauf, dein durchschnittlicher Verkauf und der Gegenstand, den du am meisten gehandelt hast, dazu zwei Liniendiagramme: deine Einnahmen pro Tag und dein Ergebnis bisher (für Credits oder für Thulium, jeweils eines). Darunter steht die Liste dessen, was du verkauft, gekauft und gewonnen hast, samt Steuer. Das Spiel bewahrt das Hauptbuch der Auktion 90 Tage auf.

Du erfährst, wenn etwas verkauft wird: durch einen Toast, den Ton der Auktion und den neuen Kontostand, und durch ein Zeichen am Eintrag der Auktion, solange die Seite geschlossen ist. Eine Folge von Verkäufen ist ein Toast. Die Auktion hat eigene leise Töne, einen für alles, was du dort tust oder was dir dort geschieht (Einstellen, Beenden, ein Verkauf, ein Gebot, überboten werden, gewinnen), und sie folgen der Lautstärke der Oberfläche.

## Die stündlichen Lose {#the-hourly-lots}

Die Lose sind die eigenen Angebote des Spiels: Munition, Raketen und EMP Charges, jede Stunde, auf Gebote. Sie sind eine Möglichkeit, Munition günstiger zu bekommen, als der Shop sie verlangt, und eine Senke: Das Gewinngebot wird vernichtet. Es öffnen nur die Lose aus der Tagestabelle unten (nie x1- oder x4-Munition, nie Siphon Batteries, nie eine besondere Rakete), in der Währung des Shops. Ein Raketenlos ist nie größer als die größte Zahl dieser Rakete, die du tragen darfst (der Stapel des Shops); ein Gebot, das dich darüber brächte, wird abgelehnt. Biete also auf ein Raketenlos, wenn du wenig von dieser Rakete trägst.

<!-- market-lots:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

- Zu Beginn jeder UTC-Stunde öffnet ein neues Los und bleibt 4 Stunden offen, sodass 4 gleichzeitig offen sind.
- Das Startgebot beträgt 40 % des Shop-Preises der Ware. Jedes weitere Gebot muss mindestens 5 % über dem Höchstgebot liegen und mindestens 100 Credits oder 1 Thulium mehr betragen.
- Dein Gebot wird sofort bezahlt und gehalten. Wirst du überboten, bekommst du es sofort zurück.
- Ein Gebot in den letzten 2 min eines Loses verschiebt dessen Ende auf 2 min nach dem Gebot, höchstens 5-mal.
- Was du gewinnst, ist zum Fliegen da, nicht zum Handeln: Es ist nie handelbar. Das Gewinngebot wird vernichtet. Auf ein Los, auf das niemand bietet, wird nichts verkauft, und es kostet niemanden etwas.
- Wie groß ein Los ist, richtet sich nach den Piloten ab Level 5, die in den letzten 3 Tagen in die Auktion geschaut haben: Bei keinem sind es 10 % der Größe in der Tabelle, ab 30 die volle Größe, in Schritten von 500 bei Munition, 50 bei Raketen und 1 bei EMP Charges.
- In den letzten 6 Stunden einer Saison wird kein Los mehr gemacht. Der Wipe bricht die noch offenen Lose ab, und jedes Gebot geht zurück.

<!-- market-lots:end -->

<!-- market-day:begin -->
<!-- Generated from server/Resources/Market.json and Auction.json (and the item seeds, Rockets.json) by scripts/market-wiki.sh: don't edit by hand. -->

| UTC-Stunde | Los | Volle Größe | Bezahlt in | Startgebot bei voller Größe |
| :--- | :--- | ---: | :--- | ---: |
| 00:00 | Scatter III | 1.250 | Thulium | 2.500 Thulium |
| 01:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 02:00 | Lancet I | 12.500 | Credits | 2.500.000 Credits |
| 03:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |
| 04:00 | Ultra Core | 25.000 | Thulium | 10.000 Thulium |
| 05:00 | Rivet II | 5.000 | Credits | 1.600.000 Credits |
| 06:00 | Advanced Plasma | 10.000 | Thulium | 2.000 Thulium |
| 07:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 08:00 | Ember I | 12.500 | Credits | 2.500.000 Credits |
| 09:00 | Ultra Core | 50.000 | Thulium | 20.000 Thulium |
| 10:00 | Scatter II | 5.000 | Credits | 1.600.000 Credits |
| 11:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |
| 12:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 13:00 | Lancet III | 1.250 | Thulium | 2.500 Thulium |
| 14:00 | Ultra Core | 10.000 | Thulium | 4.000 Thulium |
| 15:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 16:00 | Ultra Core | 50.000 | Thulium | 20.000 Thulium |
| 17:00 | Rivet I | 12.500 | Credits | 2.500.000 Credits |
| 18:00 | Advanced Plasma | 50.000 | Thulium | 10.000 Thulium |
| 19:00 | Ember II | 5.000 | Credits | 1.600.000 Credits |
| 20:00 | Ultra Core | 25.000 | Thulium | 10.000 Thulium |
| 21:00 | Advanced Plasma | 25.000 | Thulium | 5.000 Thulium |
| 22:00 | Advanced Plasma | 10.000 | Thulium | 2.000 Thulium |
| 23:00 | EMP Charge | 5 | Thulium | 1.000 Thulium |

<!-- market-day:end -->

Wenn wenige Piloten die Auktion nutzen, sind die Lose klein, damit einer Handvoll Piloten nicht jede Stunde Tausende Schuss angeboten werden; sie wachsen, je mehr Piloten hinschauen.

## Die Saison und der Wipe {#the-season-and-the-wipe}

Die Auktion folgt der Saison (siehe [Wipe-Zeitleiste](/wiki/03-Mechanics/Wipe-Timeline.md)). In den letzten zwei Tagen gibt es keine Gebühren. Ab Tag 30, wenn der fünfminütige Countdown des Wipes beginnt, ist sie geschlossen: Nichts wird eingestellt, gekauft oder geboten, ein Los, das dann endet, wird abgebrochen und sein Gebot zurückgegeben, und deine eigenen Angebote kannst du weiterhin zurückziehen. Ein Angebot läuft nie über das Ende der Saison hinaus.

Beim Wipe **kommt jedes offene Angebot zu seinem Verkäufer zurück** als lose Gegenstände, und der Wipe löscht lose Gegenstände dann wie alle anderen (nur was du in den [Transport-Cache](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) legst, bleibt): Verkaufe also, oder brich ab und lege in den Cache, was du behalten willst. Die Lose, die noch offen sind, werden abgebrochen und die Gebote erstattet. Credits und Thulium werden nicht gewipet.

## Was die Auktion dir nicht gibt {#what-the-auction-does-not-give-you}

Die Auktion dient dem Handel mit dem, was du verdienst, und sie ist ehrlich über ihre Grenzen.

- **Beute zu verkaufen ist kein Grind.** Rohe Alien-Beute besteht nur aus Ressourcen und ist 0,4 bis 0,9 Prozent dessen wert, was dieselbe Jagdstunde auf Level 5 an Abschüssen auszahlt. Was der Markt einem neuen Piloten gibt, ist die Ausrüstung, die seine Missionen auszahlen und die er nicht braucht (einmalig), die Ressourcen der Herausforderungs-Missionen, die Kisten der Schwarm-Bosse und das, was er herstellt.
- **Es gibt keinen Händler.** Kaufaufträge, bei denen ein Pilot sagt, was er kaufen will und für wie viel, gibt es in dieser Version nicht. Bis dahin sind die einzigen Händler der Handwerker, der Materialien kauft, in der Montage Ausrüstung herstellt und sie verkauft, und der Lagerpilot, der seinen Vorrat durch den Wipe im Transport-Cache hält.
- **Shop-Ausrüstung ist nicht zum Weiterverkauf da.** Ausrüstung, die du im Shop gekauft hast, kann nicht wieder verkauft werden: Dazu gehören der Quantum Laser I und II, der Light und der Basic Shield Core, Engine I und II, die erste Stufe der Zellen und Schubdüsen, die Amps, die der Shop verkauft, und gekaufte Munition. Der eine handelbare Quantum Laser II eines Piloten ist der, den eine Mission einmal auszahlt.
- **Platten kommen aus Missionen.** Die Velkonite und Orvium Reinforced Plates auf dem Markt sind die, die die Herausforderungs-Missionen auszahlen. Die Platten der Schmiede bleiben draußen, sonst wären sie die größte Ware des Markts.

Wenn ein Angebot nicht stimmt, melde es auf dem üblichen Weg: Die Admins des Spiels können ein Angebot anhalten, es zurückgeben, die Auktion pausieren oder einen Piloten davon ausschließen, und jede solche Handlung wird aufgezeichnet.
