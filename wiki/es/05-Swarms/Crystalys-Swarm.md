<!-- wiki-i18n source: 2b3edf7bcb1d9673 -->
<!-- wiki-i18n title: Enjambre Crystalys -->
# Enjambre Crystalys {#crystalys-swarm}

El enjambre Crystalys es un **Boss Crystalys** con sus **Crystalys Guards**: el más duro de los alienígenas, el [Crystalys](/wiki/04-Aliens/Crystalys.md), crecido, con guardias que se quedan cerca de él y lo curan. Vive en los [sectores de peligro](/wiki/01-General/Danger-Sectors.md) `DS-1`, `DS-2` y `DS-3`, uno en cada uno, y nunca abandona su sector. Los sectores de peligro son sectores PvP, así que el combate es para un grupo grande de los pilotos más fuertes, y el jefe no es el único peligro allí.

## De un vistazo {#at-a-glance}

<!-- crystalys-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores de peligro `DS-1`, `DS-2`, `DS-3`
- **Cuántos**: Uno en cada uno de esos sectores, 3 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio (Beta y Gamma: desde el día 1 de la temporada)
- **Líder**: Boss Crystalys
- **Seguidores**: Hasta 3 × Crystalys Guard, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 500 unidades del líder
- **Curación**: Cada Crystalys Guard a menos de 600 unidades del líder cura su casco, 250 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 30 s después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: {{guide:vitals.respawn@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- crystalys-glance:end -->

## Los miembros {#the-members}

- **Boss Crystalys**: un Crystalys más grande, con el tinte del enjambre y su nombre encima, con casco, escudo y una andanada láser propios (las cifras están más abajo). Es pasivo: merodea hasta que un piloto lo impacta, entonces va tras ese piloto y le dispara, y las naves de su enjambre cercanas se suman al combate. El alcance de su arma y su velocidad son los de un Crystalys, y nunca repara su casco por sí solo. Sus [tres pasos](#the-leaders-three-steps) y una [habilidad especial](/wiki/03-Mechanics/Special-Abilities.md) pueden cambiar eso.
- **Crystalys Guard**: un Crystalys más pequeño con el tinte del enjambre. Los Guards se mantienen cerca del jefe, se suman al combate cuando una nave de enjambre cercana es impactada, y cada uno que está cerca del jefe cura su casco. Un Guard repara su propio casco tras un descanso, como hace un Crystalys.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Lleva un grupo grande.** En Alpha bastan seis pilotos de nivel 8 en Paragons con munición x2 si su fuego se reparte entre ellos, nueve si va todo contra un solo piloto; con munición x4 son cinco y seis. Más pilotos terminan el combate antes y pierden menos naves, y un piloto solo es destruido.
- **Dispara al jefe, no a los Guards.** Un Guard cae en segundos, pero llega uno nuevo con la frecuencia que dice la lista *De un vistazo*, y lo que curan los Guards es una parte pequeña de lo que causa un grupo: dejarlos en paz cuesta un poco de tiempo, perseguirlos cuesta más.
- **Beta y Gamma son más duros.** Los enjambres de esos mundos son más fuertes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), así que piden más pilotos o mejor munición.
- **Los sectores de peligro son PvP.** Un rival puede atacar al grupo en mitad del combate y esperar la caja: es del piloto que más daño causó (y de su clan) durante 30 segundos, y después de cualquiera ([Carga](/wiki/03-Mechanics/Cargo.md)). No vayas solo.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, con toda su fuerza, en el mismo sector, y sus Guards llegan uno tras otro.

## Los tres pasos del líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Su combate tiene tres pasos ([cómo funcionan](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uno ocurre una vez.

- **Al empezar**: Recibe 50 % de cada impacto durante 8 s.
- **Por debajo de dos tercios**: Un anillo de 700 unidades golpea a cada nave que hay dentro con 4 de sus andanadas, y dispara 4 cohetes.
- **Por debajo de un tercio**: Repara 20 % de su casco y su escudo (una ráfaga de daño la interrumpe), y llegan 3 Crystalys Guards más, como máximo 6 vivos.

<!-- mob-ladder:end -->

## Recompensas y botín {#rewards-and-drops}

El Boss Crystalys paga por el combate que es: un minuto de combate contra él paga más que un minuto contra un Crystalys, el alienígena mejor pagado. La paga se reparte según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja es para el piloto que más daño causó y contiene Cataclysite y Quorvium, de vez en cuando un Power Core, una Ancient Control Unit o Dark Matter, munición x3 y x4 y cohetes Épicos. Los Guards pagan poco y no sueltan nada; matarlos no es una forma de farmear, porque vuelven con el jefe.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- crystalys-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Boss Crystalys

Base: Crystalys, con 350 % del casco y 100 % del daño de los láseres; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Boss Crystalys#1}} | {{guide:vitals.hull@Boss Crystalys#2}} | {{guide:vitals.hull@Boss Crystalys#3}} |
| Escudo | {{guide:vitals.shield@Boss Crystalys#1}} | {{guide:vitals.shield@Boss Crystalys#2}} | {{guide:vitals.shield@Boss Crystalys#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Boss Crystalys#1}} | {{guide:vitals.dps@Boss Crystalys#2}} | {{guide:vitals.dps@Boss Crystalys#3}} |
| Velocidad | {{guide:vitals.speed@Boss Crystalys#1}} | {{guide:vitals.speed@Boss Crystalys#2}} | {{guide:vitals.speed@Boss Crystalys#3}} |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Créditos | {{guide:spoils.pay.credits@Boss Crystalys#1}} | {{guide:spoils.pay.credits@Boss Crystalys#2}} | {{guide:spoils.pay.credits@Boss Crystalys#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Crystalys#1}} | {{guide:spoils.pay.thulium@Boss Crystalys#2}} | {{guide:spoils.pay.thulium@Boss Crystalys#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Boss Crystalys#1}} | {{guide:spoils.pay.experience@Boss Crystalys#2}} | {{guide:spoils.pay.experience@Boss Crystalys#3}} |
| Honor | {{guide:spoils.pay.honor@Boss Crystalys#1}} | {{guide:spoils.pay.honor@Boss Crystalys#2}} | {{guide:spoils.pay.honor@Boss Crystalys#3}} |
| Puntos PvE por derribo | 30 | 30 | 30 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@Boss Crystalys#1;Boss Crystalys#2;Boss Crystalys#3}} |

### Crystalys Guard

Base: Crystalys, con 15 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Crystalys Guard#1}} | {{guide:vitals.hull@Crystalys Guard#2}} | {{guide:vitals.hull@Crystalys Guard#3}} |
| Escudo | {{guide:vitals.shield@Crystalys Guard#1}} | {{guide:vitals.shield@Crystalys Guard#2}} | {{guide:vitals.shield@Crystalys Guard#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Crystalys Guard#1}} | {{guide:vitals.dps@Crystalys Guard#2}} | {{guide:vitals.dps@Crystalys Guard#3}} |
| Velocidad | {{guide:vitals.speed@Crystalys Guard#1}} | {{guide:vitals.speed@Crystalys Guard#2}} | {{guide:vitals.speed@Crystalys Guard#3}} |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Cura al líder, cada uno, por segundo (solo el casco) | 250 | 375 | 500 |
| Créditos | {{guide:spoils.pay.credits@Crystalys Guard#1}} | {{guide:spoils.pay.credits@Crystalys Guard#2}} | {{guide:spoils.pay.credits@Crystalys Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Crystalys Guard#1}} | {{guide:spoils.pay.thulium@Crystalys Guard#2}} | {{guide:spoils.pay.thulium@Crystalys Guard#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Crystalys Guard#1}} | {{guide:spoils.pay.experience@Crystalys Guard#2}} | {{guide:spoils.pay.experience@Crystalys Guard#3}} |
| Honor | {{guide:spoils.pay.honor@Crystalys Guard#1}} | {{guide:spoils.pay.honor@Crystalys Guard#2}} | {{guide:spoils.pay.honor@Crystalys Guard#3}} |
| Puntos PvE por derribo | 6 | 6 | 6 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- crystalys-members:end -->
