<!-- wiki-i18n source: fcba1b51b68a9123 -->
<!-- wiki-i18n title: Enjambre Dormant -->
# Enjambre Dormant {#dormant-swarm}

El enjambre Dormant es una **Dormant Force** con sus **Dormant Pulses**: un grupo de naves que nunca empiezan un combate y golpean muy fuerte una vez despiertas. Solo hay uno en los sectores de peligro de cada mundo (el [Deep Void](/wiki/03-Mechanics/Deep-Void.md#the-dormant-swarms-visit) tiene una visita propia, una vez al día). Vaga de un sector de peligro al siguiente, y es el combate más duro y el botín más rico de los enjambres: un combate para un grupo grande de las naves más fuertes. Desde el día 11 de la temporada empieza en el [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) de `DS-4`, vuelve antes y paga el doble (consulta la lista *De un vistazo*).

## De un vistazo {#at-a-glance}

<!-- dormant-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores de peligro `DS-1`, `DS-2`, `DS-3`, `DS-4`, volando de uno a otro
- **Cuántos**: Uno en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio (Beta y Gamma: desde el día 1 de la temporada)
- **Líder**: Dormant Force
- **Seguidores**: 2 × Dormant Pulse, que vuelan con el líder
- **Los seguidores se mantienen**: a no más de 700 unidades del líder
- **Líder destruido**: Dormant Pulse toma el mando
- **Líder destruido**: Los seguidores se van 30 s después de que destruyan al líder, estén atacando o no
- **Desplazamiento**: Permanece 8 a 15 min en un mapa y luego vuela a la puerta de otro sector de peligro. Nunca toma las puertas que salen de los sectores de peligro y nunca entra en el anillo del agujero negro
- **Vuelve**: {{guide:vitals.respawn@Dormant Force#1;Dormant Force#2;Dormant Force#3}} después de que destruyan a todo el enjambre, en un sector de peligro al azar
- **Desde el día 11 de la temporada**: Aparece en el [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md) de `DS-4` en lugar de en un sector de peligro al azar, vuelve 30 min después de que destruyan a todo el enjambre, y cada nave paga ×2 (créditos, Thulium, XP y honor; el botín sigue igual)
- **Avisos**: Se avisa a los pilotos de todo el mundo cuándo aparece el enjambre y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. Una marca lo muestra en los mapas de los sectores de peligro y en el mapa galáctico. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- dormant-glance:end -->

## Los miembros {#the-members}

- **Dormant Force**: una Wraith a plena fuerza, con láseres que golpean tres veces más fuerte que los de un equipamiento típico. Dirige el enjambre, es pasiva hasta que la impactan y dispara **cohetes rectos** contra el primer piloto que la impactó.
- **Dormant Pulse**: una Paragon a plena fuerza, con láseres pesados del mismo tipo, cada uno de los cuales pega el doble de fuerte que uno de los de la Force, y sus propios cohetes. Una Pulse tiene menos láseres que la Force, así que su descarga completa es mayor que la de la Force, no el doble de grande (las cifras están abajo). Las Pulses vuelan cerca de la Force, y cuando la Force es destruida, una de ellas toma el mando.

Son pasivos: nunca van a por un piloto. Si impactas a uno, los demás cercanos se suman al combate contra el primer piloto que lo impactó.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Encuéntralo.** Todo el mundo se entera cuando aparece, y una marca lo muestra en los mapas de los sectores de peligro y en el mapa galáctico. Permanece en un mapa el tiempo de la lista *De un vistazo*, luego vuela a la puerta de otro sector de peligro y salta; nunca toma una puerta que salga de los sectores de peligro y nunca entra en el anillo del agujero negro. Vuela a la velocidad de su nave más lenta, y, como un piloto, no inicia ni termina un salto mientras recibe fuego. Desde el día 11 de la temporada aparece primero justo fuera de la zona del [Dormant Swamp](/wiki/03-Mechanics/Dormant-Swamp.md), donde un grupo puede esperarlo fuera del alcance de los cañones del pantano, y luego sale volando por una puerta de `DS-4`.
- **No se puede derrotar solo, ni con unos pocos.** Ocho pilotos de nivel 8 en Paragons con munición x2 o x4 lo destruyen en aproximadamente un minuto en Alpha, perdiendo como mucho una nave; una Paragon sola es destruida, y también lo son tres o cuatro con munición x2. Los enjambres de Beta y Gamma son más fuertes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), así que esos mundos piden grupos mayores.
- **Sus láseres deciden el combate.** Juntos pueden destruir una Paragon en menos de un minuto, y aun una con los mejores escudos en menos de dos, con cohetes o sin ellos: lleva tu daño rápido, con los mejores escudos que tengas.
- **Nave por nave.** Cada nave tiene su propio casco y su propia paga, así que la Force o una Pulse pueden ser destruidas primero. El enjambre solo se reemplaza cuando está destruido por completo, pasado el tiempo de la lista *De un vistazo*.

## Los tres pasos del líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Su combate tiene tres pasos ([cómo funcionan](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uno ocurre una vez.

- **Al empezar**: Recibe 70 % de cada impacto mientras viva uno de sus Dormant Pulses.
- **Por debajo de dos tercios**: Sus Dormant Pulses disparan un cohete cada 2,5 s durante 15 s.
- **Por debajo de un tercio**: Mientras vivan todos sus Dormant Pulses, lo reparan 5 % de su casco por segundo durante 6 s.

<!-- mob-ladder:end -->

## Recompensas y botín {#rewards-and-drops}

Cada nave paga por separado, según el daño que se le causó ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)), y cada una suelta una caja para el piloto que más daño le causó. La **caja de la Force** es el premio: muchísima munición x3 y x4, cohetes Épicos de una sola clase y, de vez en cuando, un N.I.K.E. o un N.U.K.E. Las **Pulses** pueden soltar una Ancient Control Unit, un Power Core o Dark Matter. Un minuto de combate contra el enjambre paga más que un minuto de combate contra el Crystalys, el alienígena mejor pagado. Desde el día 11 de la temporada cada nave paga el doble (consulta la lista *De un vistazo*); las cajas son las mismas.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)). Los créditos, el Thulium, la XP y el honor de las tablas son la paga anterior al día 11 de la temporada; desde ese día un derribo paga el doble.

