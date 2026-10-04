<!-- wiki-i18n source: 0dfda8fd6d9be79d -->
<!-- wiki-i18n title: Drohnen -->
# Drohnen {#drones}

Drohnen sind kaufbare oder herstellbare Unterstützungseinheiten. Du kannst bis zu **8 Drohnen** gleichzeitig aktiv haben, Slave Drones und Master Drones zusammen.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Gegenstandsbaum {#item-tree}

Was die Montage herstellt, braucht zuerst seine Technologie; zeige auf einen Gegenstand, um zu sehen, wie lange die Forschung dauert. Der Technologiebaum, der Treibstoff und der Boost: [Forschung](/wiki/03-Mechanics/Research.md).

```tree
Slave Drone | drone, common | buy 100000 Credits | /wiki/06-Items/Drones.md#available-drones
Master Drone | drone, rare | craft 40000 Thulium, 60 s | research 36000 s, 36000 science | 1 Slave Drone, 100 Ship Fragment | /wiki/06-Items/Drones.md#available-drones

Slave Drone => Master Drone
```
<!-- item-tree:end -->

## Verfügbare Drohnen {#available-drones}

| Name             | Seltenheit | Slots | Beschreibung                                                                                  | Kosten                             |
| :--------------- | :--------- | :---- | :-------------------------------------------------------------------------------------------- | :--------------------------------- |
| **Slave Drone**  | Gewöhnlich | 1     | Eine einfache Drohne mit einem einzigen Ausrüstungs-Slot. Sie wächst durch 8 Level, während du Aliens zerstörst. | Ab 100.000 Credits (siehe unten) |
| **Master Drone** | Selten     | 2     | Eine in der Montage aufgerüstete Slave Drone. Sie fliegt in Gold, behält ihre Nummer und das, was sie trägt, bekommt einen zweiten Ausrüstungs-Slot und fängt wieder bei Level 1 an. | Eine Slave Drone aufrüsten: 40.000 Thulium und 100 Ship Fragments |

Eine Slave Drone beginnt als kleine Kugel und wächst auf Level 8 zu einem gepanzerten Kanonenboot heran. Jede Drohne, die du besitzt, bekommt dieselbe Erfahrung, sobald du ein Alien zerstörst, und ein höheres Level gibt dem Laser in ihrem Slot etwas mehr Schaden (bis zu +7 % auf Level 8). Die Seite zur Drohnenmechanik (unter Spielmechanik) nennt die Level und was jedes verlangt. Das Herstellen einer Master Drone verbraucht keine Drohne: Es rüstet die von dir gewählte Slave Drone an Ort und Stelle auf, und **ihr Level und ihre Erfahrung werden auf 0 zurückgesetzt**, wenn das Upgrade fertig ist (die Montage weist darauf hin und bittet dich um Bestätigung). Dafür hat die Drohne **zwei Ausrüstungs-Slots** statt einem: Was sie trug, bleibt in ihrem ersten Slot, der zweite ist leer. Deine Drohnen bleiben mit ihren Leveln und ihrer Erfahrung über den Saison-Wipe erhalten.

## Preise der Slave Drone {#slave-drone-prices}

Jede Slave Drone, die du kaufst, kostet mehr als die vorige. Der Preis hängt davon ab, wie viele Drohnen du beim Kauf besitzt (eine Master Drone zählt als eine), und der Shop zeigt immer den Preis deiner nächsten. Die ersten drei kosten nur Credits; ab der vierten kommt Thulium dazu.

| Drohne | Credits    | Thulium |
| :----- | :--------- | :------ |
| 1.     | 100.000    | –       |
| 2.     | 200.000    | –       |
| 3.     | 400.000    | –       |
| 4.     | 800.000    | 10.000  |
| 5.     | 1.600.000  | 20.000  |
| 6.     | 3.200.000  | 30.000  |
| 7.     | 6.400.000  | 40.000  |
| 8.     | 12.800.000 | 50.000  |

Alle acht zusammen kosten 25.500.000 Credits und 150.000 Thulium. Deine Drohnen bleiben über den Saison-Wipe erhalten, also läuft der Preis ab der Zahl weiter, die du besitzt: Mit drei Drohnen ist deine nächste immer die 4., und mit acht gibt es keine mehr zu kaufen.

## Verwendung {#usage}

1. **Kaufe** Slave Drones im Shop. Wenn du die goldene willst, **rüste** eine in der Montage zu einer Master Drone **auf** (ihr Level und ihre EP fangen dann von vorn an).
2. **Rüste** sie im Hangar auf dem Tab „Drohnen“ **aus**.
3. **Bestücke** sie mit Lasern oder Schilden, um deine Kampfkraft zu erhöhen: Eine Slave Drone hat einen Slot, eine Master Drone zwei. Ein Laser feuert mit deinem Schiff; ein Schild zählt wie einer in einem Kern-Slot, mit allen seinen Werten.
4. **Steigere** ihr Level, indem du Aliens zerstörst: Der Hangar zeigt das Level jeder Drohne und wie viel Erfahrung das nächste verlangt.
