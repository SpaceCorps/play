<!-- wiki-i18n source: 431a488ba7a0842e -->
<!-- wiki-i18n title: Tempo -->
# Tempoberechnung {#speed-calculation}

Das Tempo bestimmt, wie schnell sich dein Schiff auf der Weltraumkarte bewegt, damit du Ziele verfolgen, Gefechten entkommen oder Zonen durchqueren kannst.

## Die Tempoformel {#the-speed-formula}

Das endgültige Tempo deines Schiffs wird auf dem Server mit der folgenden Formel berechnet:

\[\text{Endgültiges Tempo} = (\text{Grundtempo des Schiffs} + \text{Gesamttempo der Triebwerke}) \times (1,0 + \text{Gesamter Tempobonus in Prozent})\]

### 1. Effektives Triebwerkstempo {#1-effective-engine-speed}

Jedes ausgerüstete Triebwerk erzeugt Tempo. Stecken Schubdüsen im Triebwerk, wird sein Tempo verändert:

\[\text{Triebwerkstempo} = (\text{Grundtempo des Triebwerks} \times \text{Schubdüsen-Faktor}) + \text{Fester Schubdüsen-Bonus}\]

- **Schubdüsen-Faktor**: Das Produkt aller Tempo-Faktoren der Schubdüsen, die in diesem Triebwerk stecken (z. B. ist Thruster III `1.1` oder `+10%`).
- **Fester Schubdüsen-Bonus**: Die Summe aller festen Tempozuschläge durch Schubdüsen (z. B. ist Thruster III `+15` Tempo).

### 2. Abnehmender Ertrag (Grenzeffizienz) {#2-diminishing-returns-marginal-efficiency-}

Damit Spieler nicht unendlich viele Triebwerke für unendliches Tempo stapeln, gilt eine Kurve des **abnehmenden Ertrags (der Grenzeffizienz)**. Alle Triebwerke werden nach ihrem Tempobeitrag sortiert und der Reihe nach verarbeitet. Adaptive Kerne (Hybride) und Schildkerne werden genauso gereiht, jede Art in einer eigenen Gruppe, sodass ein Schiff mit Triebwerken und mit adaptiven Kernen in jeder Gruppe eigene Plätze 1 bis 4 hat:

| Triebwerksrang | Effizienzfaktor |
| :---: | :--- |
| **1. bis 4.** | **100 %** (1,0) |
| **5.** | **85 %** (0,85) |
| **6.** | **70 %** (0,70) |
| **7.** | **55 %** (0,55) |
| **Ab dem 8.** | **25 %** (0,25) |

Außerdem wird das Triebwerkstempo mit dem Wirkungsgrad seines Slots multipliziert (Kern: 100 %, Support: 75 %, Hilfs: 50 %).

### 3. Tempobonus in Prozent & Schildabzüge {#3-speed-bonus-percent-shield-penalties}

Der gesamte Tempobonus in Prozent ist die Summe aller Tempoboni der ausgerüsteten Triebwerke (und Hybride) abzüglich der Abzüge durch ausgerüstete Schilde:

- **Tempobonus der Triebwerke**: Triebwerke fügen positive Tempoprozente hinzu (z. B. fügt Engine III `+5%` hinzu).
- **Tempoabzug durch Schilde**: Schwere Schilde belasten dein Schiff und fügen negative Tempoprozente hinzu (z. B. fügt Heavy Shield Core `-5%` Tempo hinzu).
- **Slot-Skalierung**: Auch diese prozentualen Boni und Abzüge werden mit dem Wirkungsgrad des Slots skaliert, in dem der Gegenstand ausgerüstet ist. Ein Schild auf einer deiner Drohnen bremst dich genauso wie ein Schild in einem Kern-Slot.
- **Nie unter null**: Egal, wie viele Schilde du trägst, dein Tempo sinkt nicht unter 0.