<!-- dormant-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Dormant Force

Base: Wraith, con 100 % del casco y 300 % del daño de los láseres; la velocidad y el alcance son los de la nave original. Dispara un cohete recto cada 5 s: [Rivet III](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dormant Force#1}} | {{guide:vitals.hull@Dormant Force#2}} | {{guide:vitals.hull@Dormant Force#3}} |
| Escudo | {{guide:vitals.shield@Dormant Force#1}} | {{guide:vitals.shield@Dormant Force#2}} | {{guide:vitals.shield@Dormant Force#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Dormant Force#1}} | {{guide:vitals.dps@Dormant Force#2}} | {{guide:vitals.dps@Dormant Force#3}} |
| Velocidad | {{guide:vitals.speed@Dormant Force#1}} | {{guide:vitals.speed@Dormant Force#2}} | {{guide:vitals.speed@Dormant Force#3}} |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Daño de los cohetes, como máximo | {{guide:behaviour.ability:rocket.damage@Dormant Force#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Force#3}} |
| Créditos | {{guide:spoils.pay.credits@Dormant Force#1}} | {{guide:spoils.pay.credits@Dormant Force#2}} | {{guide:spoils.pay.credits@Dormant Force#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Force#1}} | {{guide:spoils.pay.thulium@Dormant Force#2}} | {{guide:spoils.pay.thulium@Dormant Force#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Dormant Force#1}} | {{guide:spoils.pay.experience@Dormant Force#2}} | {{guide:spoils.pay.experience@Dormant Force#3}} |
| Honor | {{guide:spoils.pay.honor@Dormant Force#1}} | {{guide:spoils.pay.honor@Dormant Force#2}} | {{guide:spoils.pay.honor@Dormant Force#3}} |
| Puntos PvE por derribo | 25 | 25 | 25 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@Dormant Force#1;Dormant Force#2;Dormant Force#3}} |

### Dormant Pulse

Base: Paragon, con 100 % del casco y 600 % del daño de los láseres; la velocidad y el alcance son los de la nave original. Dispara un cohete recto cada 5 s: [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets).

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dormant Pulse#1}} | {{guide:vitals.hull@Dormant Pulse#2}} | {{guide:vitals.hull@Dormant Pulse#3}} |
| Escudo | {{guide:vitals.shield@Dormant Pulse#1}} | {{guide:vitals.shield@Dormant Pulse#2}} | {{guide:vitals.shield@Dormant Pulse#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Dormant Pulse#1}} | {{guide:vitals.dps@Dormant Pulse#2}} | {{guide:vitals.dps@Dormant Pulse#3}} |
| Velocidad | {{guide:vitals.speed@Dormant Pulse#1}} | {{guide:vitals.speed@Dormant Pulse#2}} | {{guide:vitals.speed@Dormant Pulse#3}} |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Daño de los cohetes, como máximo | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#1}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#2}} | {{guide:behaviour.ability:rocket.damage@Dormant Pulse#3}} |
| Créditos | {{guide:spoils.pay.credits@Dormant Pulse#1}} | {{guide:spoils.pay.credits@Dormant Pulse#2}} | {{guide:spoils.pay.credits@Dormant Pulse#3}} |
| Thulium | {{guide:spoils.pay.thulium@Dormant Pulse#1}} | {{guide:spoils.pay.thulium@Dormant Pulse#2}} | {{guide:spoils.pay.thulium@Dormant Pulse#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Dormant Pulse#1}} | {{guide:spoils.pay.experience@Dormant Pulse#2}} | {{guide:spoils.pay.experience@Dormant Pulse#3}} |
| Honor | {{guide:spoils.pay.honor@Dormant Pulse#1}} | {{guide:spoils.pay.honor@Dormant Pulse#2}} | {{guide:spoils.pay.honor@Dormant Pulse#3}} |
| Puntos PvE por derribo | 11 | 11 | 11 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@Dormant Pulse#1;Dormant Pulse#2;Dormant Pulse#3}} |

<!-- dormant-members:end -->
