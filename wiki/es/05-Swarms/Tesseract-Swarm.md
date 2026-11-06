<!-- wiki-i18n source: 554085379d2ae5df -->
<!-- wiki-i18n title: Enjambre Tesseract -->
# Enjambre Tesseract {#tesseract-swarm}

El enjambre Tesseract es una única nave nodriza enorme, el **Tesseract**, y los **Facets** que suelta mientras lo impactan. El Tesseract vive en un lugar fijo del [sector de peligro](/wiki/01-General/Danger-Sectors.md) `DS-4`, no tiene arma propia y nunca abandona su sector. Está hecho para un grupo muy grande de los pilotos más fuertes: su casco y su escudo superan con mucho a un Crystalys, y se repara solo en cuanto lo dejan en paz. Los sectores de peligro son sectores PvP, así que el combate puede atraer a rivales además de a los Facets.

## De un vistazo {#at-a-glance}

<!-- tesseract-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: El sector de peligro `DS-4`
- **Cuántos**: Uno en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio (Beta y Gamma: desde el día 1 de la temporada)
- **Líder**: Tesseract
- **Hogar**: A no más de 2.500 unidades del punto 27.000, 5.000 del mapa del sector
- **Regeneración**: 125.000 HP por segundo en Alpha, primero el casco y luego el escudo, cuando han pasado 5 s sin recibir daño
- **Seguidores**: Hasta 100 × Facet, 20 más cada 5 s mientras el líder recibe impactos
- **Llegada de los seguidores**: Solo mientras el líder ha recibido impactos en los últimos 5 s, a menos de 400 unidades de él
- **Cazadores**: Cada Facet vuela tramos propios alrededor del líder, a menos de 1.800 unidades de él, y no persigue a nadie. Dispara al piloto más cercano que haya impactado al líder cuando ese piloto está a su alcance. Si no tiene a quién disparar, sigue volando alrededor del líder y se va 20 s después del último impacto
- **Líder destruido**: Los seguidores se van 1 min después de que destruyan al líder, estén atacando o no
- **Vuelve**: 30 min después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- tesseract-glance:end -->

## Los miembros {#the-members}

- **Tesseract**: una nave nodriza en forma de cubo, muchas veces más grande que un Crystalys, de hierro forjado oscuro con vetas de brasa incandescentes y su nombre encima. Una bahía de su pared frontal se abre mientras lo impactan, y un cubo luminoso gira dentro de una jaula sobre su techo. Es pasivo: se desplaza despacio dentro de su zona mientras nadie lo daña, y en cuanto un piloto lo impacta, se detiene y mantiene su posición. No dispara nada y no persigue a nadie; su defensa es su tamaño, su reparación y los Facets que suelta.
- **Facet**: una nave pequeña y rápida del mismo hierro oscuro, con bordes incandescentes, una lente iluminada en la proa y dos placas de ala flotantes. Solo existe mientras impactan al Tesseract. No persigue a nadie: se queda junto al Tesseract, vuela tramos cortos propios hacia lugares al azar a su alrededor y dispara al piloto más cercano que haya impactado al Tesseract en cuanto hay uno a su alcance. Se va cuando dejan en paz al Tesseract. Es más rápido que cualquier nave, así que huir del enjambre no sirve, pero un piloto que se mantiene lejos del Tesseract nunca recibe sus disparos.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Lleva un grupo muy grande y golpead a la vez.** El casco y el escudo del Tesseract son una reserva de millones de puntos, así que el combate dura mucho incluso para un grupo grande de naves fuertes, y la paga se reparte según el daño: cuenta cada piloto presente.
- **No lo dejes nunca en paz.** Cuando nadie lo ha dañado durante el tiempo de la lista *De un vistazo*, repara su casco y luego su escudo a esa velocidad, así que una pausa de unos segundos puede deshacer un largo minuto de trabajo. Un Tesseract que se ha reparado por completo olvida quién lo dañó: la paga y la caja dependen del daño del combate que lo destruye.
- **Cada impacto llama a los Facets.** Mientras impactan al Tesseract, cada pocos segundos llega cerca de él un grupo de Facets, hasta el tope de la lista *De un vistazo*. Si nadie lo impacta, no llega ninguno, y los que ya están esperan y se van.
- **Los Facets vuelan alrededor del Tesseract y disparan a quien tengan al alcance.** No van tras el que más daño causa ni tras ningún piloto en particular: cada Facet vuela sus propios tramos cortos hacia lugares al azar de un anillo amplio alrededor del Tesseract, en todas las direcciones, y en cuanto un piloto que ha impactado al Tesseract está a su alcance, dispara al más cercano de ellos. Un grupo que se mantiene unido está al alcance de menos Facets a la vez y reparte su fuego entre todos, a diferencia de un grupo repartido alrededor del Tesseract. Un Facet tiene poco casco y poco escudo, y derribar uno no paga nada, pero le quita una salva a los pilotos que tiene cerca. Un piloto que no ha impactado al Tesseract no es su objetivo.
- **A quien se mantiene lo bastante lejos lo dejan en paz.** Los Facets nunca se alejan del Tesseract más que la distancia de la lista *De un vistazo*; un piloto que se queda más allá de esa distancia y del alcance del láser de un Facet no recibe disparos, por mucho daño que haya causado. Un Facet sin nadie a quien disparar sigue volando alrededor del Tesseract y se va cuando dejan en paz al Tesseract.
- **Beta y Gamma son más duros.** Los enjambres de esos mundos son más fuertes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), y lo mismo la reparación del Tesseract y la salva de cada Facet.
- **Los sectores de peligro son PvP.** Un rival puede atacar al grupo en mitad del combate y esperar la caja: es del piloto que más daño causó (y de su clan) durante 30 segundos, y después de cualquiera ([Carga](/wiki/03-Mechanics/Cargo.md)). No vayas solo.
- **El Tesseract vuelve** pasado el tiempo de la lista *De un vistazo*, con toda su fuerza, en su lugar fijo.

