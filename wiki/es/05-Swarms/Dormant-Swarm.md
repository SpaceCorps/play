<!-- wiki-i18n source: 4bfb24feda6f6bf5 -->
<!-- wiki-i18n title: Enjambre Dormant -->
# Enjambre Dormant {#dormant-swarm}

El enjambre Dormant es una **Dormant Force** con sus **Dormant Pulses**: un grupo de naves que nunca empiezan un combate y golpean muy fuerte una vez despiertas. Solo hay uno en cada mundo. Vaga de un sector de peligro al siguiente, y es el combate más duro y el botín más rico de los enjambres: un combate para un grupo grande de las naves más fuertes.

## De un vistazo {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores de peligro `DS-1`, `DS-2`, `DS-3`, `DS-4`, volando de uno a otro
- **Cuántos**: Uno en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio
- **Líder**: Dormant Force
- **Seguidores**: 2 × Dormant Pulse, que vuelan con el líder
- **Los seguidores se mantienen**: a no más de 700 unidades del líder
- **Líder destruido**: Dormant Pulse toma el mando
- **Desplazamiento**: Permanece 8 a 15 min en un mapa y luego vuela a la puerta de otro sector de peligro. Nunca toma las puertas que salen de los sectores de peligro y nunca entra en el anillo del agujero negro
- **Vuelve**: 1 h después de que destruyan a todo el enjambre, en un sector de peligro al azar
- **Avisos**: Se avisa a los pilotos de todo el mundo cuándo aparece el enjambre y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. Una marca lo muestra en los mapas de los sectores de peligro y en el mapa galáctico. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- dormant-glance:end -->

## Los miembros {#the-members}

- **Dormant Force**: una Wraith a plena fuerza, con láseres que golpean tres veces más fuerte que los de un equipamiento típico. Dirige el enjambre, es pasiva hasta que la impactan y dispara **cohetes rectos** contra el primer piloto que la impactó.
- **Dormant Pulse**: una Paragon a plena fuerza, con el mismo tipo de láseres pesados y sus propios cohetes. Las Pulses vuelan cerca de la Force, y cuando la Force es destruida, una de ellas toma el mando.

Son pasivos: nunca van a por un piloto. Si impactas a uno, los demás cercanos se suman al combate contra el primer piloto que lo impactó.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Encuéntralo.** Todo el mundo se entera cuando aparece, y una marca lo muestra en los mapas de los sectores de peligro y en el mapa galáctico. Permanece en un mapa el tiempo de la lista *De un vistazo*, luego vuela a la puerta de otro sector de peligro y salta; nunca toma una puerta que salga de los sectores de peligro y nunca entra en el anillo del agujero negro. Vuela a la velocidad de su nave más lenta, y, como un piloto, no inicia ni termina un salto mientras recibe fuego.
- **No se puede derrotar solo, ni con unos pocos.** Ocho pilotos de nivel 8 en Paragons con munición x2 o x4 lo destruyen en aproximadamente un minuto en Alpha, perdiendo como mucho una nave; una Paragon sola es destruida, y también lo son tres con munición x2. Los enjambres de Beta y Gamma son más fuertes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), así que esos mundos piden grupos mayores.
- **Sus láseres deciden el combate.** Juntos pueden destruir una Paragon en menos de un minuto, y aun una con los mejores escudos en menos de dos, con cohetes o sin ellos: lleva tu daño rápido, con los mejores escudos que tengas.
- **Nave por nave.** Cada nave tiene su propio casco y su propia paga, así que la Force o una Pulse pueden ser destruidas primero. El enjambre solo se reemplaza cuando está destruido por completo, pasado el tiempo de la lista *De un vistazo*.

## Recompensas y botín {#rewards-and-drops}

Cada nave paga por separado, según el daño que se le causó ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), y cada una suelta una caja para el piloto que más daño le causó. La **caja de la Force** es el premio: muchísima munición x3 y x4, cohetes Épicos de una sola clase y, de vez en cuando, un N.I.K.E. o un N.U.K.E. Las **Pulses** pueden soltar una Ancient Control Unit, un Power Core o Dark Matter. Un minuto de combate contra el enjambre paga más que un minuto de combate contra el Crystalys, el alienígena mejor pagado.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Base: Wraith, con 100 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original. Dispara un cohete recto cada 5 s: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 324.000 | 486.000 | 648.000 |
| Escudo | 83.400 | 125.100 | 166.800 |
| Daño de los láseres (una salva por segundo) | 2.880 | 4.320 | 5.760 |
| Velocidad | 220 | 220 | 220 |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Daño de los cohetes, como máximo | 7.500 | 11.250 | 15.000 |
| Créditos | 200.000 | 400.000 | 600.000 |
| Thulium | 535 | 1.070 | 1.605 |
| Experiencia (XP) | 32.100 | 64.200 | 96.300 |
| Honor | 139 | 278 | 417 |
| Puntos PvE por derribo | 25 | 25 | 25 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Ultra Core y Experimental Fusion Core, repartidos a partes iguales | 100 % | 2.000–3.000 en total |
| Uno de los 4 [cohetes](/wiki/06-Items/Rockets.md) Épicos, elegido al azar | 100 % | 30–50 |
| Uno de [N.I.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets) y [N.U.K.E.](/wiki/06-Items/Rockets.md#the-craft-only-rockets), elegido al azar | 50 % | 1 |

### Dormant Pulse

Base: Paragon, con 100 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original. Dispara un cohete recto cada 5 s: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 128.000 | 192.000 | 256.000 |
| Escudo | 64.570 | 96.855 | 129.140 |
| Daño de los láseres (una salva por segundo) | 1.920 | 2.880 | 3.840 |
| Velocidad | 210 | 210 | 210 |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Daño de los cohetes, como máximo | 5.000 | 7.500 | 10.000 |
| Créditos | 95.000 | 190.000 | 285.000 |
| Thulium | 255 | 510 | 765 |
| Experiencia (XP) | 15.200 | 30.400 | 45.600 |
| Honor | 66 | 132 | 198 |
| Puntos PvE por derribo | 11 | 11 | 11 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Ancient Control Unit | 20 % | 1 |
| Power Core | 20 % | 1 |
| Dark Matter | 20 % | 1–5 |

<!-- dormant-members:end -->
