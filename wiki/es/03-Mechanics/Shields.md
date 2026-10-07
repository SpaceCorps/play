<!-- wiki-i18n source: 7af844c9c2785078 -->
<!-- wiki-i18n title: Escudos -->
# Mecánicas de los escudos {#shield-mechanics}

Los escudos absorben la mayor parte del daño entrante y protegen el casco de tu nave del daño directo.

## Cálculos del escudo {#shield-calculations}

Los parámetros finales de escudo de tu nave se calculan así:

\[\text{Capacidad final del escudo} = \text{Capacidad base total} \times (1,0 + \text{Porcentaje total de bono de escudo})\]
\[\text{Velocidad final de recarga del escudo} = \text{Recarga base total} \times (1,0 + \text{Porcentaje total de bono de escudo})\]

### 1. Eficiencia de ranura y rendimientos decrecientes {#1-slot-efficiency-diminishing-returns}

Igual que con los motores, los escudos equipados (y los generadores híbridos) se ordenan del mejor al peor y se les aplica la eficiencia de ranura (principal: 100 %, apoyo: 75 %, auxiliar: 50 %, la ranura de un dron: 100 %, como una principal) y una curva de rendimientos decrecientes según su puesto. Un escudo se ordena por lo que cuenta de él: su capacidad por la parte de su ranura. La recarga tiene su propio orden (su valor por la parte de la ranura), y cuentan las **cuatro mejores** bonificaciones de escudo. Un escudo en uno de tus [drones](/wiki/03-Mechanics/Drones.md) se ordena junto con los de la propia nave:

- **Del 1.º al 4.º escudo**: **100 %** (1,0) de eficiencia marginal.
- **5.º escudo**: **85 %** (0,85) de eficiencia marginal.
- **6.º escudo**: **70 %** (0,70) de eficiencia marginal.
- **7.º escudo**: **55 %** (0,55) de eficiencia marginal.
- **8.º y siguientes**: **50 %** (0,50) de eficiencia marginal. (Hasta la versión 0.4.7 era el 25 %, igual que en los motores; los motores siguen en el 25 %, consulta [Velocidad](/wiki/03-Mechanics/Speed.md).)

**Poner más nunca baja tu escudo.** Añadir un escudo o una célula de escudo nunca baja tu capacidad de escudo ni tu recarga: cada cifra se ordena del mejor al peor según lo que cuenta, así que una pieza nueva ocupa el puesto que merece. La absorción es la media de tus escudos, así que la baja un escudo nuevo más débil que tu media; una célula, nunca.

**El hangar lo muestra.** Un escudo, un motor o un núcleo adaptativo que no cuenta con toda su fuerza lleva un pequeño porcentaje en su ranura (por ejemplo, `64%`: el 5.º escudo, al 85 %, en una ranura de apoyo, al 75 %), y al pasar el cursor por encima se ve el desglose. Pasa el cursor por las casillas Escudos y Velocidad de las estadísticas de combate para ver tus objetos por puesto y lo que contaría uno más. La ventana Nave en vuelo muestra las mismas listas al pasar el cursor por su barra de escudo y por la velocidad.

### 2. Absorción de escudo (reparto del daño) {#2-shield-absorbance-damage-split-}

La absorción es la parte de cada impacto que se llevan tus escudos; el resto va directamente a los puntos de vida (HP).
- **Por escudo**: la absorción de un escudo más la de las células de escudo instaladas en él. Un escudo solo tiene **del 45 al 50 %** (Light 45 %, Basic 48 %, Heavy 50 %); las células suman de 2 a 10 puntos cada una (Capacity Shield Cell I a IV +2 %, +3 %, +4 %, +5 %; Absorption Shield Cell I a IV +4 %, +6 %, +8 %, +10 %).
- **Absorción media**: la absorción de tu nave es la media simple de los escudos que hay en las ranuras principales, de apoyo y auxiliares y en tus drones. Los núcleos adaptativos no tienen absorción propia y no cuentan en la media (las células en un núcleo adaptativo solo suman capacidad y recarga). Sin ningún escudo equipado, tu absorción es del 0 %: el casco recibe cada impacto, y los puntos de escudo de las células de un núcleo adaptativo no se usan, así que equipa también un escudo.
- **Lo máximo de serie es el 80 %**: el mejor escudo con las mejores células, un Heavy Shield Core con tres Absorption Shield Cell IV en cada ranura. Mezclar escudos más débiles baja la media. Ninguna mejora de la Tienda de temporada ni ninguna bonificación de la Forja forma parte de esa cifra.
- **Ejemplo**: un Basic Shield Core (48 %) con dos Absorption Shield Cell I da 56 %; añade un Light Shield Core (45 %) y la media es 50,5 %.
- **La estadística no tiene tope en el 100 %.** Es lo que los escudos recibirían de un impacto antes de restar la *penetración de escudo* del atacante, así que una nave puede llevar más que un impacto entero: con 112 % sigue recibiendo en los escudos un impacto entero de un atacante con hasta un 12 % de penetración.

#### Penetración de escudo {#shield-penetration}

Algunos ataques tienen **penetración de escudo**: puntos que se restan de tu absorción para ese impacto. La parte que reciben tus escudos es

\[\text{Parte del escudo} = \text{clamp}(\text{Absorción} - \text{Penetración},\ 0,\ 100\,\%)\]

