<!-- wiki-i18n source: 72a495647503f96a -->
<!-- wiki-i18n title: Drones -->
# Mecánicas de los drones {#drone-mechanics}

Los drones son unidades de apoyo autónomas que vuelan junto a tu nave. Aportan ranuras de equipo adicionales y contribuyen directamente al rendimiento en combate de tu nave. Un Slave Drone además crece: gana experiencia cada vez que destruyes un alienígena y sube por **ocho niveles**, desde una pequeña esfera blindada hasta una cañonera con alas en forma de media luna. En Ensamblaje, un Slave Drone se puede mejorar a **Master Drone**, que vuelve a empezar sus niveles (consulta Master Drone, más abajo).

## Conseguir drones {#getting-drones}

Cada dron que tienes, sea un **Slave Drone** o un Master Drone, abre sus ranuras de dron (una en un Slave Drone, dos en un Master Drone), hasta **8** drones. La tienda vende Slave Drones por créditos y, a partir del cuarto, también por Thulium. Cada uno cuesta más que el anterior: los precios están en [Drones](/wiki/05-Items/Drones.md).

## Formación y movimiento {#formation-movement}

Los drones vuelan en una formación estándar **«Compañero de ala» (2-2-4)**:

- **2 drones** junto a la nave, uno en cada flanco.
- **2 drones** a los lados y justo detrás.
- **4 drones** en cola, detrás.

Usan un algoritmo de seguimiento suave que ajusta su posición según la velocidad y la rotación de tu nave, y cierran la formación en las maniobras bruscas. Ninguno vuela por delante de ti.

Los drones son pequeños y se mantienen cerca: un dron de nivel 8 mide unas 19,5 unidades de ancho (una Protos, 50) y uno de nivel 1 es una bola de unas 8, así que toda la formación cabe en unas 135 unidades alrededor de tu nave. El dron que compraste primero es el que tiene más experiencia y vuela en tu flanco izquierdo, el segundo en el derecho, y los más nuevos van detrás.

## Equipo y estadísticas {#equipment-stats}

Los drones funcionan como bastidores de equipo que amplían tu nave.

- Un Slave Drone tiene **1 ranura** y un Master Drone **2**, hasta **8 drones**.
- En estas ranuras puedes equipar **láseres** y **escudos**, en cualquiera de las dos ranuras de un Master Drone. Nada más cabe: ni motores ni núcleos adaptativos.
- **Los láseres cuentan por completo.** Un láser en un dron dispara cuando tú disparas, suma su daño a tu andanada y gasta munición como cualquier otro láser (cada láser consume una unidad de munición por andanada). Los dos láseres de un Master Drone son dos láseres.
- **Los escudos también cuentan por completo.** Un escudo en un dron cuenta como uno en una ranura principal, en cualquiera de las dos ranuras: su capacidad y su recarga con sus células, su absorción en la media de tu nave, su bono de escudo y su penalización de velocidad. Se ordena junto con los escudos de la propia nave según su capacidad (los cuatro más grandes cuentan por completo, del quinto en adelante cuentan menos; consulta [Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md)), y las bonificaciones de la Forja, las mejoras de la Tienda de temporada y la penetración de escudo de un atacante actúan sobre él como sobre cualquier escudo. El nivel del dron mejora solo su láser, nunca su escudo. Mientras se mejora un dron, sus ranuras están desconectadas, tanto la del escudo como la del láser. Antes de la 0.4.7, un escudo en un dron no sumaba nada.
- **¿Un láser o un escudo?** Una ranura admite una cosa u otra: un láser suma un láser a tu andanada, un escudo suma sus puntos de escudo. En una nave pequeña con buenos escudos, los puntos extra suman poco, porque su casco se agota antes; en un casco grande permiten aguantar mucho más.

## Niveles {#levels}

Todo Slave Drone empieza en el nivel 1 y gana experiencia (XP) cada vez que destruyes un alienígena. Un Master Drone también empieza en el nivel 1, sin XP, y sube de nivel de la misma forma. Cada nivel pide más que el anterior, y el aspecto cambia con él, así que puedes ver lo lejos que ha llegado un dron. La tabla da, para cada nivel, la XP necesaria para subir a él desde el nivel anterior y cuántos derribos de un solo tipo de alienígena supone eso (en el mundo Alpha: Beta necesita más o menos la mitad, Gamma alrededor de un tercio):

<!-- drones:begin -->
<!-- Generated from server/Resources/drone-levels.json by scripts/drones-wiki.sh: don't edit by hand. -->

- **Nivel 1, Semilla:** una pequeña esfera blindada con una lente cian.
- **Nivel 2, Halo:** la esfera dentro de un anillo flotante.
- **Nivel 3, Disco:** un disco plano bajo una cúpula de cristal.
- **Nivel 4, Platillo:** un platillo con placas de blindaje y tomas de aire.
- **Nivel 5, Cañonera:** al platillo se le suman una proa y dos cañones.
- **Nivel 6, Brotes alares:** cañones y cuchillas alares cortas sobre pilones.
- **Nivel 7, Medias alas:** cuchillas alares más largas con puntas doradas.
- **Nivel 8, Creciente:** la cañonera terminada: alas en media luna completas con tiras de luz cian.

| Nivel | XP para alcanzarlo | XP del nivel | Daño de láser | Derribos de Seeker | Derribos de Bulwark | Derribos de Goombah |
| --: | --: | --: | --: | --: | --: | --: |
| 1 | 0 | – | – | – | – | – |
| 2 | 350 | 350 | – | 350 | 44 | 15 |
| 3 | 900 | 550 | +1 % | 550 | 69 | 23 |
| 4 | 2.000 | 1.100 | +2 % | 1.100 | 138 | 46 |
| 5 | 3.700 | 1.700 | +3 % | 1.700 | 213 | 71 |
| 6 | 6.000 | 2.300 | +4 % | 2.300 | 288 | 96 |
| 7 | 9.500 | 3.500 | +5 % | 3.500 | 438 | 146 |
| 8 | 14.000 | 4.500 | +7 % | 4.500 | 563 | 188 |

