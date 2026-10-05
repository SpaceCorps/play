<!-- wiki-i18n source: c1ec7aa1207d519d -->
<!-- wiki-i18n title: Enjambres -->
# Enjambres {#swarms}

Un **enjambre** es un grupo de alienígenas que recorre una parte de la galaxia bajo un **líder**: un jefe mucho más fuerte que cualquier alienígena a su alrededor, con **seguidores** que lo protegen y, en dos de los enjambres, lo curan. Hay tres, y cada uno tiene su propio artículo:

- [Enjambre Seeker](/wiki/05-Swarms/Seeker-Swarm.md): el Boss Seeker y sus Seeker Slaves, el enjambre más pequeño, en los sectores donde vuelan los pilotos nuevos.
- [Enjambre Pirate](/wiki/05-Swarms/Pirate-Swarm.md): el Pirate Boss y sus Pirate Scouts, un combate largo para un grupo.
- [Enjambre Dormant](/wiki/05-Swarms/Dormant-Swarm.md): la Dormant Force y sus Dormant Pulses, el enjambre más fuerte, con el botín más rico.

Sus naves son **alienígenas de tipos propios**: tienen nombres propios y contadores de derribos propios, y ninguna cuenta como un Seeker, un Phantasm ni ningún otro alienígena. Una nave de enjambre tiene la forma de la nave en la que se basa, con un tinte propio y su nombre encima; el Boss Seeker es un Seeker mucho más grande.

Los **guardianes del clan** no son enjambres públicos. Un clan invoca a su propio guardián para el último paso de su línea diaria, y solo ese clan puede dañarlo: ningún piloto se topa con uno vagando por un sector, y las tablas de abajo no los incluyen. Consulta [Clanes](/wiki/03-Mechanics/Clans.md#clan-wardens).

## Los tres enjambres {#the-three-swarms}

<!-- swarms-list:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Enjambre | Dónde | Cuántos | Líder | Seguidores | Vuelve |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**Enjambre Pirate**](/wiki/05-Swarms/Pirate-Swarm.md) | Los sectores `x-2` y `x-3` de cada corporación | Uno en cada uno de esos sectores, 6 en cada mundo | **Pirate Boss** | Hasta 5 × Pirate Scout, uno nuevo cada 10 s | 2 min después de que destruyan al líder, en el mismo sector |
| [**Enjambre Dormant**](/wiki/05-Swarms/Dormant-Swarm.md) | Los sectores de peligro `DS-1`, `DS-2`, `DS-3`, `DS-4`, volando de uno a otro | Uno en cada mundo | **Dormant Force** | 2 × Dormant Pulse, que vuelan con el líder | 1 h después de que destruyan a todo el enjambre, en un sector de peligro al azar |
| [**Enjambre Seeker**](/wiki/05-Swarms/Seeker-Swarm.md) | Los sectores `x-1` y `x-2` de cada corporación | Uno en cada uno de esos sectores, 6 en cada mundo | **Boss Seeker** | Hasta 4 × Seeker Slave, uno nuevo cada 10 s | 2 min después de que destruyan al líder, en el mismo sector |

<!-- swarms-list:end -->

## Cuándo y dónde {#when-and-where}

Los enjambres empiezan a aparecer con el **Primer Contacto** y se quedan hasta el reinicio (consulta la [Cronología del reinicio](/wiki/03-Mechanics/Wipe-Timeline.md); el día es la primera línea de las reglas de más abajo). **Cada mundo tiene sus propios enjambres** en los mismos lugares, así que el Pirate Boss de Alpha y el de Beta son dos naves distintas, y un enjambre que destruyes en tu mundo no queda destruido en otro. Un enjambre destruido vuelve pasado el tiempo de la tabla de arriba.

## Las reglas de todos los enjambres {#the-rules-of-every-swarm}

<!-- swarms-rules:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- Los enjambres aparecen desde el día 4 de la temporada hasta el reinicio.
- Cuando una nave de enjambre recibe un impacto, las naves de su enjambre a menos de 1.500 unidades se suman al combate contra el primer piloto que la impactó.
- Un líder aparece al menos a 2.500 unidades del borde de cada anillo de estación y de portal.
- Un piloto que causó al menos 5 % del daño hecho a un jefe cobra por su derribo.

<!-- swarms-rules:end -->

## Los mundos {#the-worlds}

El mundo escala un enjambre como escala a todos los alienígenas ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): el casco, el escudo, la recarga del escudo, el daño de los láseres, el daño de los cohetes y la curación de una nave de enjambre son las cifras de Alpha multiplicadas por la fuerza de más abajo, y un derribo paga la paga de más abajo. La velocidad, el alcance y el botín son iguales en todos los mundos. Los artículos dan las cifras de cada nave en los tres mundos.

<!-- swarms-world:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Mundo | Fuerza | Paga |
| :--- | ---: | ---: |
| **Alpha** | ×1 | ×1 |
| **Beta** | ×1,5 | ×2 |
| **Gamma** | ×2 | ×3 |

<!-- swarms-world:end -->

## Qué se les avisa a los pilotos {#what-the-pilots-are-told}

Los enjambres Seeker y Pirate avisan a los pilotos de su propio sector cuando aparece un jefe y cuando es destruido. El enjambre Dormant avisa a todo su mundo, y está marcado en los mapas de los sectores de peligro y en el mapa galáctico, para que los pilotos puedan encontrarlo. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El derribo de un jefe también tiene una línea en el registro de bajas que nombra al piloto al que se le acredita. La lista *De un vistazo* de cada artículo dice a quién se avisa.

