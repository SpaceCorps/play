<!-- wiki-i18n source: 24b93f5c13d7994f -->
<!-- wiki-i18n title: Potenciadores -->
# Potenciadores {#boosters}

Los potenciadores aplican modificaciones temporales de estadísticas que mejoran el combate, la defensa, la subida de nivel y la recolección de recursos de tu nave.

## Reglas de acumulación {#stacking-rules}

Los potenciadores usan un sistema de escalado aditivo:
1. **Los porcentajes de bono se suman**: si compras dos potenciadores distintos que dan +10 % de daño láser, recibirás un bono total de **+20 % de daño láser**.
2. **Las duraciones se acumulan de forma multiplicativa**: comprar varias veces el _mismo_ potenciador prolonga su duración activa. Los temporizadores de potenciadores _distintos_ corren en paralelo.
3. **Vista de temporizadores**: los potenciadores activos aparecen en el HUD, en la ventana Potenciadores, con el total de los bonos activos agrupados y el próximo vencimiento.

---

## Potenciadores activos {#active-boosters}

Todos los potenciadores duran **10 horas** de base y se activan en cuanto los compras o los recibes.

| Nombre | Rareza | Efecto base (10 horas) | Precio (Thulium) |
| :--- | :--- | :--- | :--- |
| **Damage Amp** | Raro | +10 % de daño láser | 20.000 |
| **Damage Amp II** | Raro | +10 % de daño láser | Solo botín o evento |
| **Shield Wall** | Raro | +25 % de capacidad de escudo (puntos de escudo máximos) | 15.000 |
| **Shield Wall II** | Raro | +25 % de capacidad de escudo (puntos de escudo máximos) | Solo botín o evento |
| **Hull Plating** | Raro | +10 % de puntos de vida máximos | 15.000 |
| **Hull Plating II** | Raro | +10 % de puntos de vida máximos | Solo botín o evento |
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