- Los escudos reciben como mucho `round(damage x share)` del impacto; el casco recibe el resto. Un escudo demasiado bajo para su parte pasa la diferencia a los HP, y si los escudos están a 0, todo el daño va directamente a los HP.
- **De dónde viene la penetración**: la *penetración de escudo* de un cohete directo (Lancet I 10 %, Lancet II 25 %, Lancet III 35 %, Rivet I 5 %, Rivet II 25 %, Rivet III 35 %, N.I.K.E. 35 %; las explosiones en área no tienen, consulta [Cohetes](/wiki/06-Items/Rockets.md)) y la de la munición láser (Ultra Core 5 %, Experimental Fusion Core 10 %; consulta [Láseres y munición](/wiki/06-Items/Lasers.md)). Los alienígenas no tienen, y tampoco la munición x1 y x2. Un impacto láser también incluye los Penetration Amps de los láseres del atacante (de +2 % a +8 % por ranura, la media de sus láseres) y la penetración de una formación de drones (Gemini +9 %, Stiletto +16 %); la suma se detiene en el **50 %** para un láser y en el 40 % para un cohete ([cómo se suma un impacto láser](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).
- **Ejemplos**: 80 % de absorción contra un Lancet III (35 %): los escudos reciben el 45 % del impacto, el casco el 55 %. Con 100 % contra él: 65 % y 35 %. Con 112 % contra un 12 % de penetración: todo el impacto. Con 45 % (un Light Shield Core solo) contra 35 %: 10 % en el escudo y el resto en el casco. Ningún cohete atraviesa por completo un Light Shield Core. El mejor láser (50 %) sí lo consigue: contra él, el mejor escudo (80 %) recibe el 30 % del impacto y el casco el 70 %, y un Light Shield Core solo (45 %) no recibe nada.
- Los alienígenas no tienen estadística de absorción: reparten cada impacto 80 % / 20 %, menos la penetración del impacto.
- El daño de una Siphon Battery sale solo del escudo: la absorción y la penetración no intervienen.

#### Alcanzar y superar el 100 % {#reaching-and-passing-100-}

- **De serie**: como mucho, el 80 % (ver arriba).
- **Shield Absorbance Boost**: una mejora permanente de la Tienda de temporada que se compra con puntos de reinicio, **+0,1 puntos por nivel, como mucho +10 puntos** (100 niveles, 25 PR cada uno). Suma puntos fijos a la absorción de tu nave, los mismos en cualquier nave con escudo: el 80 % pasa a 80,4 % con 4 niveles (100 PR), y el 45 % de un Light Shield Core pasa a 46,2 % con 12 niveles (300 PR). Una nave sin escudo equipado se queda en el 0 %. Los 100 niveles cuestan 2.500 PR, una meta para varios reinicios: las fuentes actuales de puntos de reinicio (los hitos de derribos y las misiones) pagan 855 PR en total en sus límites, acumulados de un reinicio a otro, y eso compra 34 niveles, +3,4 puntos. Hay previstas más fuentes de puntos de reinicio. Consulta [Temporada y puntos de reinicio](/wiki/03-Mechanics/Wipe-Timeline.md#cross-season-progression-permanent-buffs-).
- **Forja**: los escudos y las células de escudo pueden obtener una bonificación de **Absorción**, que multiplica la estadística: +5 % en un escudo del 50 % son +2,5 puntos. El mejor juego Eterno forjado al máximo (núcleo y tres células, con todas las bonificaciones en su valor más alto, +15 %) suma hasta 12 puntos, unos 10 de media (consulta [La Forja](/wiki/06-Items/Forge.md)).
- **En conjunto**: 80 % de serie, +3,4 puntos de la mejora (todos los 855 puntos de reinicio actuales) y hasta +12 puntos de bonificaciones de la Forja dan **95,4 %** como máximo hoy; con los 100 niveles de la mejora (+10 puntos, 2.500 PR) sería un 102 %. Ni la mejora ni la Forja llegan solas al 100 %; llegar ahí es una meta para varios reinicios, y hay previstas más fuentes de puntos de reinicio.

### Aumentos de escudo: capacidad, absorción y recarga {#shield-boosts-capacity-absorbance-recharge}

Cada aumento de escudo sube una de las tres estadísticas y aparece en su propia categoría en la ventana Potenciadores:

- **Capacidad** (puntos de escudo máximos): los potenciadores Shield Wall Booster 1 y 2 y la mejora permanente Shield Capacity Boost.
- **Absorción** (la parte de un impacto que se llevan tus escudos): la mejora permanente Shield Absorbance Boost (+0,1 puntos por nivel, como mucho +10 puntos).
- **Recarga** (puntos de escudo restaurados por segundo): el Shield Regen Booster.

Consulta [Potenciadores](/wiki/06-Items/Boosters.md) para ver las cifras.

---

## Regeneración pasiva del escudo {#shield-passive-regeneration}

Los escudos se regeneran pasivamente con el tiempo para que estés siempre listo para el combate.

- **Ciclo de regeneración**: si los escudos están por debajo de su capacidad máxima, restauran cada segundo tantos puntos de escudo como tu velocidad de recarga.
- **Interrupción por combate (15 s de retraso)**: la regeneración se detiene al recibir daño y solo se reanuda tras **15 segundos** sin recibir daño. Las formaciones de drones Adamant y Redoubt ([Formaciones de drones](/wiki/03-Mechanics/Formations.md)) son la excepción: devuelven escudo cada segundo, también en combate.
