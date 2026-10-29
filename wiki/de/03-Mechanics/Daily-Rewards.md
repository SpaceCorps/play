<!-- wiki-i18n source: c6cf04f6e8e99425 -->
<!-- wiki-i18n title: Tägliche Belohnungen -->
# Tägliche Belohnungen {#daily-rewards}

<!-- wiki-search: daily reward; daily rewards; daily login; login bonus; login reward; calendar; advent calendar; chest; chests; season prize; souvenir; blueprint; streak; tägliche belohnung; täglicher login; login-bonus; kalender; adventskalender; truhe; saisonprämie; bauplan; serie -->

Jede Saison hat einen **Kalender der täglichen Belohnungen**: ein kleines Geschenk für jeden Tag der Saison. Drück an der Station auf **Abholen**, und das Geschenk des Tages gehört dir. Je mehr Tage du abholst, desto mehr bekommst du: Vier **Truhen** kommen bei 7, 14, 21 und 28 abgeholten Tagen, und in den letzten drei Tagen der Saison kannst du die **Saisonprämie** nehmen. Ein verpasster Tag kostet dich das Geschenk dieses Tages und sonst nichts. Du findest den Kalender im **Dashboard** (die Karte **Tägliche Belohnungen**) und unter **Saison & Profil › Kalender**.

## In einer Minute {#in-one-minute}

- **29 Kacheln.** Eine für jeden UTC-Tag der Saison. Eine Saison hat 30 Tage, aber Tag 30 ist der 5-Minuten-Countdown des [Wipe](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule), also gibt es an ihm nichts abzuholen.
- **Du drückst Abholen.** Ein Druck holt eine Kachel ab, einmal pro Pilot. Nichts wird automatisch für dich abgeholt.
- **6 Stunden Gnadenfrist.** Eine Kachel bleibt 6 Stunden nach dem Ende ihres Tages offen.
- **Keine Serie.** Ein verpasster Tag kostet nur die Kachel dieses Tages und sonst nichts. Es zählt, wie viele Tage du abgeholt hast, nicht ob sie aufeinanderfolgten.
- **4 Truhen**, bei 7, 14, 21 und 28 abgeholten Tagen.
- **Eine Saisonprämie** in den letzten drei Tagen der Saison: ein Souvenir-Look bei 10 abgeholten Tagen und ein Bauplan für ein Schiffsdesign bei 20.
- **Jeder Wipe bringt einen neuen Kalender.** Du siehst jedes Geschenk der Saison ab Tag 1.
- **Absichtlich klein.** Alle 29 Tage zusammen sind ungefähr so viel wert wie ein paar Stunden Jagd, verteilt über eine Saison.

## Der Tag {#the-day}