## Recompensas y botín {#rewards-and-drops}

El Tesseract paga por el combate que es: tanto como muchos Crystalys juntos, y más por el daño que aguanta que un Crystalys, el alienígena mejor pagado. La paga se reparte según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja es para el piloto que más daño causó y contiene Power Cores y Ancient Control Units, y de vez en cuando Dark Matter. Las placas de casco no están en esa caja: cada piloto al que paga el derribo recibe su propia [caja privada](/wiki/03-Mechanics/Cargo.md#private-boxes) de placas, que solo él ve y puede recoger, durante 10 minutos. Se tira para su parte del daño, como el botín de un [Clan Warden](/wiki/03-Mechanics/Clans.md#warden-pay-and-loot): quien causó un quinto del daño recibe cerca de un quinto de las cantidades de la tabla, y en un grupo cada piloto recibe su parte de la del grupo, como se reparte la paga. Los Facets no pagan nada, no sueltan nada y no suman puntos PvE: matarlos no es una forma de farmear.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- tesseract-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Tesseract

Base: Crystalys, con 625 % del casco; no tiene arma, y su escudo y su velocidad son propios.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 1.600.000 | 2.400.000 | 3.200.000 |
| Escudo | 1.200.000 | 1.800.000 | 2.400.000 |
| Daño de los láseres (una salva por segundo) | ninguno | ninguno | ninguno |
| Velocidad | 30 | 30 | 30 |
| Alcance de los láseres | – | – | – |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Se repara, por segundo, tras 5 s sin daño (primero el casco, luego el escudo) | 125.000 | 187.500 | 250.000 |
| Créditos | 900.000 | 1.800.000 | 2.700.000 |
| Thulium | 2.400 | 4.800 | 7.200 |
| Experiencia (XP) | 144.000 | 288.000 | 432.000 |
| Honor | 624 | 1.248 | 1.872 |
| Puntos PvE por derribo | 42 | 42 | 42 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Power Core | 70 % | 1–2 |
| Ancient Control Unit | 35 % | 1 |
| Dark Matter | 2,5 % | 1 |

**Botín para cada piloto al que paga el derribo**: una caja más para cada uno, solo para él, con su parte de estas cantidades.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 100 % | 1–2 |
| Velkonite Reinforced Plate | 60 % | 3–6 |
| Orvium Reinforced Plate | 40 % | 1–2 |

### Facet

Base: Seeker, con 2.500 % del casco y 309 % del daño de los láseres; el escudo, la velocidad y el alcance son propios.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 20.000 | 30.000 | 40.000 |
| Escudo | 16.000 | 24.000 | 32.000 |
| Daño de los láseres (una salva por segundo) | 556 | 834 | 1.112 |
| Velocidad | 750 | 750 | 750 |
| Alcance de los láseres | 600 | 600 | 600 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Créditos | 0 | 0 | 0 |
| Thulium | 0 | 0 | 0 |
| Experiencia (XP) | 0 | 0 | 0 |
| Honor | 0 | 0 | 0 |
| Puntos PvE por derribo | 0 | 0 | 0 |

**Botín**: ninguno. El derribo no paga nada.

<!-- tesseract-members:end -->
