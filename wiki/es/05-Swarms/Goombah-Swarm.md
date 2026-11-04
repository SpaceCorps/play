<!-- wiki-i18n source: 7859e3f6a7efac1e -->
<!-- wiki-i18n title: Enjambre Goombah -->
# Enjambre Goombah {#goombah-swarm}

El enjambre Goombah es un **Boss Goombah** con sus **Goombah Guards**: un [Goombah](/wiki/04-Aliens/Goombah.md) gigantesco que nunca empieza un combate, y otros más pequeños que se quedan cerca de él y lo curan. Vive en los mismos sectores que el [enjambre Phantasm](/wiki/05-Swarms/Phantasm-Swarm.md), `x-3` y `x-4`, y es un combate para un grupo de los pilotos más fuertes de los sectores de las corporaciones.

## De un vistazo {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores `x-3` y `x-4` de cada corporación
- **Cuántos**: Uno en cada uno de esos sectores, 6 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio
- **Líder**: Boss Goombah
- **Seguidores**: Hasta 4 × Goombah Guard, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 500 unidades del líder
- **Curación**: Cada Goombah Guard a menos de 600 unidades del líder cura su casco, 110 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 30 s después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: 5 min después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- goombah-glance:end -->

## Los miembros {#the-members}

- **Boss Goombah**: un Goombah más grande, con el tinte del enjambre y su nombre encima, con casco, escudo y una andanada láser propios (las cifras están más abajo). Es pasivo: merodea hasta que un piloto lo impacta, entonces va tras ese piloto y le dispara, y las naves de su enjambre cercanas se suman al combate. El alcance de su arma y su velocidad son los de un Goombah, y nunca repara su casco por sí solo.
- **Goombah Guard**: un Goombah más pequeño con el tinte del enjambre. Los Guards se mantienen cerca del jefe, se suman al combate cuando una nave de enjambre cercana es impactada, y cada uno que está cerca del jefe cura su casco. Un Guard repara su propio casco tras un descanso, como hace un Goombah.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Lleva un grupo de las naves más fuertes.** Tres pilotos de nivel 8 con munición x2 lo destruyen en unos 75 segundos en Alpha, perdiendo como mucho una nave; dos de ellos necesitan munición x4, y los pilotos de niveles más bajos no causan daño suficiente para ganar.
- **Dispara al jefe, no a los Guards.** Un Guard cae en segundos, pero llega uno nuevo con la frecuencia que dice la lista *De un vistazo*, y lo que curan los Guards es una parte pequeña de lo que causa un grupo: dejarlos en paz cuesta un poco de tiempo, perseguirlos cuesta más.
- **Beta y Gamma son más duros.** Los enjambres de esos mundos son más fuertes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), así que piden más pilotos o mejor munición.
- **Vigila el sector.** `x-4` es un sector PvP en Alpha, y `x-3` y `x-4` lo son en Beta y Gamma ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): un rival puede unirse al combate o esperar la caja. Deja una nave del grupo de guardia.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, con toda su fuerza, en el mismo sector, y sus Guards llegan uno tras otro.

## Recompensas y botín {#rewards-and-drops}

El Boss Goombah paga por el combate que es: un minuto de combate contra él paga más que un minuto contra un Goombah, el alienígena mejor pagado de estos sectores. La paga se reparte según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja es para el piloto que más daño causó y contiene el botín propio de un Goombah varias veces (Cataclysite, Quorvium, Power Cores, Reinforced Hull Plates y Ship Fragments), con munición y cohetes. Los Guards pagan poco y no sueltan nada; matarlos no es una forma de farmear, porque vuelven con el jefe.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- goombah-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Goombah

Base: Goombah, con 400 % del casco y 100 % del daño de los láseres; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 128.000 | 192.000 | 256.000 |
| Escudo | 192.000 | 288.000 | 384.000 |
| Daño de los láseres (una salva por segundo) | 3.000 | 4.500 | 6.000 |
| Velocidad | 180 | 180 | 180 |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Créditos | 120.000 | 240.000 | 360.000 |
| Thulium | 600 | 1.200 | 1.800 |
| Experiencia (XP) | 24.000 | 48.000 | 72.000 |
| Honor | 192 | 384 | 576 |
| Puntos PvE por derribo | 14 | 14 | 14 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Ship Fragment | 100 % en cada una de 8 tiradas | 3 |
| Reinforced Hull Plate | 60 % en cada una de 8 tiradas | 1 |
| Power Core | 25 % en cada una de 8 tiradas | 1 |
| Cataclysite | 100 % en cada una de 8 tiradas | 4 |
| Quorvium | 100 % en cada una de 8 tiradas | 2–4 |
| Advanced Plasma | 100 % | 100–200 |
| Ultra Core | 100 % | 100–200 |
| Uno de los 8 [cohetes](/wiki/06-Items/Rockets.md) que se compran con créditos, elegido al azar | 100 % | 6–10 |

### Goombah Guard

Base: Goombah, con 20 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 6.400 | 9.600 | 12.800 |
| Escudo | 9.600 | 14.400 | 19.200 |
| Daño de los láseres (una salva por segundo) | 600 | 900 | 1.200 |
| Velocidad | 180 | 180 | 180 |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Cura al líder, cada uno, por segundo (solo el casco) | 110 | 165 | 220 |
| Créditos | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experiencia (XP) | 12 | 24 | 36 |
| Honor | 1 | 2 | 3 |
| Puntos PvE por derribo | 3 | 3 | 3 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- goombah-members:end -->
