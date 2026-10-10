<!-- wiki-i18n source: 0f0413a5a5f080ae -->
<!-- wiki-i18n title: Schilde -->
# Schildmechanik {#shield-mechanics}

Schilde absorbieren den Großteil des eingehenden Schadens und schützen die Hülle deines Schiffs vor direktem Schaden.

## Schildberechnungen {#shield-calculations}

Die endgültigen Schildwerte deines Schiffs werden so berechnet:

\[\text{Endgültige Schildkapazität} = \text{Gesamte Grundkapazität} \times (1,0 + \text{Gesamter Schildbonus in Prozent})\]
\[\text{Endgültige Schildaufladerate} = \text{Gesamte Grundaufladung} \times (1,0 + \text{Gesamter Schildbonus in Prozent})\]

### 1. Slot-Wirkungsgrad & abnehmender Ertrag {#1-slot-efficiency-diminishing-returns}

Ähnlich wie bei Triebwerken werden ausgerüstete Schilde (und Hybridgeneratoren) mit den besten zuerst gereiht und dem Wirkungsgrad ihres Slots (Kern: 100 %, Support: 75 %, Hilfs: 50 %, der Slot einer Drohne: 100 %, wie ein Kern-Slot) sowie einer Kurve des abnehmenden Ertrags nach ihrem Rang unterworfen. Ein Schild wird nach dem gereiht, was von ihm zählt: seine Kapazität mal der Anteil seines Slots. Die Aufladung hat ihre eigene Reihenfolge (ihr Wert mal der Anteil des Slots), und die **vier besten** Schildboni zählen. Ein Schild auf einer deiner [Drohnen](/wiki/03-Mechanics/Drones.md) wird mit den eigenen Schilden des Schiffs eingereiht:

- **1. bis 4. Schild**: **100 %** (1,0) Grenzeffizienz.
- **5. Schild**: **85 %** (0,85) Grenzeffizienz.
- **6. Schild**: **70 %** (0,70) Grenzeffizienz.
- **7. Schild**: **55 %** (0,55) Grenzeffizienz.
- **Ab dem 8. Schild**: **50 %** (0,50) Grenzeffizienz. (Bis Version 0.4.7 waren es 25 %, wie bei den Triebwerken; Triebwerke behalten 25 %, siehe [Tempo](/wiki/03-Mechanics/Speed.md).)

**Mehr Ausrüstung senkt deinen Schild nie.** Ein Schild oder eine Schildzelle, die du hinzufügst, senkt nie deine Schildkapazität oder deine Aufladung: Jede Zahl wird mit dem Besten zuerst gereiht, nach dem, was zählt, also nimmt ein neues Teil den Platz ein, den es verdient. Die Absorption ist der Durchschnitt deiner Schilde, daher senkt sie ein neuer Schild, der schwächer ist als dein Durchschnitt; eine Zelle nie.

**Der Hangar zeigt es.** Ein Schild, ein Triebwerk oder ein Adaptiver Kern, der nicht mit seiner vollen Stärke zählt, trägt auf seinem Slot eine kleine Prozentangabe (zum Beispiel `64%`: das 5. Schild mit 85 % in einem Support-Slot mit 75 %); beim Darüberfahren siehst du die Aufschlüsselung. Fährst du über die Kacheln Schilde und Tempo der Kampfwerte, siehst du deine Gegenstände nach Rang und was ein weiterer zählen würde. Das Fenster Schiff im Flug zeigt dieselben Listen, wenn du über seine Schildleiste und das Tempo fährst.

### 2. Schildabsorption (Schadensaufteilung) {#2-shield-absorbance-damage-split-}

