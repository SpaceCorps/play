<!-- wiki-i18n source: abb582fd63389ab9 -->
<!-- wiki-i18n title: Enjambre Phantasm -->
# Enjambre Phantasm {#phantasm-swarm}

El enjambre Phantasm es un **Boss Phantasm** con sus **Phantasm Guards**: un [Phantasm](/wiki/04-Aliens/Phantasm.md) enorme que nunca empieza un combate, y otros más pequeños que se quedan cerca de él y lo curan. Vive en los sectores exteriores de las corporaciones, `x-3` y `x-4`, y es un combate para un grupo de pilotos de nivel medio.

## De un vistazo {#at-a-glance}

<!-- phantasm-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores `x-3` y `x-4` de cada corporación
- **Cuántos**: Uno en cada uno de esos sectores, 6 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio (Beta y Gamma: desde el día 1 de la temporada)
- **Líder**: Boss Phantasm
- **Seguidores**: Hasta 4 × Phantasm Guard, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 500 unidades del líder
- **Curación**: Cada Phantasm Guard a menos de 600 unidades del líder cura su casco, 30 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 30 s después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: 2 min después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- phantasm-glance:end -->

## Los miembros {#the-members}

- **Boss Phantasm**: un Phantasm más grande, con el tinte del enjambre y su nombre encima, con casco, escudo y una andanada láser propios (las cifras están más abajo). Es pasivo: merodea hasta que un piloto lo impacta, entonces va tras ese piloto y le dispara, y las naves de su enjambre cercanas se suman al combate. El alcance de su arma y su velocidad son los de un Phantasm, y nunca repara su casco por sí solo.
- **Phantasm Guard**: un Phantasm más pequeño con el tinte del enjambre. Los Guards se mantienen cerca del jefe, se suman al combate cuando una nave de enjambre cercana es impactada, y cada uno que está cerca del jefe cura su casco. Un Guard repara su propio casco tras un descanso, como hace un Phantasm.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Lleva un grupo.** Tres pilotos de nivel 4–5 con munición x2 lo destruyen en aproximadamente minuto y medio en Alpha, perdiendo como mucho una nave; un piloto de ese nivel solo es destruido, y dos lo ganan por muy poco, y solo mientras los golpes se reparten. Mejores naves y munición x4 lo hacen mucho más rápido.
- **Dispara al jefe, no a los Guards.** Un Guard cae en segundos, pero llega uno nuevo con la frecuencia que dice la lista *De un vistazo*, y lo que curan los Guards es una parte pequeña de lo que causa un grupo: dejarlos en paz cuesta un poco de tiempo, perseguirlos cuesta más.
- **Beta y Gamma son más duros.** Los enjambres de esos mundos son más fuertes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), así que piden más pilotos o mejor munición.
- **Vigila el sector.** `x-4` es un sector PvP en Alpha, y `x-3` y `x-4` lo son en Beta y Gamma ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): un rival puede unirse al combate o esperar la caja. Deja una nave del grupo de guardia.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, con toda su fuerza, en el mismo sector, y sus Guards llegan uno tras otro.

## Recompensas y botín {#rewards-and-drops}

El Boss Phantasm paga por el combate que es: un minuto de combate contra él paga más que un minuto contra un Goombah, el alienígena mejor pagado de estos sectores. La paga se reparte según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja es para el piloto que más daño causó y contiene el botín propio de un Phantasm muchas veces (Ship Fragments, Daraxium y Nyxite), con munición y cohetes. Los Guards pagan poco y no sueltan nada; matarlos no es una forma de farmear, porque vuelven con el jefe.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- phantasm-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Phantasm

Base: Phantasm, con 2.000 % del casco y 300 % del daño de los láseres; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 40.000 | 60.000 | 80.000 |
| Escudo | 64.000 | 96.000 | 128.000 |
| Daño de los láseres (una salva por segundo) | 1.050 | 1.575 | 2.100 |
| Velocidad | 160 | 160 | 160 |
| Alcance de los láseres | 700 | 700 | 700 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Créditos | 39.000 | 78.000 | 117.000 |
| Thulium | 195 | 390 | 585 |
| Experiencia (XP) | 7.800 | 15.600 | 23.400 |
| Honor | 62 | 124 | 186 |
| Puntos PvE por derribo | 8 | 8 | 8 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Ship Fragment | 100 % en cada una de 13 tiradas | 1 |
| Daraxium | 60 % en cada una de 13 tiradas | 1–2 |
| Nyxite | 60 % en cada una de 13 tiradas | 1–2 |
| Standard Battery | 100 % | 600–1.200 |
| Advanced Plasma | 100 % | 60–100 |
| Ultra Core | 100 % | 10–20 |
| Uno de los 8 [cohetes](/wiki/06-Items/Rockets.md) que se compran con créditos, elegido al azar | 100 % | 4–6 |

### Phantasm Guard

Base: Phantasm, con 50 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 1.000 | 1.500 | 2.000 |
| Escudo | 1.600 | 2.400 | 3.200 |
| Daño de los láseres (una salva por segundo) | 175 | 263 | 350 |
| Velocidad | 160 | 160 | 160 |
| Alcance de los láseres | 700 | 700 | 700 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Cura al líder, cada uno, por segundo (solo el casco) | 30 | 45 | 60 |
| Créditos | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experiencia (XP) | 12 | 24 | 36 |
| Honor | 1 | 2 | 3 |
| Puntos PvE por derribo | 1 | 1 | 1 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- phantasm-members:end -->
