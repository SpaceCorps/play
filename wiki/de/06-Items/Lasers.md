<!-- wiki-i18n source: d64d048fd518e14c -->
<!-- wiki-i18n title: Laser -->
# Laser & Munition {#lasers-ammo}

Waffen sind in SpaceCorps das wichtigste Mittel, Schaden zu verursachen.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Quantum Laser 1 | laser, shoddy | buy 8000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 2 | laser, common | buy 80000 Credits | /wiki/06-Items/Lasers.md#lasers
Quantum Laser 3 | laser, rare | craft 1500 Thulium, 60 s | research 10800 s, 10800 science | 10 Ship Fragment, 2 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Starfire-3 | laser, mythical | craft 100000 Credits, 1500 Thulium, 60 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Quantum Laser 3, 15 Ship Fragment, 1 Reinforced Hull Plate, 8 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Helios Beam | laser, mythical | craft 2000 Thulium, 180 s | research 86400 s, 86400 science, 10 Dark Matter | 1 Starfire-3, 4 Reinforced Hull Plate, 2 Power Core, 50 Cataclysite, 18 Orvium Reinforced Plate | /wiki/06-Items/Lasers.md#lasers
Damage Amp 1 | laser-amp, shoddy | buy 10000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Crit Amp 1 | laser-amp, shoddy | buy 15000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Arc Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Focus Amp | laser-amp, uncommon | buy 60000 Credits | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Pulse Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Prism Amp | laser-amp, rare | buy 1500 Thulium | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Nova Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Pulse Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Apex Amp | laser-amp, epic | craft 1200 Thulium, 60 s | research 36000 s, 36000 science, 10 Dark Matter | 1 Prism Amp, 1 Power Core, 30 Cataclysite, 3 Velkonite Reinforced Plate | /wiki/06-Items/Lasers.md#laser-amplifiers-amps-
Standard Battery | ammo, common | buy 10 Credits | /wiki/06-Items/Lasers.md#laser-ammunition
Siphon Battery | ammo, rare | buy 0.25 Thulium | /wiki/06-Items/Lasers.md#siphon-battery
Advanced Plasma | ammo, rare | buy 0.5 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Ultra Core | ammo, rare | buy 1 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition
Experimental Fusion Core | ammo, epic | buy 2.2 Thulium | /wiki/06-Items/Lasers.md#laser-ammunition

