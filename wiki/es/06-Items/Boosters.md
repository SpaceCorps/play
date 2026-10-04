<!-- wiki-i18n source: 539575474f5854de -->
<!-- wiki-i18n title: Potenciadores -->
# Potenciadores {#boosters}

Los potenciadores aplican modificaciones temporales de estadísticas que mejoran el combate, la defensa, la subida de nivel y la recolección de recursos de tu nave.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
Experience Kit | booster, common | buy 8000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Honor Beacon | booster, common | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp II | booster, rare | craft 20000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating II | booster, rare | craft 15000 Thulium, 60 s | research 10800 s, 10800 science | 5 Ship Fragment | /wiki/06-Items/Boosters.md#active-boosters
Shield Regen | booster, rare | buy 10000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Shield Wall | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Hull Plating | booster, rare | buy 15000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Resource Magnet | booster, rare | buy 18000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Damage Amp | booster, rare | buy 20000 Thulium | /wiki/06-Items/Boosters.md#active-boosters
Loot Luck | booster, legendary | buy 30000 Thulium | /wiki/06-Items/Boosters.md#active-boosters

Shield Wall -> Shield Wall II
Hull Plating -> Hull Plating II
Damage Amp -> Damage Amp II
```
<!-- item-tree:end -->

## Reglas de acumulación {#stacking-rules}

Los potenciadores usan un sistema de escalado aditivo:
1. **Los porcentajes de bono se suman**: si compras dos potenciadores distintos que dan +10 % de daño láser, recibirás un bono total de **+20 % de daño láser**.
2. **Las duraciones se acumulan de forma multiplicativa**: comprar varias veces el _mismo_ potenciador prolonga su duración activa. Los temporizadores de potenciadores _distintos_ corren en paralelo.
3. **Vista de temporizadores**: los potenciadores activos aparecen en el HUD, en la ventana Potenciadores, con el total de los bonos activos agrupados y el próximo vencimiento.

---

## Potenciadores activos {#active-boosters}

Todos los potenciadores duran **10 horas** de base y se activan en cuanto los compras, los recibes o los recoges. Los tres potenciadores **II** no se venden: investigas su tecnología en el Skylab ([Investigación](/wiki/03-Mechanics/Research.md)) y luego los fabricas en Ensamblaje, y al recoger uno empiezan sus 10 horas al instante, como al comprarlo.

| Nombre | Rareza | Efecto base (10 horas) | Precio (Thulium) |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | Raro | +10 % de daño láser | 20.000 |
| **Damage Amp II** | Raro | +10 % de daño láser | Ensamblaje: 20.000 |
| **Shield Wall** | Raro | +25 % de capacidad de escudo (puntos de escudo máximos) | 15.000 |
| **Shield Wall II** | Raro | +25 % de capacidad de escudo (puntos de escudo máximos) | Ensamblaje: 15.000 |
| **Hull Plating** | Raro | +10 % de puntos de vida máximos | 15.000 |
| **Hull Plating II** | Raro | +10 % de puntos de vida máximos | Ensamblaje: 15.000 |
| **Shield Regen** | Raro | +25 % de velocidad de recarga del escudo (puntos de escudo restaurados por segundo) | 10.000 |
| **Experience Kit** | Común | +20 % de experiencia ganada | 8000 |
| **Honor Beacon** | Común | +20 % de puntos de honor ganados | 10.000 |
| **Resource Magnet** | Raro | +25 % al contenido de las cajas de carga | 18.000 |
| **Loot Luck** | Legendario | +5 % de probabilidad de botín raro de los NPC | 30.000 |

---

## Aumentos de escudo: tres tipos {#shield-boosts-three-kinds}

Los escudos tienen tres estadísticas independientes, y cada aumento de escudo sube exactamente una de ellas. La ventana Potenciadores las mantiene separadas, con un icono y un total para cada una:

| Tipo | Qué es | Aumentos que la suben |
| :--- | :--- | :--- |
| **Capacidad de escudo** | Tus puntos de escudo máximos | Shield Wall, Shield Wall II, la **mejora permanente Shield Capacity Boost** (Tienda de temporada) |
| **Absorción de escudo** | La parte de cada impacto que se llevan tus escudos (el resto va al casco); puede superar el 100 % | La **mejora permanente Shield Absorbance Boost** (Tienda de temporada): +0,1 puntos por nivel por 25 PR, +10 puntos como máximo. Ningún potenciador la sube |
| **Recarga de escudo** | Puntos de escudo restaurados por segundo | Shield Regen. Ninguna mejora permanente la sube |

Los aumentos de un mismo tipo se suman; nunca cuentan para otro tipo. Las mejoras permanentes se describen en [Progreso entre temporadas](/wiki/03-Mechanics/Wipe-Timeline.md); las estadísticas en sí, en [Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md).
