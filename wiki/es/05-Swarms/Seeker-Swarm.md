<!-- wiki-i18n source: 0ed9858d316d7ddd -->
<!-- wiki-i18n title: Enjambre Seeker -->
# Enjambre Seeker {#seeker-swarm}

El enjambre Seeker es el más pequeño de los [enjambres](/wiki/05-Swarms/Swarms.md): un **Boss Seeker** y los **Seeker Slaves** que lo protegen y lo curan. Vive en los sectores donde los pilotos nuevos empiezan a volar, así que es el primer enjambre que encuentran la mayoría. El Boss Seeker nunca empieza un combate, pero en cuanto le disparas es mucho más peligroso que el [Seeker](/wiki/04-Aliens/Seeker.md) en el que se basa.

## De un vistazo {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores `x-1` y `x-2` de cada corporación
- **Cuántos**: Uno en cada uno de esos sectores, 6 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio
- **Líder**: Boss Seeker
- **Seguidores**: Hasta 4 × Seeker Slave, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 500 unidades del líder
- **Curación**: Cada Seeker Slave a menos de 600 unidades del líder cura su casco, 50 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 30 s después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: 2 min después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- seeker-glance:end -->

## Los miembros {#the-members}

- **Boss Seeker**: un Seeker mucho más grande, con el tinte del enjambre y su nombre encima, con muchas veces el casco, el escudo y el daño de un Seeker (las cifras están más abajo). Es pasivo: merodea hasta que un piloto lo impacta, entonces se detiene donde está y dispara a ese piloto, y las naves de su enjambre cercanas se suman al combate. El alcance de su arma y su velocidad son los de un Seeker, y nunca repara su casco por sí solo.
- **Seeker Slave**: un Seeker corriente con el tinte del enjambre. Los Slaves se mantienen cerca del jefe, se suman al combate cuando una nave de enjambre cercana es impactada, y cada uno que está cerca del jefe cura su casco. Un Slave repara su propio casco tras un descanso, como hace un Seeker.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Déjalo en paz hasta que tu nave pueda con él.** Un Boss Seeker golpea más fuerte de lo que aguanta la primera nave de cualquier piloto: la Protos de un piloto nuevo, todavía sin escudo, es destruida en segundos en cuanto el jefe y sus Slaves se le echan encima.
- **Mantente fuera de su alcance.** El jefe y sus Slaves son más lentos que una Protos, y sus armas llegan menos lejos que un Quantum Laser 2 (consulta [Láseres y munición](/wiki/06-Items/Lasers.md)): un piloto que tiene esos láseres y se mantiene más allá de su alcance no recibe daño mientras disparan. Un piloto con Quantum Laser 1 no puede mantenerse fuera de su alcance.
- **Los Slaves curan más rápido de lo que golpea un piloto nuevo en solitario.** Juntos curan más de lo que causan los láseres de un piloto con munición x1, así que lleva un compañero y munición x2. Dos pilotos con Quantum Laser 2 que mantienen la distancia derriban al jefe en aproximadamente un minuto en Alpha, y mucho más rápido con munición x2.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, con toda su fuerza, en el mismo sector, y sus Slaves llegan uno tras otro.

## Recompensas y botín {#rewards-and-drops}

El Boss Seeker paga **exactamente diez Seekers**: diez veces los créditos, el Thulium, la XP y el honor de un Seeker, repartidos según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja contiene el botín de diez Seekers y, además, munición y cohetes por debajo de Épico, para el piloto que más daño causó. Los Slaves pagan poco y no sueltan nada; derribarlos no es una forma de farmear, porque vuelven con el jefe.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Base: Seeker, con 400 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 3.200 | 4.800 | 6.400 |
| Escudo | 3.200 | 4.800 | 6.400 |
| Daño de los láseres (una salva por segundo) | 720 | 1.080 | 1.440 |
| Velocidad | 120 | 120 | 120 |
| Alcance de los láseres | 600 | 600 | 600 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Créditos | 10.000 | 20.000 | 30.000 |
| Thulium | 40 | 80 | 120 |
| Experiencia (XP) | 1.000 | 2.000 | 3.000 |
| Honor | 20 | 40 | 60 |
| Puntos PvE por derribo | 5 | 5 | 5 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Ship Fragment | 20 % en cada una de 10 tiradas | 1 |
| Daraxium | 50 % en cada una de 10 tiradas | 1–2 |
| Standard Battery | 100 % | 200–400 |
| Advanced Plasma | 100 % | 10–20 |
| Ultra Core | 100 % | 2–4 |
| Uno de los 8 [cohetes](/wiki/06-Items/Rockets.md) que se compran con créditos, elegido al azar | 100 % | 2–3 |

### Seeker Slave

Base: Seeker, con 100 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 800 | 1.200 | 1.600 |
| Escudo | 800 | 1.200 | 1.600 |
| Daño de los láseres (una salva por segundo) | 180 | 270 | 360 |
| Velocidad | 120 | 120 | 120 |
| Alcance de los láseres | 600 | 600 | 600 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Cura al líder, cada uno, por segundo (solo el casco) | 50 | 75 | 100 |
| Créditos | 125 | 250 | 375 |
| Thulium | 1 | 2 | 3 |
| Experiencia (XP) | 12 | 24 | 36 |
| Honor | 1 | 2 | 3 |
| Puntos PvE por derribo | 1 | 1 | 1 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- seeker-members:end -->