Absorption ist der Anteil jedes Treffers, den deine Schilde nehmen; der Rest geht direkt an die Trefferpunkte (HP).
- **Pro Schild**: die Absorption eines Schilds plus die Absorption der Schildzellen, die darin eingesetzt sind. Ein Schild allein hat **45 bis 50 %** (Light 45 %, Basic 48 %, Heavy 50 %); Zellen fügen je 2 bis 10 Punkte hinzu (Capacity Shield Cell I bis IV +2 %, +3 %, +4 %, +5 %; Absorption Shield Cell I bis IV +4 %, +6 %, +8 %, +10 %).
- **Durchschnittliche Absorption**: Die Absorption deines Schiffs ist der einfache Durchschnitt über die Schilde in Kern-, Support- und Hilfs-Slots und auf deinen Drohnen. Adaptive Kerne haben keine eigene Absorption und zählen im Durchschnitt nicht mit (Zellen in einem adaptiven Kern fügen nur Kapazität und Aufladung hinzu). Ohne ausgerüsteten Schild liegt deine Absorption bei 0 %: Die Hülle nimmt jeden Treffer, und die Schildpunkte aus Zellen in einem adaptiven Kern bleiben ungenutzt, rüste also nebenbei einen Schild aus.
- **Ab Werk sind höchstens 80 % möglich**: der beste Schild mit den besten Zellen, ein Heavy Shield Core mit drei Absorption Shield Cell IV in jedem Slot. Schwächere Schilde dazwischen senken den Durchschnitt. Weder ein Buff aus dem Saison-Shop noch ein Schmiede-Buff ist Teil dieser Zahl.
- **Beispiel**: Ein Basic Shield Core (48 %) mit zwei Absorption Shield Cell I ergibt 56 %; kommt ein Light Shield Core (45 %) hinzu, liegt der Durchschnitt bei 50,5 %.
- **Der Wert ist nicht auf 100 % begrenzt.** Er gibt an, was die Schilde von einem Treffer nehmen würden, bevor die *Schilddurchdringung* des Angreifers abgezogen wird, ein Schiff kann also mehr als einen ganzen Treffer tragen: 112 % nehmen immer noch einen ganzen Treffer von einem Angreifer mit bis zu 12 % Durchdringung.

#### Schilddurchdringung {#shield-penetration}

Manche Angriffe haben eine **Schilddurchdringung**: Punkte, die für diesen Treffer von deiner Absorption abgezogen werden. Der Anteil, den deine Schilde nehmen, ist

\[\text{Schildanteil} = \text{Begrenzen}(\text{Absorption} - \text{Durchdringung};\ 0;\ 100\%)\]