| Alienígena | XP por cada dron |
| :--- | --: |
| Seeker | 1 |
| Phantasm | 2 |
| Bulwark | 8 |
| Goombah | 24 |
| Crystalys | 72 |

<!-- drones:end -->

### Cómo ganan XP los drones {#how-drones-earn-xp}

- **Todos tus drones ganan la misma XP** por cada derribo de alienígena por el que cobras: los 8 primeros drones, lleven o no un láser. Un dron que compras más tarde empieza en el nivel 1 sin XP, así que tus primeros drones siempre son los de nivel más alto.
- **Los alienígenas más duros valen más.** La XP que da cada alienígena está en la segunda tabla de arriba (el Crystalys vale lo que 72 Seekers). Cualquier otro alienígena da 1.
- **Los mundos pagan más.** Beta duplica la XP y Gamma la triplica (los alienígenas de allí también tienen más vida). Los potenciadores y Premium no la cambian.
- **Los derribos cuentan cuando te pagan.** Un alienígena que rematas mientras otro piloto tiene su reclamación no da nada a tus drones, igual que no te da nada a ti. Los derribos de jugadores, las misiones y los derribos propios de los pilotos de corporación no dan XP a los drones.
- **El nivel 8 es el último.** La XP sigue sumándose después.

### Qué da cada nivel {#what-a-level-gives}

El **láser instalado en la ranura de un dron** inflige más daño base a medida que su dron sube de nivel: nada en los niveles 1 y 2, luego +1 % en el nivel 3 y así hasta **+7 % en el nivel 8**. La bonificación multiplica el daño propio de ese láser (después de su encantamiento); los amplificadores instalados en él se suman encima y no se multiplican. El hangar muestra el nivel de cada dron, su barra de XP y los derribos que pide el siguiente nivel, y sus cifras de daño ya incluyen la bonificación. Cuando un dron sube de nivel, el Registro de juego lo indica («El dron 2 alcanzó el nivel 4.») y el dron destella con un anillo de luz.

### Cuánto se tarda {#how-long-it-takes}

La curva está pensada para que un dron nuevo llegue al nivel 2 en más o menos una hora de juego normal (cazando Bulwarks y Goombahs), y al nivel 8 en unas 27 horas de juego. Esas horas son para un piloto que compra el primer dron hacia las misiones de nivel 7; con peor equipo se tarda más (hasta unas 4 horas para el nivel 2 y 150 horas para el nivel 8). Cazar un solo tipo de alienígena es, como mucho, alrededor de un 50 % más rápido que una mezcla normal. Los drones se conservan tras el reinicio de temporada con sus niveles y su experiencia, así que esas horas se invierten una sola vez, a lo largo de tantas temporadas como haga falta: un piloto que juega media hora al día lo consigue en un par de temporadas.

### Master Drone {#master-drone}

Un Slave Drone se convierte en **Master Drone** cuando lo mejoras en Ensamblaje. La receta cuesta 40.000 de Thulium y 100 Ship Fragments, tarda 60 segundos y no gasta ningún dron: **eliges qué Slave Drone es** (el selector muestra el nivel y la XP de cada uno), y ese mismo dron, con su número, su ranura de dron y todo lo que lleva instalado, se convierte en Master Drone cuando termina el trabajo, con una segunda ranura vacía. Nada va a tu inventario y no hay nada que recoger: el Registro de juego te avisa cuando termina, también si la mejora terminó mientras estabas fuera.

**Su nivel y su XP se restablecen a 0 cuando termina la mejora.** Un Master Drone vuelve a empezar en el nivel 1, sin XP, y sube de nivel igual que un Slave Drone (la tabla de arriba); la bonificación láser del nivel que tenía desaparece con él. El Ensamblaje lo avisa antes de empezar y, si el dron tiene algo de XP, te pide confirmación nombrándolo. La opción por defecto es el dron con menos XP.

Mientras dura la mejora, el dron está bloqueado: no puedes volver a mejorarlo ni eliminarlo, y su ranura está **desconectada**, así que el láser que lleva no dispara hasta que termina el trabajo (hasta entonces sigue siendo un Slave Drone con una ranura). Se pone en cola detrás de tus otros trabajos, como cualquier fabricación.

Un Master Drone es uno de tus 8 drones: cuenta para el límite de drones y para el precio del siguiente Slave Drone, así que mejorar no cambia ninguna de las dos cosas, y se conserva tras el reinicio de temporada con su nivel y su XP. En vuelo es la cañonera terminada, en dorado. Un Master Drone tiene **dos ranuras de equipo** donde un Slave Drone tiene una: cada una admite un láser o un escudo, y la bonificación de nivel se aplica al láser de cualquiera de las dos. Por lo demás es un Slave Drone: los mismos ocho niveles y la misma bonificación láser. Los Master Drones que fabricaste antes de que tuvieran la segunda ranura ya la tienen, con lo que llevaban en el mismo sitio. Los Master Drones fabricados antes de que existieran las mejoras sobre el propio dron son objetos normales de tu inventario y no vuelan.

## Comportamiento en combate {#combat-behavior}

- **Láseres**: los drones disparan sus láseres equipados contra tu objetivo fijado.
- **Daño**: los drones pueden recibir daño (si existe una lógica de entidad propia; por ahora comparten casi siempre la reserva de la nave, aunque se vean como algo aparte). _Nota: por ahora, los drones son extensiones indestructibles de la nave._
