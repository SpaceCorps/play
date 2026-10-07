<!-- wiki-i18n source: 5326d0eb87e5eb5c -->
<!-- wiki-i18n title: Clans -->
# Clans

Einen Clan zu gründen oder ihm beizutreten, erlaubt es dir, Ressourcen zu bündeln, die gemeinsame Bank aufzuwerten, Steuersätze festzulegen, dich mit Fraktionsmitgliedern abzustimmen und Diplomatie zu betreiben. Ein Clan hat außerdem gemeinsame Arbeit: Jeden Tag bekommt er eine **Tageslinie** aus Missionen, die mit einem Boss endet, den nur der Clan verletzen kann, und die Punkte, die er dabei verdient, kaufen **dauerhafte Boni** für jedes Mitglied. (Auf der Clan-Seite des Spiels heißt ein Clan „Flotte“, seine Punkte und Boni heißen dort Flottenpunkte und Flottenboni.)

**In einer Minute**

- Jeden Saisontag bekommt dein Clan eine [Tageslinie](#daily-line): vier Missionen der Reihe nach (Aliens abschießen, eine Strecke fliegen, an manchen Tagen Schwarm-Bosse erledigen), danach einen [Clan-Wächter](#clan-wardens), einen Boss, den du rufst und den nur dein Clan verletzen kann.
- Jeder abgeschlossene Schritt zahlt sofort Clanpunkte: 15, 15, 20, 20 und 30, also **100 Punkte** für eine ganze Linie.
- Der Anführer und die Stellvertreter geben die Punkte für drei [Boni](#clan-points-and-boosts) mit je zehn Stufen aus: **Schaden** (bis +5 %), **Thulium** (bis +10 %) und **Credits** (bis +10 %).
- Ein Clan, der jede Linie schafft, hat am **Saisontag 12** jede Stufe gekauft. Punkte und Stufen beginnen mit jedem Wipe neu.
- Du brauchst mindestens **drei Mitglieder**, die ihren Teil geleistet haben, und **etwa sieben Piloten** für den Kampf gegen den Wächter: Fünf verlieren meistens, zehn gewinnen mühelos ([wie groß die Besatzung sein muss](#how-big-a-crew)). Eine zu kleine Besatzung verliert den Kampf: Der Clan behält dann die **70 Punkte** der vier Missionen, aber die Linie ist nicht abgeschlossen und zahlt keine [Belohnung für dich](#the-reward-for-you).
- Dein Schiff zeigt die Boni, die es hat, im **Booster-Fenster** auf einer eigenen Karte ([wo du sie siehst](#the-three-boosts)).
- Linie und Boni brauchen ein Spiel ab Version 0.4.10, die Karte im Booster-Fenster ab 0.4.12.

![The Boosters window in flight: the Clan boosts card under the timed boosters lists your clan's tag and each boost with its bonus and level](../../img/wiki-img/shots/clan-boosters-window.jpg)
![Buying a level of a clan boost: the sheet shows the level, the bonus the whole fleet gets and the cost in clan points](../../img/wiki-img/shots/clan-boosts.jpg)
![Summoning a Warden for the clan](../../img/wiki-img/shots/clan-warden.jpg)

## Clan-Fortschritt {#clan-progression}

Clans beginnen auf Level 1 und lassen sich bis auf Level 5 aufwerten. Für das Aufwerten des Clans müssen Credits aus der **Clanbank** gezahlt werden. Upgrades erhöhen die Mitgliederkapazität und die täglichen Auszahlungslimits.

| Clan-Level | Mitgliederlimit | Tägliches Auszahlungslimit (pro Mitglied) | Upgrade-Kosten (Credits) |
| :---: | :---: | :---: | :--- |
| **Level 1** | 10 | 1.000.000 Cr | — |
| **Level 2** | 25 | 2.000.000 Cr | 10.000.000 Cr |
| **Level 3** | 50 | 3.000.000 Cr | 100.000.000 Cr |
| **Level 4** | 75 | 4.000.000 Cr | 1.000.000.000 Cr |
| **Level 5** | 100 | 5.000.000 Cr | 10.000.000.000 Cr |

---

## Clan-Wirtschaft & Besteuerung {#clan-economy-taxation}

Clans arbeiten mit einem steuerbasierten Finanzsystem:

### 1. Tägliche Besteuerung {#1-daily-taxation}

- **Steuersatz**: Der Anführer oder die Stellvertreter können einen täglichen Steuersatz zwischen **0 % und 5 %** festlegen.
- **Automatische Einziehung**: Einmal pro Tag (UTC) zieht der Server die Steuern automatisch von allen Clanmitgliedern ein.
- **Formel**: Die Steuer wird als `ClanTaxRate` des aktuellen Credit-Guthabens jedes Mitglieds berechnet.
  - *Beispiel*: Hast du 10.000.000 Credits und beträgt die Clan-Steuer 2 %, werden 200.000 Credits von deinem Konto abgezogen und in die Clanbank eingezahlt.
  - Freiwillige Credit-Spenden sind ebenfalls möglich, bis zur Grenze im nächsten Abschnitt.

### 2. Spenden {#2-donations}

- **Spenden**: Jedes Mitglied kann auf der Clan-Seite Credits in die Clanbank einzahlen. Das Fenster zeigt, was du noch senden kannst.
- **Spendenlimit**: Ein Pilot kann in beliebigen 24 Stunden höchstens **1.000.000 Credits in Clans einzahlen**, gezählt über alle Clans, in denen der Pilot war. Der Austritt aus einem Clan und der Beitritt zu einem anderen gibt kein neues Kontingent.
- **Kein Tageswechsel**: Die 24 Stunden gleiten mit. Jede Spende zählt genau 24 Stunden nach ihrem Zeitpunkt nicht mehr mit, und das Fenster sagt dir, wann das bei der ältesten der Fall ist und wie viel zurückkommt. Eine Spende über dem, was übrig ist, wird als Ganzes abgelehnt.
- Die tägliche Steuer ist keine Spende und verbraucht dein Kontingent nicht.

### 3. Auszahlungen aus der Bank {#3-bank-payouts}

- **Auszahlungslimits**: Clan-Anführer und Offiziere können Credits aus der Clanbank an einzelne Mitglieder verteilen.
- **Tageslimit**: Ein Mitglied kann an einem einzigen Kalendertag (UTC) nicht mehr als `1,000,000 * ClanLevel` Credits an Auszahlungen erhalten.

---

## Hierarchie & Rollen {#hierarchy-roles}

Clans nutzen eine rollenbasierte Rangstruktur, um Berechtigungen zu verwalten:

- **Anführer (Rolle 3)**: Hat vollständigen Verwaltungszugriff: Upgrades, Steuern, Diplomatie, Beförderungen, Entlassungen und die Auflösung des Clans.
- **Stellvertreter (Rolle 2)**: Kann Steuersätze festlegen, Credits auszahlen, die Diplomatie verwalten und niedrigere Ränge befördern oder degradieren.
- **Ältester (Rolle 1)**: Vertrautes Mitglied, das neue Bewerbungen für den Clan annehmen kann.
- **Mitglied (Rolle 0)**: Normaler Spieler ohne Verwaltungsrechte.

### Berechtigungstabelle {#permissions-table}

| Aktion | Anführer | Stellvertreter | Ältester | Mitglied |
| :--- | :---: | :---: | :---: | :---: |
| **Clan auflösen** | ✅ | ❌ | ❌ | ❌ |
| **Clan aufwerten** | ✅ | ❌ | ❌ | ❌ |
| **Steuersatz festlegen** | ✅ | ✅ | ❌ | ❌ |
| **Credits auszahlen** | ✅ | ✅ | ❌ | ❌ |
| **Diplomatie verwalten** | ✅ | ✅ | ❌ | ❌ |
| **Clan-Boni kaufen** | ✅ | ✅ | ❌ | ❌ |
| **Clan-Wächter rufen** | ✅ | ✅ | ❌ | ❌ |
| **Befördern / Entlassen** | ✅ | ✅* | ❌ | ❌ |
| **Bewerbungen annehmen** | ✅ | ✅ | ✅ | ❌ |

*\*Stellvertreter können nur Mitglieder mit einem niedrigeren Rang als ihrem eigenen befördern, degradieren oder entlassen.*

### Wenn der Anführer geht {#when-the-leader-leaves}

Ein Anführer kann einen Clan, der noch andere Mitglieder hat, nicht verlassen: Befördere zuerst einen Stellvertreter zum Anführer (der Anführer tritt zum Stellvertreter zurück) oder gehe als Letzter, wodurch der Clan aufgelöst wird. Löscht der Anführer sein Konto (Einstellungen › Konto), geht die Führung an das ranghöchste Mitglied, bei Gleichstand an das am längsten dienende; ein Anführer, der allein im Clan ist, löst ihn auf, samt Bank.

---

## Tageslinie {#daily-line}

Jeder Clan bekommt täglich eine **Tageslinie**: fünf Schritte, die der ganze Clan gemeinsam **der Reihe nach** erledigt. Die ersten vier sind Missionen: So viele Aliens abschießen, so weit fliegen oder an manchen Tagen Schwarm-Bosse erledigen. Der fünfte ist ein **Clan-Wächter**, ein Boss, den du rufst und zerstörst. Öffne **Community › Clan** und dort den Reiter **Einsätze**, um die heutige Linie, den offenen Schritt mit seinem Balken, deinen eigenen Anteil und die verbleibende Zeit zu sehen.

### Die fünf Schritte {#the-five-steps}

| Schritt | Was | Clanpunkte |
| :---: | :--- | ---: |
| 1 | Erste Mission | 15 |
| 2 | Zweite Mission | 15 |
| 3 | Dritte Mission | 20 |
| 4 | Vierte Mission | 20 |
| 5 | Der Clan-Wächter des Tages | 30 |
| | **Eine abgeschlossene Linie** | **100** |

- Nur der **offene Schritt zählt**. Ein Abschuss, der gelingt, während Schritt 1 offen ist, zählt für Schritt 1 und für nichts sonst. Ist Schritt 1 erledigt, beginnt Schritt 2 bei null. Was du über das Ziel eines Schritts hinaus abschießt, wird nicht für den nächsten aufgehoben.
- Ein Schritt zahlt seine Punkte **in dem Moment, in dem er erledigt ist**. Ein Clan, der die vier Missionen schafft und dann keine Besatzung für den Wächter zusammenbekommt oder den Kampf verliert, behält trotzdem **70 Punkte**; die [Belohnung für dich](#the-reward-for-you) kommt erst mit der abgeschlossenen Linie.
- Die Arbeit aller geht in **einen gemeinsamen Zähler**: Die Abschüsse des Aliens im offenen Schritt und die Strecke, die alle deine Mitglieder fliegen, werden addiert. Niemand muss einen Schritt allein schaffen.

### Der Tag {#the-day}

- Der Tag eines Clans ist ein **Saisontag**: 24 Stunden, gezählt ab dem Start der Saison ([Wipe-Zeitleiste](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)). Eine neue Linie beginnt jeden Tag zur selben Uhrzeit, und die ist nicht Mitternacht UTC (die tägliche Steuer des Clans läuft weiter um Mitternacht UTC). Der Reiter Einsätze zählt bis zum Wechsel herunter.
- Eine Linie, die nicht fertig wird, **verfällt**, wenn der Tag endet. Die erledigten Schritte behalten ihre Punkte, der Fortschritt des offenen Schritts verfällt, und aufholen kann man nicht. Linien laufen an den Saisontagen 1 bis 29.
- Die Piloten des Clans, die online sind, bekommen eine Systemzeile, wenn die neue Linie beginnt, wenn ein Schritt erledigt ist und **eine Stunde vor dem Wechsel**, falls die Linie nicht fertig ist.

### Schwierigkeitsstufen {#difficulty-tiers}

Jeden Tag nimmt das Spiel den **Durchschnitt der Level der fünf Piloten mit dem höchsten Level** im Clan (alle, wenn er weniger als fünf hat) und legt daraus die Stufe des Tages fest:

| Stufe | Durchschnittslevel | Wächter |
| :--- | :--- | :---: |
| Rekrut | unter 4 | I |
| Veteran | 4 bis unter 7 | II |
| Elite | 7 oder mehr | III |

Die Stufe bestimmt, wie viele Aliens die Missionen verlangen, welches Alien der „schwere“ Schritt verlangt und wie stark der Wächter ist. **Die Punkte sind in jeder Stufe gleich.** Neue Piloten mit niedrigem Level ziehen die Stufe nicht herunter: Es zählen nur die fünf besten.

### Wer zählt {#who-counts}

- **Die Summe des Clans zählt.** Die Balken im Reiter Einsätze sind die des ganzen Clans.
- **Dein Minimum.** Um an der Belohnung des Tages teilzuhaben, musst du **5 % der Tagesarbeit** leisten, etwa acht Minuten echte Jagd. Der Reiter zeigt es als „Deine Arbeit heute: 312 von 469 Einheiten“. Eine Arbeitseinheit ist eine Sekunde Spielzeit: Ein Abschuss zählt so viel, wie es dauert, dieses Alien zu finden und zu zerstören, und eine Flugstrecke so viel, wie der Flug dauert. Für einen Veteranen-Clan ist ein Seeker etwa 12 Einheiten wert, ein Phantasm 22, ein Bulwark 123 und 1.000 geflogene Einheiten etwa 5; das Minimum liegt bei 446 bis 480 Einheiten, an jedem Tag und in jeder Stufe.
- **Mindestens drei Mitglieder** müssen ihr Minimum erreicht haben, bevor ein Schritt erledigt sein kann. Ist ein Schritt voll und haben es weniger geschafft, **wartet** er („Schritt 3 ist voll, aber erst 2 Mitglieder haben ihr Minimum erreicht“), und Abschüsse des Aliens dieses Schritts erhöhen weiter die Arbeit der Mitglieder, die sie gemacht haben, bis das dritte es geschafft hat. Ein Clan mit weniger als drei Piloten kann keinen Schritt abschließen.
- **Wer einen Abschuss bekommt.** Der Pilot, der für den Abschuss bezahlt wird, und seine Gruppenmitglieder im Umkreis von 4.000 Einheiten, die in den letzten 15 Sekunden gefeuert haben ([Gruppen](/wiki/03-Mechanics/Groups.md#sharing-kills)). Ein Clan zählt einen Abschuss **einmal**, egal wie viele seiner Piloten in der Gruppe waren, und die Arbeit des Abschusses wird gleichmäßig auf sie verteilt. Zwei Clans in einer Gruppe zählen ihn je einmal.
- **Welche Abschüsse.** Nur das Alien des offenen Schritts: der gewöhnliche Seeker, Phantasm, Bulwark oder Goombah. Schwarmschiffe, andere Piloten und die Helfer eines Wächters zählen nicht als diese Aliens. Jede Welt zählt, und ein Abschuss zählt in einer stärkeren Welt mehr: **1 in Alpha, 1,5 in Beta, 2 in Gamma** ([Welten](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)). Ein Boss-Schritt zählt die Bosse der [Schwärme](/wiki/05-Swarms/Swarms.md), einen für jeden Clan, der einen Piloten hat, der mindestens 5 % des Schadens verursacht hat.
- **Fliegen.** Ein Patrouillen-Schritt zählt die Strecke, die jeder Pilot außerhalb der Schutzzonen fliegt; fünf Piloten, die zusammen fliegen, bringen die fünffache Strecke.
- **Beitreten und Austreten.** Was du getan hast, bleibt gezählt, wenn du gehst. Ein Pilot, der beitritt, zählt ab diesem Moment.

### Die sieben Linien {#the-seven-lines}

Die Linien laufen in einem Zyklus von sieben: Die Linie des Saisontags *d* hat die Nummer 1 + ((*d* − 1) mod 7), jede kehrt also alle sieben Tage wieder. Die Zahlen gelten für einen **Rekruten- / Veteranen- / Elite-**Clan. Die beiden **Swarm-Break**-Linien verlangen Schwarm-Bosse und kommen erst ab Tag 4, wenn die [Schwärme](/wiki/05-Swarms/Swarms.md) erscheinen. Alle Zahlen sind für etwa **2,6 Stunden Spielzeit insgesamt** gemacht, eine halbe Stunde pro Kopf bei fünf Piloten (eine Schätzung, keine Messung).

| Linie | Saisontage | Schritt 1 | Schritt 2 | Schritt 3 | Schritt 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Seeker Sweep | 1, 8, 15, 22, 29 | 150 / 300 / 425 Seeker | 115.000 / 155.000 / 185.000 Einheiten | 21 / 70 / 130 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Phantasm Purge | 2, 9, 16, 23 | 40 / 140 / 270 Phantasm | 60 / 120 / 170 Seeker | 175.000 / 230.000 / 275.000 Einheiten | 26 Phantasm / 15 Bulwark / 17 Goombah |
| Long Haul | 3, 10, 17, 24 | 290.000 / 385.000 / 460.000 Einheiten | 90 / 180 / 260 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah |
| Swarm Break I | 4, 11, 18, 25 | 75 / 150 / 220 Seeker | 3 Boss Seeker / 3 Boss Seeker / 2 Pirate Boss | 26 / 85 / 170 Phantasm | 30 Phantasm / 18 Bulwark / 21 Goombah |
| Heavy Iron | 5, 12, 19, 26 | 40 Phantasm / 24 Bulwark / 28 Goombah | 21 / 70 / 130 Phantasm | 175.000 / 230.000 / 275.000 Einheiten | 75 / 150 / 220 Seeker |
| Swarm Break II | 6, 13, 20, 27 | 75 / 150 / 220 Seeker | 21 / 70 / 130 Phantasm | 4 Boss Seeker / 1 Pirate Boss / 3 Pirate Boss | 350.000 / 460.000 / 550.000 Einheiten |
| Grand Round | 7, 14, 21, 28 | 100 / 210 / 300 Seeker | 26 / 85 / 170 Phantasm | 21 Phantasm / 12 Bulwark / 14 Goombah | 230.000 / 305.000 / 365.000 Einheiten |

### Deine Belohnung {#the-reward-for-you}

Ist die Linie abgeschlossen, das heißt der Wächter zerstört, bekommt jedes Mitglied, das sein Minimum erreicht hat und noch im Clan ist, eine Auszahlung, auch wenn es offline ist. Eine Linie, die ohne den Wächter endet, zahlt keine Belohnung, egal was die vier Missionen geschafft haben. Sie ist pauschal: Boni, Booster und die Welt ändern sie nicht.

| Stufe | Credits | Thulium |
| :--- | ---: | ---: |
| Rekrut | 5.000 | 20 |
| Veteran | 15.000 | 60 |
| Elite | 22.000 | 90 |

---

## Clan-Wächter {#clan-wardens}

Ein **Clan-Wächter** ist der Boss am Ende der Tageslinie. Er ist keiner der öffentlichen [Schwärme](/wiki/05-Swarms/Swarms.md), die durch einen Sektor streifen: Dein Clan **ruft ihn**, und **nur dein Clan kann ihn verletzen**. Drei Wächter wechseln sich ab, einer pro Tag: Tag 1 **Brood**, Tag 2 **Siege**, Tag 3 **Wrath**, Tag 4 wieder Brood und so weiter (Tag 15 ist ein Wrath-Tag). Jeder kommt in drei Stärken, **I, II und III**, die die Stufe des Clans bestimmt. Ein Wächter ist ein Alien eigener Art, wie die Schiffe eines Schwarms: Er zählt nicht als Seeker, Phantasm oder irgendein anderes Alien. Seine Laser treffen hart, ein Wächter ist also ein Kampf für eine volle Besatzung: Bring etwa sieben Piloten mit, denn fünf verlieren meistens ([wie groß die Besatzung sein muss](#how-big-a-crew)).

| Wächter | Saisontage | Rolle | Wie er kämpft |
| :--- | :--- | :--- | :--- |
| **Brood Warden** | 1, 4, 7, 10 … | Hüter des Stocks: teile dein Feuer auf | Vier kleine **Brood Drones** heilen seine Hülle, und alle 8 Sekunden kommt eine neue, solange weniger als vier leben. Erst die Drohnen abschießen, dann den Wächter. |
| **Siege Warden** | 2, 5, 8, 11 … | Belagerungsbrecher: bleib in Bewegung | Er streift umher, feuert eine gerade [Rivet-Rakete](/wiki/06-Items/Rockets.md#the-twelve-rockets) auf den Piloten, der ihn zuerst getroffen hat, und repariert sich selbst. Zwei **Siege Escorts** feuern zusätzlich Laser. Bleib in Bewegung und wechselt euch als Ziel ab. |
| **Wrath Warden** | 3, 6, 9, 12 … | Kriegsherr: schlage die Raserei | Er kämpft auf der Stelle und repariert sich selbst. Unter halber Hülle treffen seine Laser **anderthalbmal so hart**. Zwei **Wrath Guards** feuern zusätzlich Laser. Bring ihn schnell herunter und halte die Schilde oben. |

### Einen Wächter rufen {#calling-a-warden}

- **Wann.** Nachdem Schritt 4 erledigt ist. Ein Clan hat **zwei Rufe pro Tag**, es ist immer nur ein Wächter gleichzeitig draußen, und vom Tag müssen noch **mindestens 30 Minuten** übrig sein.
- **Wer.** Der Anführer oder ein Stellvertreter.
- **Wie.** Im Flug: Der Knopf **Hier rufen** erscheint auf dem Flugbildschirm, sobald Schritt 4 erledigt ist, und lässt dich bestätigen. Sei außerhalb der Schutzzonen, in einem Konzernsektor **x-2, x-3 oder x-4** (eines beliebigen Konzerns) deiner Welt. Der Reiter Einsätze zeigt den Wächter des Tages, die übrigen Rufe und warum der Knopf ausgegraut ist, aber ein Wächter wird vom Schiff aus gerufen.
- **Wo er erscheint.** 3.000 bis 4.500 Einheiten von deinem Schiff entfernt, in deiner Welt: Nur Piloten dieser Welt erreichen ihn. Der Reiter empfiehlt **x-2 für einen Rekruten-Clan, x-3 für Veteranen und x-4 für Elite**. Die üblichen [PvP-Regeln](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma) des gewählten Sektors gelten weiter.
- **Aufwärmen.** Er steht **90 Sekunden** lang abgeschirmt und passiv da („fährt hoch“), und jeder Clanpilot, der online ist, erfährt, wo. Flieg hin, während er hochfährt: Nach den 90 Sekunden ist er kampfbereit. Eine Kapsel unter der Schutzzonen-Anzeige auf dem Flugbildschirm begleitet ihn: sein Name, „fährt hoch“ mit der Restzeit, dann „kampfbereit“ mit seinem Sektor und der Zeit bis zum Rückzug, und „rasend“, sobald ein Wrath Warden unter der halben Hülle ist.
- **Nur dein Clan.** Die Schüsse von Piloten anderer Clans werden ignoriert und bringen ihn nicht dazu, zurückzuschießen.
- **Wie es endet.** Wenn er zerstört wird. Er **zieht sich zurück**, 40 Minuten nachdem er kampfbereit wurde, wenn der Tag endet, wenn kein Pilot deines Clans 2 Minuten lang in seinem Sektor im Flug war oder wenn der Server neu startet (dann wird der Ruf zurückgegeben). Ein Wächter, der sich zurückzieht, kostet einen Ruf, und der nächste Ruf ist derselbe Wächter mit voller Stärke.

### Einen Wächter bekämpfen {#fighting-a-warden}

- **Ein Wächter kämpft gegen den Piloten, der ihn zuerst getroffen hat**, wie jeder Boss: Lass das robusteste Schiff der Besatzung beginnen und nutze [Shield Surge und Emergency Repair](/wiki/03-Mechanics/Abilities.md).
- **Bring etwa sieben Piloten und x2-Munition mit** ([Laser](/wiki/06-Items/Lasers.md#laser-ammunition)). Fünf verlieren meistens, zehn gewinnen mühelos. Die Tabelle unten zeigt den besten Fall, und selbst in ihm verlieren drei gegen jeden Wächter, und vier gewinnen nur gegen die Siege Warden I und II. In der Tabelle hat die kleinste Besatzung, die gewinnen kann, 4 bis 5 Piloten mit x2-Munition und 6 bis 8 mit x1-Munition.
- **Brood:** Die Drohnen heilen seine Hülle, und eine Besatzung, die sie ignoriert, verliert: Fünf Piloten, die nur auf den Wächter schießen, fallen alle, wenn noch etwa die Hälfte von ihm steht, und zehn brauchen etwa ein Fünftel länger. Schieß sie zuerst ab: Eine stirbt unter dem Feuer von fünf Piloten in einer Sekunde oder weniger, und die nächste kommt nach 8 Sekunden.
- **Siege:** Seine Raketen fliegen gerade und ungelenkt, ein Schiff, das in Bewegung bleibt, weicht den meisten aus. Bleib in Bewegung und wechselt euch als Ziel ab.
- **Wrath:** Sobald seine Hülle unter der Hälfte liegt, trifft jede Salve anderthalbmal so hart, die zweite Hälfte des Kampfs ist also die gefährliche. Bring die erste Hälfte schnell herunter, halte die Schilde oben und spare Emergency Repair für die Raserei auf.

### Wie groß die Besatzung sein muss {#how-big-a-crew}

> [!NOTE]
> Diese Zeiten sind aus den Zahlen unten **berechnet**, nicht im Spiel gemessen. Die Besatzung fliegt in den Schiffen und der Ausrüstung, für die die Stufe gemacht ist, und die Tabelle zeigt ihren **besten Fall**: Jeder Pilot setzt Shield Surge und Emergency Repair ein, sobald sie bereit sind, und die Besatzung schießt zuerst auf die Helfer des Wächters, wenn das besser ist. Der Wächter und seine Helfer feuern alle auf den Piloten, der zuerst getroffen hat, und niemand weicht aus. **Ein echter Kampf ist härter als die Tabelle.** Die Zeile mit fünf Piloten ist selbst im besten Fall knapp (ein Sieg, der ein oder zwei Schiffe kostet), und in denselben Kämpfen, die wir im Spiel selbst mit skriptgesteuerten Piloten ausgetragen haben, verloren fünf Piloten die meisten, auch wenn sie beide Fähigkeiten einsetzten; sieben gewannen jeden ihrer Kämpfe, und zehn gewannen mühelos. Eine Besatzung aus fünf Piloten, die keine Fähigkeit einsetzt und nur auf den Wächter schießt, verliert gegen sieben der neun Wächter; sieben Piloten, die dasselbe tun, gewinnen gegen acht von ihnen (alle außer dem Brood Warden III, dessen Drohnen ihn heilen) und verlieren ein bis drei Schiffe, und zehn gewinnen gegen alle neun.

Die Tabelle zeigt den besten Fall mit x2-Munition; im Spiel verlieren fünf Piloten meistens, und etwa sieben gewinnen.

| Besatzung | Mit x2-Munition | Mit x1-Munition |
| :--- | :--- | :--- |
| 3 Piloten | verlieren gegen jeden Wächter, nach 4,7 bis 13,8 Minuten; der Wächter behält zwischen einem Viertel und zwei Dritteln seiner Hülle und seines Schilds | verlieren |
| 4 Piloten | gewinnen nur gegen die Siege Warden I und II, in etwa 8 Minuten, und verlieren 1 Schiff | verlieren |
| 5 Piloten | gewinnen gegen jeden Wächter in 5,3 bis 6,5 Minuten und verlieren 1 bis 2 Schiffe | verlieren |
| 7 Piloten | gewinnen gegen jeden Wächter in 3,3 bis 3,6 Minuten und verlieren 0 bis 1 Schiffe | gewinnen gegen jeden Wächter außer den Brood Warden II und III, in 8,7 bis 12,3 Minuten, und verlieren 1 bis 4 Schiffe |
| 10 Piloten | gewinnen gegen jeden Wächter in 2,2 bis 2,4 Minuten und verlieren 0 bis 1 Schiffe | gewinnen gegen jeden Wächter in 5,1 bis 5,6 Minuten und verlieren 1 bis 2 Schiffe |

Im besten Fall hat die kleinste Besatzung, die mit x2-Munition gewinnt, **4 Piloten** (gegen die Siege Warden I und II) bis **5** (gegen die anderen sieben) und verliert dabei **1 bis 2** Schiffe; mit x1-Munition hat sie **6 bis 8** Piloten und verliert 2 bis 4. Eine Besatzung von **sieben** gewinnt mit x2-Munition gegen jeden Wächter und verliert im besten Fall höchstens ein Schiff. Die Laser eines Wächters treffen in Stärke I mit einigen Dutzend bis über hundert pro Salve (48 bis 129) und in Stärke III mit Tausenden (1.845 bis 3.090), und seine Helfer kommen dazu: Das Schiff, gegen das er kämpft, fällt in anderthalb bis vier Minuten, dann wendet er sich dem nächsten zu, und so verliert selbst eine Besatzung, die gewinnt, Schiffe.

Die Tabelle gilt für eine Besatzung in der Ausrüstung der eigenen Stufe des Wächters. Schwächere Schiffe schneiden schlechter ab: Zehn Piloten in Rekruten-Ausrüstung können keinen Veteranen-Wächter töten, und zehn in Veteranen-Ausrüstung keinen Elite-Wächter. Der Wächter **deines** Clans passt immer zu **deiner** Stufe, die die fünf besten Piloten des Clans bestimmen, bring sie also mit.

**Ein Clan, der für seinen Wächter zu klein ist,** ist nicht ausgesperrt (weniger als etwa sieben Piloten am Tag). Die vier Missionen zahlen ihre **70 Punkte**, was auch mit dem Wächter geschieht, die Punkte kaufen Boni, und der Clan kann den Wächter erneut rufen, wenn er noch einen Ruf übrig hat (es sind zwei pro Tag): Fällt die Besatzung und bleibt weg, zieht sich der Wächter zurück, das kostet einen Ruf, und der nächste Ruf bringt ihn mit voller Stärke zurück. Aber die Linie ist nicht abgeschlossen, also bekommt niemand die [Belohnung für dich](#the-reward-for-you), und ein Clan, der seinen Wächter nie besiegt, hat alle 30 Bonusstufen frühestens am Saisontag 18 statt am Tag 12 ([wie lange es dauert](#how-long-it-takes)).

### Die Zahlen der Wächter {#warden-numbers}

Die Wächter haben in jeder Welt dieselben Zahlen (die Alpha-Zahlen), ebenso ihre Bezahlung. Jede Drohne, jeder Begleiter und jede Wache hat die Zahlen der zweiten Tabelle, und sie stehen beim Wächter: Eine Brood Drone heilt die Hülle des Wächters, eine Siege Escort oder eine Wrath Guard feuert Laser. Eine Salve sind die Schüsse aller Laser eines Schiffs in einer Sekunde, ausgewürfelt zwischen 80 und 100 % der angezeigten Zahl; ein Wrath Warden mit weniger als der halben Hülle trifft anderthalbmal so hart. Der Wächter und seine Helfer feuern alle auf den Piloten, gegen den der Wächter kämpft, ihre Salven addieren sich also: Ein Brood Warden III mit seinen vier Drohnen legt bis zu 4.350 pro Sekunde auf ein Schiff. Die [Rivet-Rakete](/wiki/06-Items/Rockets.md#the-twelve-rockets) des Siege Warden wird nicht ausgewürfelt: Sie trifft mit höchstens **2.500** in Stärke I, **5.000** in Stärke II und **7.500** in Stärke III, während die Rivet eines Piloten zwischen einer kleinsten und einer größten Zahl gewürfelt wird. Sie fliegt geradeaus, ein Schiff, das in Bewegung bleibt, wird also verfehlt.

| Wächter | Hülle | Schild | Laserschaden (eine Salve pro Sekunde) | Tempo | Laserreichweite | Repariert sich selbst (Hülle pro Sekunde) | Rakete und Sekunden zwischen den Schüssen |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Brood Warden I | 166.000 | 136.000 | 129 | 90 | 600 | – | – |
| Brood Warden II | 288.000 | 236.000 | 777 | 90 | 700 | – | – |
| Brood Warden III | 1.060.000 | 870.000 | 3.090 | 90 | 800 | – | – |
| Siege Warden I | 143.000 | 117.000 | 48 | 110 | 600 | 215 | Rivet I: 24 |
| Siege Warden II | 248.000 | 203.000 | 291 | 110 | 700 | 375 | Rivet II: 12 |
| Siege Warden III | 915.000 | 745.000 | 1.845 | 110 | 800 | 1.385 | Rivet III: 8 |
| Wrath Warden I | 163.000 | 133.000 | 96 | 90 | 700 | 215 | – |
| Wrath Warden II | 282.000 | 231.000 | 582 | 90 | 800 | 375 | – |
| Wrath Warden III | 1.040.000 | 850.000 | 2.460 | 90 | 900 | 1.385 | – |

| Helfer | Anzahl | Hülle | Schild | Laserschaden (eine Salve pro Sekunde) | Tempo | Heilt den Wächter (Hülle pro Sekunde) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Brood Drone I | 4 | 700 | 500 | 12 | 170 | 120 |
| Brood Drone II | 4 | 1.200 | 900 | 78 | 170 | 210 |
| Brood Drone III | 4 | 4.000 | 3.500 | 315 | 170 | 770 |
| Siege Escort I | 2 | 4.300 | 3.500 | 6 | 175 | – |
| Siege Escort II | 2 | 7.400 | 6.100 | 45 | 175 | – |
| Siege Escort III | 2 | 27.500 | 22.500 | 285 | 175 | – |
| Wrath Guard I | 2 | 4.900 | 4.000 | 18 | 180 | – |
| Wrath Guard II | 2 | 8.500 | 6.900 | 117 | 180 | – |
| Wrath Guard III | 2 | 31.000 | 25.500 | 495 | 180 | – |

### Bezahlung und Beute {#warden-pay-and-loot}

Ein Wächter zahlt so viel wie ein Stapel des schweren Aliens der Stufe: **30 Phantasms** für einen Wächter I, **24 Bulwarks** für einen II und **16 Goombahs** für einen III. Es ist ein Topf, aufgeteilt nach Schaden unter den Piloten, die mindestens 5 % des Schadens verursacht haben, genauso wie beim Anführer eines [Schwarms](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays). Deine [Clan-Boni](#what-the-boosts-apply-to) gelten für deinen Anteil. Nach unserer Rechnung decken die Credits ungefähr die x1-Munition, die die kleinste Besatzung verbrennt, die gewinnen kann, und x2-Munition kostet mehr Thulium, als der Wächter zahlt: Es ist ein Kampf um die Punkte und die Kiste. Die Bezahlung hat sich in 0.4.12 nicht geändert, als die Laser der Wächter stärker wurden: Der Topf wächst nicht mit dem Schaden, den du einsteckst, oder den Schiffen, die du verlierst.

| Stärke des Wächters | Credits | Thulium | Erfahrung (EP) | Ehre |
| :--- | ---: | ---: | ---: | ---: |
| I | 90.000 | 360 | 9.000 | 180 |
| II | 120.000 | 600 | 19.200 | 240 |
| III | 240.000 | 1.200 | 48.000 | 384 |

Der Wächter lässt **eine Kiste** für den Piloten fallen, der den meisten Schaden verursacht hat; sie gehört 30 Sekunden lang ihm und seinem Clan ([Frachtkisten](/wiki/03-Mechanics/Cargo.md)). Eine Chance in Klammern gilt für jeden der genannten Würfe: (5 × 50 %) sind fünf Würfe mit je 50 % Chance.

| Wächter | Gegenstand | I | II | III |
| :--- | :--- | :---: | :---: | :---: |
| Brood Warden | Ship Fragment | 3–5 | 8–12 | 15–25 |
| Brood Warden | Advanced Plasma | 100–200 | 300–600 | – |
| Brood Warden | Daraxium | 1–2 (5 × 50 %) | – | – |
| Brood Warden | Nyxite | – | 2–4 (5 × 50 %) | – |
| Brood Warden | Ultra Core | – | – | 300–500 |
| Brood Warden | Quorvium | – | – | 5–10 (60 %) |
| Siege Warden | Ship Fragment | 2–4 | 6–10 | 12–20 |
| Siege Warden | Siphon Battery | 100–200 | 300–500 | 800–1.200 |
| Siege Warden | Rakete aus dem Credits-Shop (eine Sorte, zufällig) | 2–3 | 5–8 | 8–12 |
| Siege Warden | Reinforced Hull Plate | – | 1 (30 %) | – |
| Siege Warden | Epische Rakete (eine Sorte, zufällig) | – | – | 1–2 (50 %) |
| Wrath Warden | Ship Fragment | 4–6 | 8–12 | – |
| Wrath Warden | Cataclysite | 3–5 | 5–10 | – |
| Wrath Warden | Reinforced Hull Plate | 1 (25 %) | 1 (50 %) | 1–2 (70 %) |
| Wrath Warden | Power Core | – | 1 (15 %) | 1 (35 %) |
| Wrath Warden | Quorvium | – | – | 5–10 (70 %) |
| Wrath Warden | Ancient Control Unit | – | – | 1 (8 %) |

Ein Wächter zählt in deiner Abschussstatistik unter seinem eigenen Namen und bringt deinem [Rang](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) PvE-Punkte: **13 bis 35** für den Anführer, je nach Wächter und Stärke (ein Wächter III bringt am meisten), und **1 bis 6** für jeden Helfer, mehr für eine stärkere Besatzung.

---

## Clanpunkte und Boni {#clan-points-and-boosts}

Clanpunkte gehören dem Clan. Jeder Schritt, den der Clan abschließt, erhöht sein Guthaben. Der **Anführer und die Stellvertreter** geben es auf der Karte **Flottenboni** im Reiter Einsätze aus: drei Boni mit je zehn Stufen, und jedes Mitglied hat sie sofort. Ein Kauf ist endgültig: Es gibt keine Rückerstattung und keine Umverteilung.

### Die drei Boni {#the-three-boosts}

| Bonus | Stufen | Pro Stufe | Höchste Stufe | Wirkt auf |
| :--- | :---: | :---: | :---: | :--- |
| **Flotten-Schaden** | 10 | +0,5 % | +5 % | Laserschaden gegen Aliens und Piloten |
| **Flotten-Thulium** | 10 | +1 % | +10 % | Thulium aus Abschüssen und Missionsbelohnungen |
| **Flotten-Credits** | 10 | +1 % | +10 % | Credits aus Abschüssen und Missionsbelohnungen |

**Wo du sie siehst.** Im Flug zeigt das **Booster-Fenster** die Boni, die dein Schiff hat, auf einer eigenen Karte **Flottenboni** unter den zeitlich begrenzten Boostern: das Tag deines Clans, dann eine Zeile pro Bonus mit seinem Wert und seiner Stufe (Stufe 3/10). Sie haben keinen Timer, denn ein Clanbonus gilt, solange du im Clan bist. Fahr mit der Maus über eine Zeile, um zu sehen, worauf sie wirkt. Ein Clan, der noch nichts gekauft hat, zeigt „Deine Flotte hat noch keine Boni“, und ein Pilot ohne Clan sieht keine Karte. Die Booster-Karte des **Dashboards** und das Profil eines Piloten listen sie ebenfalls. Die Karte zeigt, was dein Schiff anwendet, so wie der Server es dem Spiel mitteilt, eine Stufe, die die Offiziere gerade gekauft haben, erscheint also sofort. Ein Spiel vor 0.4.12 wendet die Boni an und zeigt keine Karte.

### Preise {#boost-prices}

Der Preis einer Stufe ist **22 Clanpunkte plus 4 für jede Stufe davor**, und er ist für alle drei Boni gleich: 400 Punkte für einen Bonus, **1.200 für alle drei**, das sind zwölf abgeschlossene Linien.

| Stufe | Preis | Summe für diesen Bonus | Flotten-Schaden | Flotten-Thulium | Flotten-Credits |
| :---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 22 | 22 | +0,5 % | +1 % | +1 % |
| 2 | 26 | 48 | +1 % | +2 % | +2 % |
| 3 | 30 | 78 | +1,5 % | +3 % | +3 % |
| 4 | 34 | 112 | +2 % | +4 % | +4 % |
| 5 | 38 | 150 | +2,5 % | +5 % | +5 % |
| 6 | 42 | 192 | +3 % | +6 % | +6 % |
| 7 | 46 | 238 | +3,5 % | +7 % | +7 % |
| 8 | 50 | 288 | +4 % | +8 % | +8 % |
| 9 | 54 | 342 | +4,5 % | +9 % | +9 % |
| 10 | 58 | 400 | +5 % | +10 % | +10 % |

### Worauf die Boni wirken {#what-the-boosts-apply-to}

- **Flotten-Schaden** erhöht den gesamten Laserschaden deines Schiffs: gegen Aliens, Schwarmschiffe, Wächter und andere Piloten. Er wirkt **nicht auf Raketen**, auf keine Art.
- **Flotten-Thulium und Flotten-Credits** erhöhen die Bezahlung von Alien-Abschüssen (deine eigenen, dein Anteil an einem Boss und dein Anteil an einem Gruppenabschuss) und die Belohnung jeder Mission, die du einlöst, ob Level-, Station- oder Herausforderungs-Mission ([Quests](/wiki/03-Mechanics/Quests.md#rewards)). Sie wirken **nicht auf** die Farmen des [Skylab](/wiki/03-Mechanics/Skylab.md#credit-farm-and-thulium-farm), Bankauszahlungen, Bonuscodes oder die Belohnung der Tageslinie.
- **Sie addieren sich zu deinen anderen Boni** (Booster wie der Laser Damage Booster, die Boni des [Saison-Shops](/wiki/03-Mechanics/Wipe-Timeline.md#the-permanent-buff-store)): Die Prozente werden addiert. Laserverstärker (Amps) gehören nicht dazu: Sie addieren festen Schaden, und die Prozente gelten für die Summe. Fünf Punkte Flotten-Schaden neben 50 aus anderen Quellen ergeben 55, das sind 3,3 % mehr Schaden als vorher.
- **Ein Bruchteil geht nicht verloren.** Ein Bonus bringt einem Abschuss oft weniger als eine Einheit: 10 % von 4 Thulium eines Seekers sind 0,4. Das Spiel merkt sich den Bruchteil und zahlt ihn mit den Einheiten deiner nächsten Abschüsse aus, sodass zehn Seeker die 4 zahlen, die dir zustehen. Der Bruchteil, den du gerade hältst, verfällt, wenn du dich abmeldest.
- **Beitreten und Austreten.** Ein Pilot hat die Boni ab dem Moment, in dem er dem Clan beitritt, und verliert sie in dem Moment, in dem er austritt, rausgeworfen wird oder der Clan aufgelöst wird. Der Clan behält seine Stufen.

### Wie lange es dauert {#how-long-it-takes}

Ein Clan, der jede Linie schafft, verdient 100 Punkte pro Tag. Wenn die Offiziere gleichmäßig auf die drei Boni verteilt kaufen, hat er **4 Stufen nach der ersten Linie, 10 nach der dritten, 16 nach der fünften und alle 30 am Saisontag 12**. Vierzehn Linien sind vorbei, wenn Tag 15 beginnt, ein solcher Clan hat also zwei Linien Spielraum. Ein Tag, der nicht fertig wird, zahlt trotzdem für die erledigten Schritte: Ein Clan, der die vier Missionen schafft, seinen Wächter aber nie besiegt, verdient 70 Punkte pro Tag und hat alle 30 Stufen frühestens am Saisontag 18. Nach der letzten Stufe läuft die Linie weiter und zahlt weiter deine Belohnung; die Punkte zählen weiter in das, was der Clan in dieser Saison verdient hat, das der Hover-Tooltip der Clanpunkte auf der Karte Flottenboni zeigt.

### Punkte und der Wipe {#clan-points-and-the-wipe}

Bei jedem Wipe beginnen **Punkte, Boni-Stufen und Linien des Clans von vorn**, jede Saison ist also ein neues Rennen um volle Boni. Der Clan selbst, seine Mitglieder, seine Bank und seine Steuer bleiben, wie sie sind.

---

## Diplomatie {#diplomacy}

Clans können formelle diplomatische Beziehungen zu anderen Organisationen aufnehmen, indem sie das Kürzel des Zielclans eingeben:

- **Allianz**: Formell verbündete Clans. Der freundliche Status wird auf der Karte angezeigt.
- **NAP (Nichtangriffspakt)**: Die Vereinbarung, keine Feindseligkeiten aufzunehmen.
- **Krieg**: Förmliche Kriegserklärung. Kriegsziele können überall ohne Strafe angegriffen werden.

---

## Einen Freund mitbringen {#bringing-a-friend}

Ein Freund, der neu im Spiel ist, kann mit deinem persönlichen Einladungscode beitreten und bekommt ein Startpaket; siehe [Freunde einladen](/wiki/03-Mechanics/Invite-Friends.md). Sobald er im Spiel ist, kann er sich wie jeder Pilot bei deinem Clan bewerben.
