<!-- wiki-i18n source: 21f10d185095b346 -->
<!-- wiki-i18n title: Clans -->
# Clans {#clans}

Einen Clan zu gründen oder ihm beizutreten, erlaubt es dir, Ressourcen zu bündeln, die gemeinsame Bank aufzuwerten, Steuersätze festzulegen, dich mit Fraktionsmitgliedern abzustimmen und Diplomatie zu betreiben.

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
| **Befördern / Entlassen** | ✅ | ✅* | ❌ | ❌ |
| **Bewerbungen annehmen** | ✅ | ✅ | ✅ | ❌ |

*\*Stellvertreter können nur Mitglieder mit einem niedrigeren Rang als ihrem eigenen befördern, degradieren oder entlassen.*

### Wenn der Anführer geht {#when-the-leader-leaves}

Ein Anführer kann einen Clan, der noch andere Mitglieder hat, nicht verlassen: Befördere zuerst einen Stellvertreter zum Anführer (der Anführer tritt zum Stellvertreter zurück) oder gehe als Letzter, wodurch der Clan aufgelöst wird. Löscht der Anführer sein Konto (Einstellungen › Konto), geht die Führung an das ranghöchste Mitglied, bei Gleichstand an das am längsten dienende; ein Anführer, der allein im Clan ist, löst ihn auf, samt Bank.

---

## Diplomatie {#diplomacy}

Clans können formelle diplomatische Beziehungen zu anderen Organisationen aufnehmen, indem sie das Kürzel des Zielclans eingeben:

- **Allianz**: Formell verbündete Clans. Der freundliche Status wird auf der Karte angezeigt.
- **NAP (Nichtangriffspakt)**: Die Vereinbarung, keine Feindseligkeiten aufzunehmen.
- **Krieg**: Förmliche Kriegserklärung. Kriegsziele können überall ohne Strafe angegriffen werden.

---

## Einen Freund mitbringen {#bringing-a-friend}

Ein Freund, der neu im Spiel ist, kann mit deinem persönlichen Einladungscode beitreten und bekommt ein Startpaket; siehe [Freunde einladen](/wiki/03-Mechanics/Invite-Friends.md). Sobald er im Spiel ist, kann er sich wie jeder Pilot bei deinem Clan bewerben.