## Combatir a un enjambre {#fighting-a-swarm}

- **Los líderes nunca empiezan un combate.** Un líder merodea hasta que un piloto lo impacta, entonces responde, y las naves de su enjambre cercanas a él se suman al combate contra el primer piloto que lo impactó (la distancia está en las reglas de arriba). Los Pirate Scouts son la excepción: atacan a cualquier piloto que se les acerque. Un líder nunca repara su casco por sí solo, así que el daño que le hiciste se queda en él a menos que sus seguidores lo curen; su escudo se recarga como el de cualquier alienígena.
- **Las naves de enjambre solo combaten contra pilotos.** No disparan a los alienígenas y los alienígenas no les disparan a ellas, y los [pilotos de corporación](/wiki/03-Mechanics/Company-Pilots.md) las ignoran: no cazan una nave de enjambre ni acuden en tu ayuda contra una.
- **Cohetes.** El Pirate Boss, la Dormant Force y las Pulses disparan cohetes **rectos**, [cohetes Rivet](/wiki/06-Items/Rockets.md), contra el piloto que los atacó. Una nave que no deja de moverse los esquiva; una que se queda quieta recibe el impacto.
- **El tamaño de los combates.** El enjambre Seeker es para dos pilotos, el Pirate para un grupo pequeño y el Dormant para un grupo grande de las naves más fuertes; los mundos más altos piden más pilotos, como con cualquier alienígena.

## Qué llevar {#what-to-bring}

- **Un grupo.** Vuela en [grupo](/wiki/03-Mechanics/Groups.md): los enjambres están equilibrados para grupos, un piloto solo de nivel bajo es destruido enseguida, y solo las naves más fuertes pueden derrotar a un Pirate Boss en solitario. Nadie derrota solo al enjambre Dormant. Un enjambre combate contra el primer piloto que lo impactó ([A quién combate un alienígena](/wiki/03-Mechanics/Combat.md#who-an-alien-fights)), así que deja que empiece la nave más resistente del grupo.
- **Mejor munición.** Lleva munición x2 o mejor (consulta [Láseres y munición](/wiki/06-Items/Lasers.md)). La curación de los seguidores de un enjambre puede superar lo que un grupo pequeño causa con munición x1.
- **Escudos y reparaciones** para un combate largo: las habilidades de tu nave ([Habilidades](/wiki/03-Mechanics/Abilities.md)) importan sobre todo en el combate contra los piratas, que dura minutos.
- **Espacio para moverte.** Mantente fuera del alcance de un arma a la que superas en alcance, y no dejes de moverte frente a un cohete.

## Cómo paga el derribo de un jefe {#how-a-boss-kill-pays}

Un alienígena normal paga al piloto que lo impactó primero ([Combate](/wiki/03-Mechanics/Combat.md#kill-rewards-first-hit-claims)). El líder de un enjambre, y cada Dormant Pulse, pagan en cambio **según el daño causado**:

- **La paga se reparte según el daño.** Cada piloto que causó al menos la parte indicada en las reglas de arriba cobra, en proporción al daño causado: los créditos, el Thulium, la XP y el honor del derribo se reparten entre ellos. Un piloto por debajo de esa parte no cobra nada.
- **La caja de carga es para el piloto que más daño causó.** Es suya (y de su clan) durante 30 segundos, como con cualquier alienígena, y después puede cogerla cualquiera ([Carga](/wiki/03-Mechanics/Cargo.md)). Cada nave Dormant tiene su propio recuento de daño y su propia caja.
- **Los seguidores pagan como siempre**: los Pirate Scouts y los Seeker Slaves pagan al piloto que los impactó primero, y su paga es pequeña comparada con la de un jefe.
- **La paga de un jefe está hecha para superar a los alienígenas de su entorno.** Un minuto de combate contra un Pirate Boss paga más que un minuto de combate contra un Goombah, y el enjambre Dormant paga todavía más; el Boss Seeker paga exactamente diez Seekers.

Cada derribo se cuenta con el nombre propio de la nave en tus estadísticas de derribos y suma puntos PvE a tu clasificación:

<!-- swarms-points:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

| Nave de enjambre | Enjambre | Puntos PvE por derribo |
| :--- | :--- | ---: |
| **Pirate Boss** | Enjambre Pirate | 10 |
| **Pirate Scout** | Enjambre Pirate | 1 |
| **Dormant Force** | Enjambre Dormant | 25 |
| **Dormant Pulse** | Enjambre Dormant | 10 |
| **Boss Seeker** | Enjambre Seeker | 5 |
| **Seeker Slave** | Enjambre Seeker | 1 |

<!-- swarms-points:end -->

El derribo de una nave de enjambre no cuenta como derribo de ningún otro alienígena: un Boss Seeker o un Seeker Slave no es un Seeker para una misión que pide Seekers, y los hitos de los puntos de reinicio ([Cronología del reinicio](/wiki/03-Mechanics/Wipe-Timeline.md#earning-wipe-points)) son solo los de los cinco alienígenas. Las misiones que piden naves de enjambre están en [Misiones de enjambre](/wiki/03-Mechanics/Quests.md#swarm-missions).