Der Tag des Kalenders ist ein **UTC-Tag**: Er wechselt um **00:00 UTC**, für alle Piloten im selben Moment, und er ist dieselbe Tageszählung wie die Tageslinie der Clans („Tag *n* von 29“, siehe [Clans](/wiki/03-Mechanics/Clans.md#the-day)). Er folgt nicht deiner Zeitzone, und er ist nicht der Saisontag der Saison-Seite, der zu der Uhrzeit wechselt, zu der die Saison begann. Die Uhr des Servers entscheidet alles: Die Uhr deines Computers ändert nichts.

Die Karte und der Reiter nennen beide, wann die nächste Belohnung **in deiner eigenen Zeitzone** öffnet („Neue Belohnungen öffnen um 02:00 deiner Zeit (00:00 UTC)“). Um es selbst auszurechnen, rechne 00:00 UTC um. Einige Beispiele:

| Wo | UTC-Mitternacht ist |
| :--- | :--- |
| Mitteleuropa | 01:00 (Winter) oder 02:00 (Sommer) |
| Moskau, Istanbul | 03:00 |
| Japan, Korea | 09:00 |
| US-Ostküste | 19:00 (Winter) oder 20:00 (Sommer) |
| US-Westküste | 16:00 (Winter) oder 17:00 (Sommer) |

- **Tag 1 ist kurz.** Die Saison beginnt mit dem Wipe, mitten in einem UTC-Tag, also ist Kachel 1 ab da bis zum Ende dieses Tages offen, plus die Gnadenfrist.
- **Tag 29 ist lang.** Die letzte Kachel bleibt offen, bis der Countdown des Wipe beginnt, und das kann mehr als 24 Stunden nach ihrem Öffnen sein. Sobald der Countdown läuft, lässt sich nichts mehr abholen, bis die neue Saison beginnt.
- **Administratoren können den Saisontag verschieben.** Der Kalender folgt ihm: Übersprungene Tage gelten für alle als verpasst, und eine Kachel, die du schon abgeholt hast, bleibt abgeholt.

## Die Kacheln {#the-tiles}

Der Reiter Kalender zeigt ein Raster mit einer Kachel für jeden Tag: die Tagesnummer, das Geschenk und einen Zustand in Worten. Jedes Geschenk der Saison ist ab dem ersten Tag sichtbar, du siehst also, was kommt. Er zählt auch deine Tage (zum Beispiel „11 von 29 Tagen abgeholt“) und sagt, wann die nächste Truhe kommt. Die Karte im Dashboard zeigt das Geschenk von heute und einen einzigen Knopf **Abholen**.

| Zustand | Was es bedeutet |
| :--- | :--- |
| **Heute** | Jetzt offen. Drück auf **Abholen**. |
| **Abgeholt** | Du hast es. |
| **Gestern** | Die Kachel von gestern, während der Gnadenfrist noch offen. Sie zeigt, wie lange noch, und hat einen eigenen Knopf **Abholen**. |
| **Verpasst** | Der Tag und seine Gnadenfrist sind vorbei. Das Geschenk ist weg, und sonst hat sich nichts geändert. |
| **Öffnet in …** | Ein kommender Tag. Du siehst sein Geschenk, kannst es aber noch nicht abholen. |
| **Vor Beitritt** | Ein Tag vor deiner ersten Anmeldung. Er lässt sich nicht abholen. |

Solange eine Belohnung wartet, erscheint ein kleines **(!)** bei **Saison & Profil** in der Seitenleiste und bei **Zurück zur Basis** im Flug, und eine Meldung bei der Anmeldung sagt es dir (einmal pro Tag und Computer).

## Gnadenfrist und verpasste Tage {#grace-and-missed-days}

Eine Kachel schließt nicht um Mitternacht: Sie bleibt **6 Stunden** nach dem Ende ihres UTC-Tages offen. In diesen 6 Stunden sind zwei Kacheln offen, die von gestern und die von heute, und du holst jede mit einem eigenen Druck ab. Nach der Gnadenfrist ist die Kachel von gestern endgültig **Verpasst**, und weiter zurück kommst du nicht.

Ein verpasster Tag kostet dich **das Geschenk dieses Tages und sonst nichts**. Es gibt keine Serie, die reißen könnte: Deine Zahl abgeholter Tage, deine Truhen und die Saisonprämie laufen weiter. Eine Kachel, die du in der Gnadenfrist abholst, zählt genauso wie eine, die du rechtzeitig abgeholt hast.

## Truhen {#chests}

Eine Truhe kommt mit dem **Abholen**, durch das deine Zahl abgeholter Tage eine bestimmte Zahl erreicht, und nicht früher: Es gibt nichts zu drücken und keinen Schlüssel zu finden. Es zählt die Anzahl, nicht das Datum: Die Truhe bei 7 kommt mit deinem 7. abgeholten Tag, egal welcher Tag der Saison das ist.

| Truhe | Kommt bei |
| :---: | :--- |
| **1.** | 7 abgeholten Tagen |
| **2.** | 14 abgeholten Tagen |
| **3.** | 21 abgeholten Tagen |
| **4.** | 28 abgeholten Tagen |

Jede Truhe enthält einen **Specimen Vault**, den Container, der von allem ein bisschen enthält. Die späteren Truhen können eine kleine Zugabe enthalten, die der Wipe nicht nimmt. Der Reiter Kalender zeigt, was in jeder Truhe steckt. Ein Container gehört nur dir, und du öffnest ihn auf der Seite Container. Ein Container, den du nicht geöffnet hast, bleibt auch durch den [Wipe](/wiki/03-Mechanics/Wipe-Timeline.md) auf deinem Konto.

Kann das Spiel den Container nicht ausgeben, zum Beispiel weil Container nicht eingeschaltet sind, zahlt die Truhe stattdessen ein **Bündel** aus Credits, Thulium und einem Booster von ungefähr gleichem Wert. Eine Truhe geht nie verloren, und du bekommst nie beides.

## Saisonprämie {#season-prize}

Die Saisonprämie hat zwei Stufen. Du holst sie in den **letzten drei Tagen** der Saison ab (Tag 27 bis 29), bis der Countdown des Wipe beginnt. Vor Tag 27 sagt der Reiter **Öffnet an den letzten drei Tagen**, auch wenn du die Tage schon hast. Jede Stufe wird einmal abgeholt, in beliebiger Reihenfolge.

| Stufe | Braucht | Preis |
| :---: | :--- | :--- |
| **1** | 10 abgeholte Tage | Ein **Saison-Souvenir**: ein Look |
| **2** | 20 abgeholte Tage | Ein **Design-Bauplan**: die Technologie eines Schiffsdesigns |

- **Das Souvenir** ist ein Skin, eine Farbe, ein Triebwerksspur-Effekt oder eine Aura ([Kosmetik](/wiki/06-Items/Cosmetics.md)), für die Saison aus einer kurzen Liste dafür zurückgelegter Looks gewählt und nie über Episch. Wie jeder Look dient es nur der Optik, gehört zu deinem Konto und bleibt durch den Wipe. Besitzt du es schon, bekommst du das nächste Souvenir, das dir fehlt. Besitzt du alle, bekommst du 250 Thulium.
- **Der Bauplan** ist die Erforschung eines Schiffsdesigns, für dich erledigt: die Technologie des Designs und die Technologien, die es braucht. Ein Schiff in das Design umzubauen geschieht weiter in der Montage und kostet weiter, was [Schiffsdesigns](/wiki/03-Mechanics/Ship-Designs.md#getting-a-design) sagt. Das Design einer Saison ist eines der 13, in fester Reihenfolge genommen, sodass ein Design 13 Saisons lang nicht wiederkommt. Kennst du es schon, bekommst du das nächste Design, das dir fehlt. Kennst du alle 13, bekommst du 4 Dark Matter Plates, die Gegenstände sind: Leg sie vor dem Wipe in den Transport-Cache.

## Die Geschenke {#the-gifts}

Das Geschenk eines Tages ist klein. Es ist eines von diesen:

- **Munition und Raketen** in bescheidenen Stapeln.
- **Materialien, Platten und Verbrauchsgüter**, darunter Forge kits (die Materialien eines Schritts in der Schmiede).
- **Booster** von ein paar Stunden. Ein Booster-Geschenk fügt seine Stunden deinen [Boostern](/wiki/06-Items/Boosters.md#active-boosters) hinzu.
- **Credits und Thulium** in kleinen Mengen.
- **Ein paar Spezialgegenstände** (Workforce Contract, Forger's Seal): nie mehr als 4 Kacheln einer Saison.

Diese Seite nennt kein Geschenk irgendeiner Saison, weil der Kalender bei jedem Wipe anders ist. Der Reiter Kalender zeigt die Geschenke dieser Saison. Ein Geschenk ist ein Geschenk: Gegenstände aus dem Kalender tragen kein Label **Handelbar** ([Handelbare Gegenstände](/wiki/03-Mechanics/Inventory.md#marketable-items)) und lassen sich nicht in der [Auktion](/wiki/03-Mechanics/Auction.md) anbieten.

## Der Wipe {#the-wipe}

Eine neue Saison ist ein neuer Kalender. Beim [Wipe](/wiki/03-Mechanics/Wipe-Timeline.md) schließt der alte, und der neue öffnet mit seinen eigenen 29 Geschenken, und deine Zählung beginnt wieder bei 0. Der Wipe nimmt nichts von dem, was du abgeholt hast, außer dem, was er jedem Gegenstand nimmt:

- **Gelöscht:** Geschenke, die Gegenstände sind (Munition, Raketen, Materialien, Platten, Verbrauchsgüter), löscht der Wipe, wenn sie nicht in deinem [Transport-Cache](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-) liegen. Der Kalender kennzeichnet so ein Geschenk mit einem Hinweis.
- **Behalten:** Booster, Credits, Thulium, Spezialgegenstände, Looks, Technologien (ein Bauplan) und Container.
- **Die letzten vier Tage (26 bis 29) geben nur Geschenke, die behalten werden**, sodass ein Geschenk der letzten Woche dem Wipe nie zum Opfer fällt.

## Späte Einsteiger und späte Kalender {#late-joiners-and-late-calendars}

**Steigst du mitten in einer Saison ein,** zeigen die Kacheln vor deiner ersten Anmeldung **Vor Beitritt** und lassen sich nicht abholen. Die Truhen und die Saisonprämie verlangen von allen gleich viele Tage, ein später Pilot erreicht also weniger davon. Ein Pilot, der sich zum ersten Mal an Tag 16 anmeldet, hat noch 14 Kacheln, also sind 14 Tage das Meiste, was er abholen kann: Die ersten beiden Truhen und Stufe 1 der Saisonprämie sind erreichbar, Stufe 2 (20 Tage) nicht.

**Auch ein Kalender kann spät starten.** Normalerweise öffnet er mit der Saison. Er kann später öffnen, zum Beispiel wenn das Spiel mitten in einer Saison die Täglichen Belohnungen bekommt. Ein solcher Kalender hat nur die Tage, die noch übrig sind, und alles skaliert mit: Einer, der an Tag 14 öffnet, hat 16 Kacheln („von 16“), Truhen bei 4, 8, 12 und 15 abgeholten Tagen und Stufen der Saisonprämie bei 6 und 11. Die Karte im Dashboard sagt, an welchem Tag er geöffnet hat. Sind weniger als 10 Tage übrig, bekommt die laufende Saison gar keinen Kalender (**In dieser Saison gibt es keinen Kalender**), und der nächste beginnt mit dem Wipe.

## Fragen {#questions}

- **Warum kann ich Tag N nicht abholen?** Es gibt vier Gründe. Der Tag ist noch nicht gekommen (**Öffnet in …**). Der Tag und seine Gnadenfrist sind vorbei (**Verpasst**). Der Tag lag vor deiner ersten Anmeldung (**Vor Beitritt**). Oder der Countdown des Wipe läuft. Eine Saison ohne Kalender oder ein ausgeschalteter Kalender hat nichts zum Abholen.
- **Folgt er meiner Zeitzone?** Nein. Der Tag ist ein UTC-Tag. Nur die angezeigten Uhrzeiten werden in deine Zeitzone umgerechnet ([Der Tag](#the-day)).
- **Was, wenn der Server ausgefallen war?** Die 6 Stunden Gnadenfrist decken einen kurzen Ausfall um Mitternacht ab. Bei einem längeren kann ein Administrator einen Tag für alle länger offen halten. Seine Kachel zeigt sich dann als **Gestern** mit eigenem Countdown.
- **Kann ich zwei Tage auf einmal abholen?** Nur solange zwei Kacheln offen sind, in den 6 Stunden nach einer UTC-Mitternacht: die von gestern und die von heute, je ein Druck. Eine Kachel lässt sich weder zweimal noch im Voraus abholen.
- **Muss ich mich jeden Tag anmelden?** Nein. Es gibt keine Serie: Ein Tag, den du auslässt, kostet dich das Geschenk dieses Tages, und die Truhen und die Saisonprämie zählen nur, wie viele Tage du abgeholt hast.
- **Ändert Premium etwas?** Nein. Premium gibt keine zusätzlichen Kacheln und keine besseren Geschenke, und der Kalender verschenkt keine Premium-Tage.
- **Brauche ich einen Clan?** Nein. Der Kalender nutzt denselben Tag wie die Tageslinie der Clans, aber er gehört dir allein.
- **Gibt es eine Levelgrenze?** Nein. Jeder Pilot kann abholen, ab Level 1.
- **Was passiert beim Wipe?** Du bekommst einen neuen Kalender und fängst wieder bei 0 Tagen an. Geschenke, die Gegenstände sind, werden gelöscht, wenn sie nicht im Transport-Cache liegen; der Rest bleibt ([Der Wipe](#the-wipe)).

## Gut zu wissen {#good-to-know}

- Die Geschenke, die Zahlen und die Gnadenfrist werden auf dem Spielserver festgelegt und können sich mit einem Update ändern; der Reiter Kalender zeigt immer die geltenden.
- Ein Spielserver aus der Zeit vor den Täglichen Belohnungen hat keinen Kalender, und die Karte und der Reiter bleiben verborgen. Ein Administrator kann den Kalender auch ausschalten; was du abgeholt hast, bleibt abgeholt.
- Jeder neue Kalender wird vor dem Wipe angelegt, damit die Administratoren des Spiels ihn vor dem Start ansehen und ein falsches Geschenk ändern können.
