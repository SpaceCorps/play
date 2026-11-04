<!-- wiki-i18n source: 62896aebea81e95a -->
<!-- wiki-i18n title: Enjambre Crystalys -->
# Enjambre Crystalys {#crystalys-swarm}

El enjambre Crystalys es un **Boss Crystalys** con sus **Crystalys Guards**: el más duro de los alienígenas, el [Crystalys](/wiki/04-Aliens/Crystalys.md), crecido, con guardias que se quedan cerca de él y lo curan. Vive en los [sectores de peligro](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` y `DS-3`, uno en cada uno, y nunca abandona su sector. Los sectores de peligro son sectores PvP, así que el combate es para un grupo grande de los pilotos más fuertes, y el jefe no es el único peligro allí.

## De un vistazo {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores de peligro `DS-1`, `DS-2`, `DS-3`
- **Cuántos**: Uno en cada uno de esos sectores, 3 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio
- **Líder**: Boss Crystalys
- **Seguidores**: Hasta 3 × Crystalys Guard, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 500 unidades del líder
- **Curación**: Cada Crystalys Guard a menos de 600 unidades del líder cura su casco, 250 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 30 s después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: 30 min después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- crystalys-glance:end -->

## Los miembros {#the-members}

- **Boss Crystalys**: un Crystalys más grande, con el tinte del enjambre y su nombre encima, con casco, escudo y una andanada láser propios (las cifras están más abajo). Es pasivo: merodea hasta que un piloto lo impacta, entonces va tras ese piloto y le dispara, y las naves de su enjambre cercanas se suman al combate. El alcance de su arma y su velocidad son los de un Crystalys, y nunca repara su casco por sí solo.
- **Crystalys Guard**: un Crystalys más pequeño con el tinte del enjambre. Los Guards se mantienen cerca del jefe, se suman al combate cuando una nave de enjambre cercana es impactada, y cada uno que está cerca del jefe cura su casco. Un Guard repara su propio casco tras un descanso, como hace un Crystalys.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Lleva un grupo grande.** Ocho pilotos de nivel 8 en Paragons con munición x2 lo destruyen en aproximadamente un minuto en Alpha, perdiendo como mucho una nave; cuatro necesitan munición x4, y un piloto solo es destruido.
- **Dispara al jefe, no a los Guards.** Un Guard cae en segundos, pero llega uno nuevo con la frecuencia que dice la lista *De un vistazo*, y lo que curan los Guards es una parte pequeña de lo que causa un grupo: dejarlos en paz cuesta un poco de tiempo, perseguirlos cuesta más.
- **Beta y Gamma son más duros.** Los enjambres de esos mundos son más fuertes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), así que piden más pilotos o mejor munición.
- **Los sectores de peligro son PvP.** Un rival puede atacar al grupo en mitad del combate y esperar la caja: es del piloto que más daño causó (y de su clan) durante 30 segundos, y después de cualquiera ([Carga](/wiki/03-Mechanics/Cargo.md)). No vayas solo.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, con toda su fuerza, en el mismo sector, y sus Guards llegan uno tras otro.

## Recompensas y botín {#rewards-and-drops}

El Boss Crystalys paga por el combate que es: un minuto de combate contra él paga más que un minuto contra un Crystalys, el alienígena mejor pagado. La paga se reparte según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja es para el piloto que más daño causó y contiene Cataclysite y Quorvium, de vez en cuando un Power Core, una Ancient Control Unit o Dark Matter, munición x3 y x4 y cohetes Épicos. Los Guards pagan poco y no sueltan nada; matarlos no es una forma de farmear, porque vuelven con el jefe.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Base: Crystalys, con 175 % del casco y 50 % del daño de los láseres; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 448.000 | 672.000 | 896.000 |
| Escudo | 280.000 | 420.000 | 560.000 |
| Daño de los láseres (una salva por segundo) | 5.000 | 7.500 | 10.000 |
| Velocidad | 230 | 230 | 230 |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Créditos | 393.750 | 787.500 | 1.181.250 |
| Thulium | 1.050 | 2.100 | 3.150 |
| Experiencia (XP) | 63.000 | 126.000 | 189.000 |
| Honor | 273 | 546 | 819 |
| Puntos PvE por derribo | 21 | 21 | 21 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Cataclysite | 100 % en cada una de 2 tiradas | 8 |
| Quorvium | 100 % en cada una de 2 tiradas | 6–10 |
| Power Core | 30 % | 1 |
| Ancient Control Unit | 15 % | 1 |
| Dark Matter | 4 % | 1 |
| Ultra Core y Experimental Fusion Core, repartidos a partes iguales | 100 % | 600–1.000 en total |
| Uno de los 4 [cohetes](/wiki/06-Items/Rockets.md) Épicos, elegido al azar | 100 % | 8–15 |

### Crystalys Guard

Base: Crystalys, con 15 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 38.400 | 57.600 | 76.800 |
| Escudo | 24.000 | 36.000 | 48.000 |
| Daño de los láseres (una salva por segundo) | 1.500 | 2.250 | 3.000 |
| Velocidad | 230 | 230 | 230 |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Cura al líder, cada uno, por segundo (solo el casco) | 250 | 375 | 500 |
| Créditos | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experiencia (XP) | 12 | 24 | 36 |
| Honor | 1 | 2 | 3 |
| Puntos PvE por derribo | 6 | 6 | 6 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- crystalys-members:end -->