- Die Schilde nehmen höchstens `round(damage x share)` des Treffers; die Hülle nimmt den Rest. Ein Schild, der für seinen Anteil zu niedrig ist, gibt die Differenz an die HP weiter, und stehen die Schilde auf 0, trifft der gesamte Schaden direkt die HP.
- **Woher die Durchdringung kommt**: die *Schilddurchdringung* einer direkten Rakete (Lancet I 10 %, Lancet II 25 %, Lancet III 35 %, Rivet I 5 %, Rivet II 25 %, Rivet III 35 %, N.I.K.E. 35 %; Flächenschaden hat keine, siehe [Raketen](/wiki/06-Items/Rockets.md)) und die der Lasermunition (Ultra Core 5 %, Experimental Fusion Core 10 %; siehe [Laser & Munition](/wiki/06-Items/Lasers.md)). Aliens haben keine, ebenso wenig die Munition x1 und x2. Ein Lasertreffer nimmt außerdem die Penetration Amps der Laser des Schützen (+3 % bis +12 % pro Slot, der Mittelwert über seine Laser) und die Durchdringung einer Drohnenformation (Gemini +9 %, Stiletto +16 %); eine direkte Rakete addiert die der Formation zu ihrer eigenen. **Nichts begrenzt die Summe**: Die Schilde fangen die Absorption abzüglich all dessen ab, bis hinunter zu nichts vom Treffer ([so setzt sich ein Lasertreffer zusammen](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).
- **Beispiele**: 80 % Absorption gegen eine Lancet III (35 %): Die Schilde nehmen 45 % des Treffers, die Hülle 55 %. 100 % dagegen: 65 % und 35 %. 112 % gegen 12 % Durchdringung: der ganze Treffer. 45 % (ein Light Shield Core allein) gegen 35 %: 10 % auf den Schild, der Rest auf die Hülle. Eine Rakete allein durchdringt keinen Kern vollständig, aber eine Lancet III mit einer Stiletto (35 % + 16 % = 51 %) lässt einem Light Shield Core allein (45 %) nichts vom Treffer, und der beste Laser (62 %) ebenso: Gegen diesen Laser nimmt der beste Schild (80 %) 18 % des Treffers und die Hülle 82 %.
- Aliens haben keinen Absorptionswert: Sie teilen jeden Treffer 80 % / 20 % auf, abzüglich der Durchdringung des Treffers.
- Der Schaden einer Siphon Battery geht allein vom Schild ab: Absorption und Durchdringung spielen dabei keine Rolle.

**Wo die Schilde nichts nehmen.** Eine Durchdringung in Höhe der Absorption oder darüber lässt den Schilden nichts vom Treffer: Die Hülle nimmt alles. Die Tabelle zeigt, was die Schilde von einem Treffer des besten Lasers (62 %) und der besten direkten Rakete (eine Lancet III oder eine Rivet III mit einer Stiletto, 51 %) nehmen:

| Schild | Absorption | Schilde nehmen, bester Laser (62 %) | Schilde nehmen, beste direkte Rakete (51 %) |
| :--- | ---: | ---: | ---: |
| Light Shield Core | 45 % | 0 % | 0 % |
| Basic Shield Core | 48 % | 0 % | 0 % |
| Heavy Shield Core | 50 % | 0 % | 0 % |
| Der beste Schild ab Werk | 80 % | 18 % | 29 % |
| Ein Schild mit 100 % | 100 % | 38 % | 49 % |
| Ein Schild mit 120 % | 120 % | 58 % | 69 % |

#### 100 % erreichen und überschreiten {#reaching-and-passing-100-}

- **Ab Werk**: höchstens 80 % (siehe oben).
- **Schildabsorptions-Boost**: ein dauerhafter Buff aus dem Saison-Shop, mit Wipe-Punkten gekauft, **+0,1 Punkte pro Level, höchstens +10 Punkte** (100 Level, je 25 WP). Er fügt der Absorption deines Schiffs feste Punkte hinzu, auf jedem Schiff mit Schild gleich: 80 % werden mit 4 Leveln (100 WP) zu 80,4 %, und die 45 % eines Light Shield Core werden mit 12 Leveln (300 WP) zu 46,2 %. Ein Schiff ohne ausgerüsteten Schild bleibt bei 0 %. Die 100 Level kosten 2.500 WP, ein Ziel für mehrere Wipes: Die heutigen Quellen für Wipe-Punkte (die Abschuss-Meilensteine und die Missionen) zahlen an ihren Obergrenzen insgesamt 855 WP, über Wipes hinweg mitgenommen, und das kauft 34 Level, +3,4 Punkte. Weitere Quellen für Wipe-Punkte sind geplant. Siehe [Saison & Wipe-Punkte](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Schmiede**: Schilde und Schildzellen können einen **Absorptions**-Buff würfeln, der den Wert multipliziert: +5 % auf einen Schild mit 50 % sind +2,5 Punkte. Ein voll geschmiedetes bestes Set der Stufe Ewig (Kern und drei Zellen, jeder Buff am oberen Rand gewürfelt, +15 %) bringt bis zu 12 Punkte, im Durchschnitt etwa 10 (siehe [Die Schmiede](/wiki/06-Items/Forge.md)).
- **Zusammen**: 80 % ab Werk, +3,4 Punkte Buff (alle heutigen 855 Wipe-Punkte) und bis zu +12 Punkte aus Schmiede-Buffs ergeben heute höchstens **95,4 %**; mit allen 100 Leveln des Buffs (+10 Punkte, 2.500 WP) wären es 102 %. Weder der Buff noch die Schmiede allein erreicht 100 %; dorthin zu kommen ist ein Ziel für mehrere Wipes, und weitere Quellen für Wipe-Punkte sind geplant.

### Schild-Boosts: Kapazität, Absorption, Aufladung {#shield-boosts-capacity-absorbance-recharge}

Jeder Schild-Boost erhöht einen der drei Werte und steht im Fenster Booster unter seiner eigenen Art:

- **Kapazität** (maximale Schildpunkte): Shield Wall Booster I und II und der dauerhafte Schildkapazitäts-Boost.
- **Absorption** (der Anteil eines Treffers, den deine Schilde nehmen): der dauerhafte Schildabsorptions-Boost (+0,1 Punkte pro Level, höchstens +10 Punkte).
- **Aufladung** (pro Sekunde wiederhergestellte Schildpunkte): der Shield Regen Booster.

Die Zahlen stehen unter [Booster](/wiki/06-Items/Boosters.md).

---

## Passive Schildregeneration {#shield-passive-regeneration}

Schilde regenerieren sich mit der Zeit passiv, damit du kampfbereit bleibst.

- **Regenerationsschritt**: Liegen die Schilde unter der maximalen Kapazität, stellen sie pro Sekunde so viele Schildpunkte wieder her, wie deine Aufladerate beträgt.
- **Kampfunterbrechung (15 s Verzögerung)**: Die Regeneration endet, sobald du Schaden nimmst, und setzt erst nach **15 Sekunden** ohne Schaden wieder ein. Die Drohnenformationen Adamant und Redoubt ([Drohnenformationen](/wiki/03-Mechanics/Formations.md)) sind die Ausnahme: Sie geben jede Sekunde Schild zurück, auch im Kampf.
