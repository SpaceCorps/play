<!-- wiki-i18n source: 7c6bc3eaf70223f5 -->
<!-- wiki-i18n title: Enjambre Seeker -->
# Enjambre Seeker {#seeker-swarm}

El enjambre Seeker es el más pequeño de los [enjambres](/wiki/05-Swarms/Swarms.md): un **Boss Seeker** y los **Seeker Slaves** que lo protegen y lo curan. Vive en los sectores donde los pilotos nuevos empiezan a volar, así que es el primer enjambre que encuentran la mayoría. El Boss Seeker nunca empieza un combate, pero en cuanto le disparas es mucho más peligroso que el [Seeker](/wiki/04-Aliens/Seeker.md) en el que se basa.

## De un vistazo {#at-a-glance}

<!-- seeker-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores `x-1` y `x-2` de cada corporación
- **Cuántos**: Uno en cada uno de esos sectores, 6 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio (Beta y Gamma: desde el día 1 de la temporada)
- **Líder**: Boss Seeker
- **Seguidores**: Hasta 4 × Seeker Slave, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 500 unidades del líder
- **Curación**: Cada Seeker Slave a menos de 600 unidades del líder cura su casco, 50 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 30 s después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: {{guide:vitals.respawn@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- seeker-glance:end -->

## Los miembros {#the-members}

- **Boss Seeker**: un Seeker mucho más grande, con el tinte del enjambre y su nombre encima, con muchas veces el casco, el escudo y el daño de un Seeker (las cifras están más abajo). Es pasivo: merodea hasta que un piloto lo impacta, entonces se detiene donde está y dispara a ese piloto, y las naves de su enjambre cercanas se suman al combate. El alcance de su arma y su velocidad son los de un Seeker, y nunca repara su casco por sí solo. Sus [tres pasos](#the-leaders-three-steps) y una [habilidad especial](/wiki/03-Mechanics/Special-Abilities.md) pueden cambiar eso.
- **Seeker Slave**: un Seeker corriente con el tinte del enjambre. Los Slaves se mantienen cerca del jefe, se suman al combate cuando una nave de enjambre cercana es impactada, y cada uno que está cerca del jefe cura su casco. Un Slave repara su propio casco tras un descanso, como hace un Seeker.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Déjalo en paz hasta que tu nave pueda con él.** Un Boss Seeker golpea más fuerte de lo que aguanta la primera nave de cualquier piloto: la Protos de un piloto nuevo, todavía sin escudo, es destruida en segundos en cuanto el jefe y sus Slaves se le echan encima.
- **Mantente fuera de su alcance.** El jefe y sus Slaves son más lentos que una Protos, y sus armas llegan menos lejos que un Quantum Laser II (consulta [Láseres y munición](/wiki/06-Items/Lasers.md)): un piloto que tiene esos láseres y se mantiene más allá de su alcance no recibe daño mientras disparan. Un piloto con Quantum Laser I no puede mantenerse fuera de su alcance.
- **Los Slaves curan más rápido de lo que golpea un piloto nuevo en solitario.** Juntos curan más de lo que causan los láseres de un piloto con munición x1, así que lleva un compañero y munición x2. Dos pilotos con Quantum Laser II que mantienen la distancia derriban al jefe en aproximadamente un minuto en Alpha, y mucho más rápido con munición x2.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, con toda su fuerza, en el mismo sector, y sus Slaves llegan uno tras otro.

## Los tres pasos del líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Su combate tiene tres pasos ([cómo funcionan](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uno ocurre una vez.

- **Al empezar**: Sus Seeker Slaves lo reparan ×2 más rápido durante 8 s.
- **Por debajo de dos tercios**: 2 copias suyas aparecen, y la auténtica lleva un anillo.
- **Por debajo de un tercio**: Huye de los pilotos durante 4 s y luego se vuelve contra ellos.

<!-- mob-ladder:end -->

## Recompensas y botín {#rewards-and-drops}

El Boss Seeker paga **exactamente diez Seekers**: diez veces los créditos, el Thulium, la XP y el honor de un Seeker, repartidos según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja contiene el botín de diez Seekers y, además, munición y cohetes por debajo de Épico, para el piloto que más daño causó. Los Slaves pagan poco y no sueltan nada; derribarlos no es una forma de farmear, porque vuelven con el jefe.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- seeker-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Seeker

Base: Seeker, con 400 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Boss Seeker#1}} | {{guide:vitals.hull@Boss Seeker#2}} | {{guide:vitals.hull@Boss Seeker#3}} |
| Escudo | {{guide:vitals.shield@Boss Seeker#1}} | {{guide:vitals.shield@Boss Seeker#2}} | {{guide:vitals.shield@Boss Seeker#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Boss Seeker#1}} | {{guide:vitals.dps@Boss Seeker#2}} | {{guide:vitals.dps@Boss Seeker#3}} |
| Velocidad | {{guide:vitals.speed@Boss Seeker#1}} | {{guide:vitals.speed@Boss Seeker#2}} | {{guide:vitals.speed@Boss Seeker#3}} |
| Alcance de los láseres | 600 | 600 | 600 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Créditos | {{guide:spoils.pay.credits@Boss Seeker#1}} | {{guide:spoils.pay.credits@Boss Seeker#2}} | {{guide:spoils.pay.credits@Boss Seeker#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Seeker#1}} | {{guide:spoils.pay.thulium@Boss Seeker#2}} | {{guide:spoils.pay.thulium@Boss Seeker#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Boss Seeker#1}} | {{guide:spoils.pay.experience@Boss Seeker#2}} | {{guide:spoils.pay.experience@Boss Seeker#3}} |
| Honor | {{guide:spoils.pay.honor@Boss Seeker#1}} | {{guide:spoils.pay.honor@Boss Seeker#2}} | {{guide:spoils.pay.honor@Boss Seeker#3}} |
| Puntos PvE por derribo | 5 | 5 | 5 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@Boss Seeker#1;Boss Seeker#2;Boss Seeker#3}} |

### Seeker Slave

Base: Seeker, con 100 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Seeker Slave#1}} | {{guide:vitals.hull@Seeker Slave#2}} | {{guide:vitals.hull@Seeker Slave#3}} |
| Escudo | {{guide:vitals.shield@Seeker Slave#1}} | {{guide:vitals.shield@Seeker Slave#2}} | {{guide:vitals.shield@Seeker Slave#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Seeker Slave#1}} | {{guide:vitals.dps@Seeker Slave#2}} | {{guide:vitals.dps@Seeker Slave#3}} |
| Velocidad | {{guide:vitals.speed@Seeker Slave#1}} | {{guide:vitals.speed@Seeker Slave#2}} | {{guide:vitals.speed@Seeker Slave#3}} |
| Alcance de los láseres | 600 | 600 | 600 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Cura al líder, cada uno, por segundo (solo el casco) | 50 | 75 | 100 |
| Créditos | {{guide:spoils.pay.credits@Seeker Slave#1}} | {{guide:spoils.pay.credits@Seeker Slave#2}} | {{guide:spoils.pay.credits@Seeker Slave#3}} |
| Thulium | {{guide:spoils.pay.thulium@Seeker Slave#1}} | {{guide:spoils.pay.thulium@Seeker Slave#2}} | {{guide:spoils.pay.thulium@Seeker Slave#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Seeker Slave#1}} | {{guide:spoils.pay.experience@Seeker Slave#2}} | {{guide:spoils.pay.experience@Seeker Slave#3}} |
| Honor | {{guide:spoils.pay.honor@Seeker Slave#1}} | {{guide:spoils.pay.honor@Seeker Slave#2}} | {{guide:spoils.pay.honor@Seeker Slave#3}} |
| Puntos PvE por derribo | 1 | 1 | 1 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- seeker-members:end -->