Quantum Laser 1 -> Quantum Laser 2 -> Quantum Laser 3 => Starfire-3 => Helios Beam
Damage Amp 1 -> Arc Amp -> Pulse Amp => Nova Amp
Crit Amp 1 -> Focus Amp -> Prism Amp => Apex Amp
Standard Battery -> Advanced Plasma -> Ultra Core -> Experimental Fusion Core
```
<!-- item-tree:end -->

## Laser {#lasers}

Rüste Laser direkt in den Laser-Slots des Schiffs oder in Drohnen aus, um deine Angriffskraft zu erhöhen.

| Name | Seltenheit | Grundschaden | Krit-Chance | Reichweite | Verstärker-Slots | Kosten |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Quantum Laser 1** | Minderwertig | 55 | – | 600 | 1 | 8.000 Credits |
| **Quantum Laser 2** | Gewöhnlich | 65 | – | 700 | 2 | 80.000 Credits |
| **Quantum Laser 3** | Selten | 80 | 10 % | 800 | 3 | Nur herstellbar |
| **Starfire-3** | Mythisch | 135 | 15 % | 850 | 3 | Nur herstellbar |
| **Helios Beam** | Mythisch | 185 | 25 % | 900 | 3 | Nur herstellbar |

Die Spalte Reichweite ist die jedes einzelnen Lasers. **Dein Schiff feuert mit dem Durchschnitt der Reichweiten seiner Laser** (die Laser in deinen Drohnen zählen mit), auf die nächste ganze Einheit gerundet, und jeder Laser feuert, sobald das Ziel innerhalb dieser Entfernung liegt. Ein Starfire-3 neben zwei Quantum Laser 2 gibt einem Schiff die Reichweite 750, nicht 850; drei Starfire-3 behalten 850, und lauter gleiche Laser ändern nichts. Ein Reichweiten-Bonus aus der Schmiede zählt auf seinem eigenen Laser, bevor der Durchschnitt gebildet wird. Ohne Laser zeigt der Hangar keine Reichweite (einen Strich), und die Laser können nicht feuern, deine Raketen aber schon, jede mit ihrer eigenen Reichweite (siehe [Raketen](/wiki/06-Items/Rockets.md)). Im Hangar steht auf der Kachel „Ø Reichweite“, wo sich deine Laser unterscheiden, und fährst du mit der Maus darüber, werden die Reichweiten der einzelnen Laser aufgelistet.

Quantum Laser 1 und 2 haben keine eigene Krit-Chance („–“): Ein Schadens- oder Krit-Verstärker in ihren Slots bringt sie mit. Kritische Treffer erscheinen in den schwebenden Schadenszahlen in einer anderen Farbe (eisblau, größer, mit einem „!“).

### Die obersten drei Laser herstellen {#making-the-top-three-lasers}

Der **Quantum Laser 3**, der **Starfire-3** und der **Helios Beam** werden nur in der **Montage** hergestellt. Der Quantum Laser 3 wird nicht mehr im Shop verkauft; ein Pilot, der bereits einen besitzt, behält ihn. Jedes Rezept verlangt Platten aus der [Skylab](/wiki/03-Mechanics/Skylab.md)-Schmiede:

| Laser | Herstellungszeit | Was er braucht |
| :--- | :---: | :--- |
| Quantum Laser 3 | 1 min | 10 Ship Fragments, 2 Velkonite Reinforced Plates, 1.500 Thulium |
| Starfire-3 | 1 min | 1 Quantum Laser 3, 15 Ship Fragments, 8 Velkonite Reinforced Plates, 1 Reinforced Hull Plate, 1.500 Thulium, 100.000 Credits |
| Helios Beam | 3 min | 1 Starfire-3, 50 Cataclysite, 2 Power Cores, 18 Orvium Reinforced Plates, 4 Reinforced Hull Plates, 2.000 Thulium |

Die Montage-Seite zeigt, was du hast, im Vergleich zu dem, was ein Rezept verlangt, und die Schaltfläche „Herstellen“ sagt, was dir fehlt. Zeigst du auf das Bild oder den Namen eines Rezepts oder auf eines seiner Materialien, erscheinen die vollständige Beschreibung und die Werte des Gegenstands.

**Der Starfire-3 wird aus einem Quantum Laser 3 hergestellt.** Du stellst zuerst den Quantum Laser 3 her, und der Starfire-3 verbraucht ihn. Was der Quantum Laser 3 schon gekostet hat, wird nicht noch einmal verlangt, die beiden zusammen kosten also genau das, was ein Starfire-3 allein gekostet hat: 3.000 Thulium, 100.000 Credits, 25 Ship Fragments, 10 Velkonite Reinforced Plates, 1 Reinforced Hull Plate und 2 Minuten. Hast du schon einen Quantum Laser 3, bezahlst du nur den eigenen Teil des Starfire-3. Es gelten die Regeln des Helios Beam, die unten stehen: Der Starfire-3 behält die Verzauberungsstufe des Quantum Laser 3, den er verbraucht (ein Quantum Laser 3 (Göttlich) ergibt einen Starfire-3 (Göttlich)), und seine Boni werden neu ausgewürfelt; du wählst, welcher Quantum Laser 3 geht, die Karte fragt vorher nach, bevor sie einen über Standard verwendet, und der Quantum Laser 3 muss lose sein: **Lege ihn zuerst von deinem Schiff ab** (seine Verstärker gehen zurück in dein Inventar) und nimm ihn aus dem Transport-Cache. Die Schaltfläche „Herstellen“ sagt „Quantum Laser 3 zuerst ausbauen“, wenn er auf einem Schiff liegt.

**Der Helios Beam wird aus einem Starfire-3 hergestellt.** Du stellst zuerst den Starfire-3 her (3.000 Thulium und 100.000 Credits mit seinem Quantum Laser 3), und der Helios Beam verbraucht ihn, so wie die [Master Drone](/wiki/06-Items/Drones.md) eine Slave Drone verbraucht. Was der Starfire-3 schon gekostet hat, wird nicht noch einmal verlangt, die beiden zusammen kosten also die 5.000 Thulium, das Cataclysite, die Power Cores und die Reinforced Hull Plates, die der Helios Beam allein verlangte, und 18 Orvium-Platten statt 20 (die zehn Velkonite-Platten des Starfire-3 ersetzen die fehlenden zwei); darüber hinaus bezahlst du die 100.000 Credits und 25 Ship Fragments des Starfire-3. Es gilt die Regel der [Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly): Der Helios Beam behält die Verzauberungsstufe des Starfire-3, den er verbraucht (ein Starfire-3 (Göttlich) ergibt einen Helios Beam (Göttlich)), und seine Boni werden neu ausgewürfelt; du wählst, welcher Starfire-3 geht, wenn du mehrere besitzt, und die Karte fragt vorher nach, bevor sie einen über Standard verwendet. Der Starfire-3 muss lose sein: **Lege ihn zuerst von deinem Schiff ab** (die in ihn eingesetzten Verstärker gehen zurück in dein Inventar) und nimm ihn aus dem Transport-Cache. Die Schaltfläche „Herstellen“ sagt „Starfire-3 zuerst ausbauen“, wenn er auf einem Schiff liegt.

Woher die Platten kommen:

- **Velkonite Reinforced Plates** (Quantum Laser 3 und Starfire-3) werden aus Velkonite geschmiedet, 40 Erz pro Platte auf Schmiede-Level 1. **Orvium Reinforced Plates** (Helios Beam) werden aus Orvium geschmiedet, 80 Erz pro Platte.
- Das Erz kommt nur aus den Kollektoren deines Skylab. Ein Velkonite-Kollektor auf Level 5 baut etwa 29 Velkonite pro Stunde ab, die Platten eines Quantum Laser 3 brauchen also etwa 3 Stunden Abbau und die zehn Platten eines Starfire-3 (zwei in seinem Quantum Laser 3, acht in seinem eigenen Schritt) etwa 14. Der Helios Beam ist der langwierige: Seine 18 Platten brauchen 1.440 Orvium, etwa 4 Tage von einem Orvium-Kollektor auf Level 5.
- Das Ressourcenlager fasst auf Level 1 je 900 Erz jeder Sorte, schmiede also laufend (eine Charge der Schmiede sind auf Level 1 10 Platten) oder baue das Lager aus.
- Geschmiedete Platten warten in der Schmiede, bis du sie abholst, während dein Schiff gelandet ist, und landen als gewöhnliche Gegenstände in deinem Inventar.

Ship Fragments, Cataclysite, Power Cores und Reinforced Hull Plates fallen bei Aliens ab; jede Quelle und Verwendung jedes Materials steht auf der Seite [Ressourcen](/wiki/06-Items/Resources.md); die Beutelisten auf den Seiten des [Bulwark](/wiki/04-Aliens/Bulwark.md) und des [Goombah](/wiki/04-Aliens/Goombah.md) zeigen, wie viel.

---

## Laserverstärker (Amps) {#laser-amplifiers-amps-}

Setze sie direkt in den Slot eines Lasers ein, um seine Eigenschaften zu verstärken. Es gibt zwei Linien mit je vier Sprossen: Die **Schadenslinie** gibt einen festen Betrag an Schaden, und die **Krit-Linie** gibt Krit-Chance und festen Krit-Schaden.

| Name | Seltenheit | Grundschadens-Boost | Krit-Chance-Boost | Fester Krit-Schaden | Kosten |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Damage Amp 1** | Minderwertig | +10 | +5 % | +5 | 10.000 Credits |
| **Arc Amp** | Ungewöhnlich | +16 | +5 % | +8 | 60.000 Credits |
| **Pulse Amp** | Selten | +26 | +6 % | +13 | 1.500 Thulium |
| **Nova Amp** | Episch | +38 | +7 % | +20 | Nur herstellbar |
| **Crit Amp 1** | Minderwertig | +0 | +15 % | +0 | 15.000 Credits |
| **Focus Amp** | Ungewöhnlich | +0 | +20 % | +14 | 60.000 Credits |
| **Prism Amp** | Selten | +0 | +25 % | +24 | 1.500 Thulium |
| **Apex Amp** | Episch | +0 | +25 % | +44 | Nur herstellbar |

Der Nova Amp und der Apex Amp werden in der [Montage](/wiki/06-Items/Overview.md#upgrading-modules) aus einem Pulse Amp und einem Prism Amp hergestellt, mit Thulium, Beute und je 3 Velkonite Reinforced Plates aus deinem Skylab. Sie behalten die Verzauberungsstufe des Verstärkers, den sie verbrauchen, und ihre Boni werden neu ausgewürfelt ([Modul-Upgrades](/wiki/06-Items/Forge.md#module-upgrades-in-the-assembly)).

### Welcher Verstärker wohin gehört {#which-amp-goes-where}

Ein Schadensverstärker gibt jedem Laser denselben Schaden dazu, ist also auf den **Quantum Lasern** am meisten wert. Ein Krit-Verstärker vervielfacht, was der Laser ohnehin leistet, ist also umso mehr wert, je härter der Laser trifft: Auf dem **Starfire-3** zieht er mit der Schadenslinie gleich, und auf dem **Helios Beam** liegt er etwa 3,5 % vorn. Die Krit-Chance eines Lasers endet bei 100 %: Drei Prism Amps oder Apex Amps bringen einen Helios Beam genau dorthin.

Mit demselben Verstärker bestückt, ist ein Laser immer stärker als der unter ihm, ein besserer Verstärker ersetzt also nie einen besseren Laser: Ein Quantum Laser 3 mit drei Nova Amps leistet weniger als ein Helios Beam mit drei Damage Amp 1 (bei Teilen derselben Verzauberungsstufe: Ein Quantum Laser 3 und Nova Amps, die auf Göttlich oder höher geschmiedet wurden, können mit den besten Würfen einen schlichten Helios Beam in Damage Amp 1 überholen, auf Göttlich um Haaresbreite).

---

## Lasermunition {#laser-ammunition}

Verbrauchsbatterien, die den Schaden deiner Laser-Salven vervielfachen:

| Name | Seltenheit | Schadensfaktor | Schilddurchdringung | Preis pro Einheit |
| :--- | :--- | :---: | :---: | :--- |
| **Standard Battery** | Gewöhnlich | 1,0x | – | 10 Credits |
| **Advanced Plasma** | Selten | 2,0x | – | 0,5 Thulium |
| **Ultra Core** | Selten | 3,0x | 5 % | 1,0 Thulium |
| **Experimental Fusion Core** | Episch | 4,0x | 10 % | 2,2 Thulium |
| **Siphon Battery** | Selten | 1,0x, nur Schilde | – | 0,25 Thulium |

Die **Schilddurchdringung** wird bei jedem Treffer deiner Salven von der Absorption deines Ziels abgezogen: Die Schilde nehmen die Absorption des Ziels abzüglich der Durchdringung (siehe [Schildmechanik](/wiki/03-Mechanics/Shields.md#shield-penetration)). Gegen ein Schiff mit 80 % (der beste Schild mit den besten Zellen) lassen die 10 % der x4-Munition den Schilden 70 % des Treffers und der Hülle 30 %. Sie zählt am meisten gegen Schiffe, deren Hülle neben ihrem Schild klein ist; ein sehr großes Schiff mit 80 % hält so oder so gleich viel aus. Aliens haben keinen nennenswerten Absorptionswert (ihre Schilde nehmen 80 % eines Treffers), und die Durchdringung wird auch davon abgezogen.

### Siphon Battery {#siphon-battery}

Die Siphon Battery ist Munition, um Schilde zu rauben, statt Hüllen zu brechen. Sie verursacht **x1 Schaden direkt am Schild des Ziels** und schreibt dieselbe Menge **deinem eigenen Schild** gut, bis zu deinem Maximum. Wähle sie in der Munitionsauswahl der Aktionsleiste wie jede andere Munition (es ist die Kachel mit dem türkisen Wirbel). Sie feuert keinen Strahl: Eine dünne, schwache türkise Sonde fliegt zum Ziel, der Schild des Ziels flammt dort türkis auf, wo sie trifft, und der Schild, den du abgesaugt hast, strömt sichtbar als leuchtende türkise Pakete zu deinem Schiff zurück (drei bis zehn, mehr bei einem größeren Entzug), eines nach dem anderen über etwa eine halbe Sekunde. Jedes Paket, das ankommt, lässt deinen Schild pulsieren. Dasselbe siehst du bei der Siphon Battery jedes Piloten in Sichtweite, egal wen sie anzapft: Aliens, andere Piloten und die Schiffe von Konzernpiloten.

- **Nur Schild**: Die Hülle wird nie berührt, die Absorption des Ziels teilt den Schaden nicht auf, und eine Siphon Battery kann nie etwas zerstören. Ihr Schaden ist durch das begrenzt, was der Schild des Ziels noch hält.
- **Nichts zu holen**: Gegen ein Ziel ohne Schild entzieht sie nichts und gibt nichts. Die Salve ist trotzdem verbraucht, eine Batterie pro Laser, wie bei jeder Munition. Du siehst nur die Sonde und ein mattes Flackern auf der Hülle, und keine Pakete.
- **Gewinn**: Dein Schild geht nie über sein Maximum, und das Aufnehmen von Schild verzögert deine eigene Schildregeneration nicht.
- **Aliens und Piloten** haben gleichermaßen Schilde, die sich absaugen lassen. Ein Entzug, der einem Alien Schild nimmt, zählt als Treffer für den [Ersttreffer-Anspruch](/wiki/03-Mechanics/Combat.md); einer, der keinen Schild findet, nicht. Er weckt auch einen Seeker oder einen Goombah, die nur zurückschlagen, wie jeder andere Treffer.
- **Kritische Treffer** zählen: Eine kritische Salve entzieht 1,5-mal so viel, und ihre Zahl wird als kritischer Treffer dargestellt. Ihre Pakete sind größer und heller, und der Schild des Ziels flammt stärker auf.
- [Konzernpiloten](/wiki/03-Mechanics/Company-Pilots.md) feuern Standardmunition x1.
