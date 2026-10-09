<!-- wiki-i18n source: 5e11f7d9fa6eb28d -->
<!-- wiki-i18n title: Inventar -->
# Inventar & Ausrüstung {#inventory-equipment}

Im Hangar verwaltest du deine Schiffe und deine Ausrüstung. Gegenstände wirksam auszurüsten ist der Schlüssel zum Überleben und zur Vorherrschaft. Du kannst das an der Station tun und im Flug aus einer Schutzzone heraus: siehe [Der Hangar im Flug](/wiki/03-Mechanics/Hangar.md).

## Ausrüstungs-Slots & Wirkungsgrade der Werte {#equipment-slots-stat-efficiencies}

Anders als in herkömmlichen Weltraumspielen hat SpaceCorps dynamisch gestufte Ausrüstungs-Slots, die die Wirksamkeit der eingesetzten Module skalieren.

- **Laser-Slots**: Für Angriffswaffen (Laser). Diese arbeiten immer mit **100 % Schaden und Reichweite**.
- **Generator-Slots**: Gemeinsame Slots für Schilde, Triebwerke und adaptive Kerne. Sie sind in drei Wirkungsgrad-Stufen eingeteilt, und die Stufe entscheidet, wie viel von den Grundwerten eines Gegenstands zählt. Im Hangar hat jede Stufe neben ihrem Namen ein (i), das sie erklärt:
  - **Kern-Slots**: Gegenstände, die hier sitzen, erhalten **100 %** ihrer Grundwerte. Jedes Schiff hat sie: Setze hier deine stärksten Schilde und Triebwerke ein.
  - **Support-Slots**: Gegenstände, die hier sitzen, erhalten **75 %** ihrer Grundwerte (z. B. 75 % des Tempos oder der Schildkapazität). Jedes Schiff hat sie.
  - **Hilfs-Slots**: Gegenstände, die hier sitzen, erhalten **50 %** ihrer Grundwerte. Nur manche Schiffe haben sie (die Nomad hat 1, die Paragon und die Storm 2, die Ironclad 3 und die Wraith 4; die Protos, Kitefin und Ostirion haben keine). Sie eignen sich am besten für zusätzliche, schwächere Schilde und Triebwerke, während deine stärksten in die Kern-Slots kommen.
  - **Drohnen-Slots**: Ein Schild auf einer deiner Drohnen zählt wie einer in einem Kern-Slot, **100 %** seiner Werte (siehe [Drohnenmechanik](/wiki/03-Mechanics/Drones.md)).
  - **Nicht zugewiesene Slots/Alt-Slots**: Gegenstände, die hier sitzen, tragen nichts zu den Werten bei.
  - **Auch das Stapeln lässt nach**: Schilde und Triebwerke werden nach Stärke geordnet, die stärksten zuerst (nach dem, was jedes nach dem Anteil seines Slots zählt), und der Anteil der Stufe wird dann mit dem ihres Rangs multipliziert: Der 1. bis 4. zählt voll, der 5. bis 7. mit 85 %, 70 % und 55 %, ab dem 8. mit 50 % bei Schilden und 25 % bei Triebwerken. Siehe [Schilde](/wiki/03-Mechanics/Shields.md) und [Tempo](/wiki/03-Mechanics/Speed.md).
