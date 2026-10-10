<!-- wiki-i18n source: 1591c57b813b2ba9 -->
<!-- wiki-i18n title: Enjambre Pirate -->
# Enjambre Pirate {#pirate-swarm}

El enjambre Pirate es un **Pirate Boss** con sus **Pirate Scouts**: una nave enorme y lenta que no ataca a nadie y responde con cohetes, y una manada de naves más rápidas que lo protegen y lo curan. Vive en los sectores entre la base de una corporación y su frontera, donde se juegan los niveles medios del juego, y es un combate largo para un grupo de pilotos, no un derribo rápido.

## De un vistazo {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores `x-2` y `x-3` de cada corporación
- **Cuántos**: Uno en cada uno de esos sectores, 6 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio
- **Líder**: Pirate Boss
- **Seguidores**: Hasta 5 × Pirate Scout, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 900 unidades del líder
- **Curación**: Cada Pirate Scout a menos de 600 unidades del líder cura su casco, 40 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 1 min después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: 2 min después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- pirate-glance:end -->

## Los miembros {#the-members}

- **Pirate Boss**: una nave basada en la Ironclad, con una parte de su fuerza (las cifras están más abajo). Es pasivo y no dispara **ningún láser**: su única arma es un **cohete recto** ([Cohetes](/wiki/06-Items/Rockets.md); cuál depende del sector, mira la tabla), contra el piloto que lo atacó, y sigue merodeando mientras dispara. Nunca repara su casco por sí solo.
- **Pirate Scout**: una nave basada en la Kitefin, con una parte de su fuerza. Los Scouts atacan a cualquier piloto que se les acerque, se mantienen cerca del jefe, y cada uno que está cerca del jefe cura su casco.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Dispara al jefe, no a los Scouts.** Los Scouts curan al jefe, pero la curación es pequeña comparada con su casco, y llega un Scout nuevo con la frecuencia que indica la lista *De un vistazo*: un grupo que mata primero a los Scouts nunca les saca ventaja, y solo un grupo muy grande puede despejarlos y aun así tarda más en acabar con el jefe que uno que los dejó en paz. Los Scouts te cuestan tiempo, no deciden el combate.
- **Aleja a los Scouts.** Un Scout cura solo mientras está al alcance del jefe, así que un Scout que te sigue fuera de ese alcance no cura nada, y una Ostirion es más rápida que un Scout.
- **No dejes de moverte.** El cohete del jefe es recto y no teledirigido: una nave que no deja de moverse lo esquiva, una que se queda quieta recibe el impacto.
- **Lleva un grupo.** Tres pilotos en Ostirions con munición x2 lo pierden en `x-3` incluso mientras los golpes se reparten; cuatro lo derriban en unos cuatro minutos en Alpha, y tres aún pueden hacerlo en `x-2`, pero por poco. Con munición x4 bastan tres también en `x-3` (unos dos minutos y medio). Cinco lo derriban en unos tres minutos cuando los golpes se reparten y en algo más de cuatro cuando un piloto recibe todo el fuego, y entonces pierden tres naves: un grupo que deja que un piloto reciba todo el fuego necesita cinco. En Beta hacen falta seis pilotos y en Gamma siete, con los golpes repartidos (el jefe es más grande allí y sus Scouts curan más). Una Ostirion sola no puede, y una Paragon sola sí. El jefe responde al primer piloto que lo impactó, así que deja que empiece la nave más resistente, y usa tus habilidades (Emergency Repair, Shield Surge: [Habilidades](/wiki/03-Mechanics/Abilities.md)) en un combate tan largo. Los pilotos que aún son de nivel 2 o 3 son demasiado débiles para él, incluso donde vuelan: mantente lejos hasta que seas más fuerte.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, en el mismo sector.

## Recompensas y botín {#rewards-and-drops}

El Pirate Boss paga por el combate que es: un minuto de combate contra él paga más que un minuto de combate contra un Goombah. La paga se reparte según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja es para el piloto que más daño causó y puede contener una **Reinforced Hull Plate**, cohetes y munición. Su caja vale unos dos quintos de lo que paga el derribo mismo. Los Scouts pagan poco y no sueltan nada.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Base: Ironclad, con 50 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original. Dispara un cohete recto cada 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) en `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) en `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 300.000 | 450.000 | 600.000 |
| Escudo | 50.100 | 75.150 | 100.200 |
| Daño de los láseres (una salva por segundo) | ninguno | ninguno | ninguno |
| Velocidad | 92 | 92 | 92 |
| Alcance de los láseres | – | – | – |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Daño de los cohetes, como máximo | 2.500 (Rivet I) / 5.000 (Rivet II) | 3.750 (Rivet I) / 7.500 (Rivet II) | 5.000 (Rivet I) / 10.000 (Rivet II) |
| Créditos | 145.000 | 290.000 | 435.000 |
| Thulium | 725 | 1.450 | 2.175 |
| Experiencia (XP) | 29.000 | 58.000 | 87.000 |
| Honor | 232 | 464 | 696 |
| Puntos PvE por derribo | 15 | 15 | 15 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto | Probabilidad | Cantidad |
| :--- | ---: | ---: |
| Reinforced Hull Plate | 50 % | 1 |
| Uno de los 8 [cohetes](/wiki/06-Items/Rockets.md) que se compran con créditos, elegido al azar | 100 % | 5–10 |
| Uno de Advanced Plasma y Siphon Battery, elegido al azar | 100 % | 1.000–2.000 |

### Pirate Scout

Base: Kitefin, con 50 % del casco y 113 % del daño de los láseres; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | 12.000 | 18.000 | 24.000 |
| Escudo | 9.818 | 14.727 | 19.636 |
| Daño de los láseres (una salva por segundo) | 221 | 332 | 442 |
| Velocidad | 175 | 175 | 175 |
| Alcance de los láseres | 700 | 700 | 700 |
| Radio de agresión | 700 | 700 | 700 |
| Cura al líder, cada uno, por segundo (solo el casco) | 40 | 60 | 80 |
| Créditos | 1.000 | 2.000 | 3.000 |
| Thulium | 4 | 8 | 12 |
| Experiencia (XP) | 100 | 200 | 300 |
| Honor | 2 | 4 | 6 |
| Puntos PvE por derribo | 4 | 4 | 4 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- pirate-members:end -->
