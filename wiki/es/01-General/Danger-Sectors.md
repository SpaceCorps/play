<!-- wiki-i18n source: e2db1138ec491432 -->
<!-- wiki-i18n title: Sectores de peligro -->
# Sectores de peligro {#danger-sectors}

<!-- wiki-search: ds; ds-1; ds-2; ds-3; ds-4; central pvp zone; pvp zone; pulsar; giant excavator; excavator; dormant swamp; swamp; event 2; tech surge; sector de peligro; excavadora gigante; excavadora; púlsar; pantano; auge tecnológico -->

Los **sectores de peligro** son los cuatro sectores del centro de la galaxia, `DS-1` a `DS-4`. Allí se encuentran las tres corporaciones, y en todos los mundos los pilotos pueden combatir entre sí ([Viajes por el mapa espacial](/wiki/01-General/Spacemap%20Travel.md)). `DS-1`, `DS-2` y `DS-3` tienen cada uno la puerta de una corporación; `DS-4` es el núcleo, con el [agujero negro](/wiki/03-Mechanics/Black-Hole.md) en el medio. Ninguno tiene estación: los únicos lugares seguros son los anillos alrededor de las puertas de salto.

Aquí vivió una civilización de la vieja galaxia, avanzada y de color negro violáceo, y por una razón que nadie conoce se derrumbó. Sus restos nunca estuvieron del todo muertos: el [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md) fue la primera señal. Desde el **día 11 de la temporada**, el comienzo del evento 2 (**Auge Tecnológico**, consulta la [Cronología del reinicio](/wiki/03-Mechanics/Wipe-Timeline.md#30-day-season-schedule)), despierta más de ella y los sectores de peligro cambian. Todos los pilotos del mundo se enteran el día en que empieza, y lo nuevo se queda hasta el reinicio.

## Qué hay de nuevo desde el día 11 {#what-is-new-from-day-11}

- **Púlsares y excavadoras gigantes.** `DS-1`, `DS-2` y `DS-3` reciben cada uno un púlsar con una **excavadora gigante** a su lado. Pon Dark Matter en el depósito de la excavadora, elige un recurso, y ella mina el púlsar: Thulium y minerales raros caen a su alrededor en cajas que puede recoger cualquiera. Es lo más rico por lo que pelear en los sectores de peligro, y lo más peligroso. Consulta [Excavadora gigante](/wiki/03-Mechanics/Giant-Excavator.md).
- **Slumbering Voids.** Mientras una excavadora mina, los **Slumbering Voids** llegan en oleadas desde el borde del mapa y cazan a los pilotos que están cerca. Otros patrullan el pantano. Consulta [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#slumbering-void).
- **El Dormant Swamp.** En una esquina de `DS-4` está la base de la civilización perdida: cañones que disparan a toda nave que ven, Inert Masses que la guardan y, en el centro, el Unwakened. Es un lugar que los pilotos todavía no deben visitar. Consulta [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md).
- **Un Enjambre Dormant más rápido y más rico.** El enjambre aparece ahora en el pantano, vuelve antes después de ser destruido y paga el doble. Consulta [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md).
- **Antes del día 11** nada de esto existe: los sectores de peligro son como los describe [Viajes por el mapa espacial](/wiki/01-General/Spacemap%20Travel.md). Un mundo que está en el día 11 o después lo tiene todo de golpe.

## Dónde está cada cosa {#where-everything-is}

Cada mundo tiene su propia copia de todo, y un púlsar y su excavadora están en el tercio abierto de su sector, lejos de todos los anillos de puertas, en el lado que mira al centro del mapa. Las distancias son en unidades del mapa; los sectores miden 32.000 por 18.000 unidades.

<!-- danger-sites:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

| Sector | Puerta de la corporación | Púlsar | Excavadora gigante |
| :--- | :--- | :--- | :--- |
| `DS-1` | Mars | 8.000 / 5.000 | 8.805 / 5.402 |
| `DS-2` | Terra | 8.000 / 13.000 | 8.805 / 12.598 |
| `DS-3` | Galactic | 24.000 / 13.000 | 23.195 / 12.598 |

<!-- danger-sites:end -->

`DS-4` no tiene púlsar: allí está el agujero negro. Su esquina contiene en cambio el Dormant Swamp; sus cifras están en [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#at-a-glance).

<!-- danger-rules:begin -->
<!-- Generated from server/Resources/Excavator.json and DormantSwamp.json (and Rockets.json, Values/ranking-config.json) by scripts/dormant-wiki.sh: don't edit by hand. -->

- Todo lo nuevo aparece el día 11 de la temporada y se queda hasta el reinicio.
- Cada mundo tiene sus propios púlsares, excavadoras y pantano: lo que ocurre en uno no ocurre en otro.
- Ningún asteroide queda a menos de 2.600 unidades de un púlsar, a menos de 2.200 unidades de una excavadora gigante ni a menos de 4.900 unidades del centro del Dormant Swamp.

<!-- danger-rules:end -->

## Cómo evitar problemas {#keeping-out-of-trouble}

- **Radiación.** Una excavadora que se ha sobrecalentado o ha sido destruida, y su púlsar, queman toda nave que se quede dentro de sus círculos ([Excavadora gigante](/wiki/03-Mechanics/Giant-Excavator.md#heat-and-radiation)). El juego te avisa antes, y el mapa del Sistema estelar y el minimapa dibujan los círculos.
- **Los cañones del pantano.** Las torretas del pantano disparan a una nave que puedan ver mucho antes de que ella vea nada que valga el viaje ([Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md#the-guns)). Un rumbo que marcas con un clic se desvía alrededor de los cañones y de la radiación, como alrededor del agujero negro, y un aviso te advierte si el lugar donde haces clic queda dentro.
- **Si te destruyen allí,** la opción de volver **en el sitio** te coloca en el punto más cercano fuera de la radiación y fuera de la zona del pantano, como con el agujero negro ([Primeros pasos](/wiki/01-General/Getting-Started.md#dying-and-coming-back)).
- **Un grupo y una salida.** Las excavadoras atraen a los Voids y a los rivales por igual. Ve con un [grupo](/wiki/03-Mechanics/Groups.md), sabe cuál es la puerta más cercana y recuerda que en los sectores de peligro no puedes saltar mientras te atacan ([Saltar bajo fuego](/wiki/01-General/Spacemap%20Travel.md#jumping-under-fire)).
- **El resto es PvP como siempre.** Nada de esto es un lugar seguro: valen las reglas normales de tu mundo, rivales incluidos.

## Dónde leer más {#where-to-read-more}

- [Excavadora gigante](/wiki/03-Mechanics/Giant-Excavator.md): el panel, el combustible, qué mina, los Voids, el calor y la radiación.
- [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md): los cañones, los tres alienígenas y el nuevo hogar del enjambre.
- [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md) y [Enjambres](/wiki/05-Swarms/Swarms.md).
- [El agujero negro](/wiki/03-Mechanics/Black-Hole.md) y [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md): de dónde viene el combustible.
- [Minería de asteroides](/wiki/03-Mechanics/Asteroid-Mining.md): las rocas de los sectores de peligro.