- **Extra-Slots**: Für spezialisierte Hilfsgegenstände, etwa Repair Drones. Protos, Kitefin, Ostirion und Nomad haben zwei; Paragon, Ironclad, Wraith und Storm, die du baust, haben drei. Die Extra Slots CPUs ([Extras](/wiki/06-Items/Extras.md#extra-slots-cpus)) geben 3, 5 oder 7 dazu.
- **Panzerungs-Slots**: Für [Hüllenpanzerung](/wiki/06-Items/Hull-Plating.md#hull-plate-slots), die Hülle hinzufügt. Nur die vier Schiffe, die du baust, haben sie (die Paragon 5, die Storm 7, die Ironclad 15 und die Wraith 9), jeder gesperrt, bis du ihn im Skylab erforschst, und sie sind in beiden Konfigurationen gleich.

## Reihenfolge im Inventar {#inventory-order}

Das Inventar listet deine Gegenstände in derselben Reihenfolge wie der Shop auf, egal in welcher Reihenfolge du sie gekauft, hergestellt oder gefunden hast. Arten, die zusammengehören, stehen zusammen: Laser, Laserverstärker und Lasermunition; Schilde und Schildzellen; Triebwerke und Schubdüsen; adaptive Kerne; Extras (Repair Drones); Drohnen und Drohnenformationen; dann Ressourcen. Innerhalb einer Art kommt das Günstigste zuerst (Credits vor Thulium), dann das, was keinen Preis hat: nur herstellbare Ausrüstung und Beute, die schwächste Seltenheit zuerst (Laser einer Seltenheit, der mit dem schwächsten Schaden zuerst). Lasermunition steht von x1 bis x4, dann die Siphon Battery. Raketen sortieren sich nach Art (Einzelziel vor Flächenschaden, gelenkt vor geradeaus) und dann nach Stufe, daher steht die epische Rakete, die Thulium kostet, in ihrer Art zuletzt. Exemplare eines Gegenstands sortieren sich nach ihrer Verzauberungsstufe. Über dem Raster steht pro Art ein Chip in derselben Reihenfolge, jeweils mit der Zahl der Gegenstände, die die Suche darin findet. Jeder Chip lässt sich einzeln ein- oder ausschalten, sodass du Munition und Repair Drones ausblenden kannst, während du an Lasern, Schilden und Triebwerken arbeitest: Klicke einen Chip an, um seine Art ein- oder auszublenden; ein Shift-Klick (oder Doppelklick) lässt nur diese Art eingeschaltet, und ein weiterer Klick darauf holt den Rest zurück. **Alle** zeigt jede Art, und **Keine** blendet alle aus, damit du nur die einschaltest, die du willst. Ein durchgestrichener Chip ist aus, ein Chip mit Häkchen ist an. Die Suche arbeitet mit den Arten, die an sind, und deine Wahl wird bei deinem Piloten gespeichert. Ist alles ausgeblendet, sagt das Raster das und bietet **Alle Kategorien anzeigen** an.

## Handelbare Gegenstände {#marketable-items}

Gegenstände, die du verdient hast (Beute, Missionsbelohnungen und alles, was die Montage und die Schmiede herstellen), tragen auf ihrer Kachel ein kleines Etikett **Handelbar**, und die Gegenstandskarte zeigt „Handelbar“ oder, bei einem Stapel, von dem nur ein Teil verkauft werden kann, „Handelbar (3 von 5)“. Der Chip **Nur Handelbares** neben den Kategorie-Chips zeigt nur diese Gegenstände. Ein **Auktionshammer** neben dem Mülleimer eines markierten Gegenstands öffnet das Verkaufsblatt der [Auktion](/wiki/03-Mechanics/Auction.md) (im Flug wird er nicht angezeigt: Verkaufen ist eine Seite der Station). Was du gekauft, gewonnen oder geschenkt bekommen hast, trägt kein Etikett und kann nicht wieder verkauft werden.

## Gegenstand in Gegenstand ausrüsten (Sub-Sockets) {#item-to-item-equipping-sub-sockets-}

Manche Hauptgegenstände können sekundäre Hilfsgegenstände „ausrüsten“ (man spricht von Sub-Socketing), um ihre Werte zu verstärken. Um etwas in einen Sub-Socket zu setzen, ziehe den Hilfsgegenstand direkt auf den Hauptgegenstand in deinem Hangar-Inventar.

### Verträglichkeitstabelle {#compatibility-table}

| Hauptgegenstand | Zulässige Sub-Socket-Gegenstände | Resultierende Wirkung |
| :--- | :--- | :--- |
| **Laser** | Laserverstärker (Amp) | Erhöht Grundschaden und Werte für kritische Treffer oder zieht Punkte von der Absorption des Ziels ab (Penetration Amp) |
| **Schild** | Schildzelle | Erhöht Schildkapazität und Aufladerate |
| **Triebwerk** | Schubdüse | Erhöht Tempo und Faktoren des Triebwerks |
| **Hybridgenerator** | Schildzelle ODER Schubdüse | Erhöht Schildkapazität, Aufladerate oder Tempo |
| **Drohne** | Laser oder Schild, in jedem ihrer Slots (eine Master Drone hat zwei) | Ein Laser fügt deiner Salve seinen Schaden hinzu; ein Schild zählt wie einer in einem Kern-Slot (100 % seiner Werte) |

---

## Munitionsverwaltung {#ammo-management}

Lasermunition ist eine verbrauchbare Ressource.
- Munition stapelt sich in deinem Inventar.
- Die aktive Lasermunition kannst du über die Aktionsleiste deines HUDs wechseln.
- Hochwertigere Munition bringt Schadensfaktoren (z. B. Standard x1, Advanced Plasma x2, Ultra Core x3, Experimental Fusion Core x4). Die Siphon Battery verursacht x1 Schaden nur an Schilden und gibt ihn an deinen eigenen Schild weiter.
