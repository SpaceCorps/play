<!-- wiki-i18n source: 38ffa8ba7cbf5000 -->
<!-- wiki-i18n title: Enjambre Goombah -->
# Enjambre Goombah {#goombah-swarm}

El enjambre Goombah es un **Boss Goombah** con sus **Goombah Guards**: un [Goombah](/wiki/04-Aliens/Goombah.md) gigantesco que nunca empieza un combate, y otros más pequeños que se quedan cerca de él y lo curan. Vive en los mismos sectores que el [enjambre Phantasm](/wiki/05-Swarms/Phantasm-Swarm.md), `x-3` y `x-4`, y es un combate para un grupo de los pilotos más fuertes de los sectores de las corporaciones.

## De un vistazo {#at-a-glance}

<!-- goombah-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores `x-3` y `x-4` de cada corporación
- **Cuántos**: Uno en cada uno de esos sectores, 6 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio (Beta y Gamma: desde el día 1 de la temporada)
- **Líder**: Boss Goombah
- **Seguidores**: Hasta 4 × Goombah Guard, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 500 unidades del líder
- **Curación**: Cada Goombah Guard a menos de 600 unidades del líder cura su casco, 110 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 30 s después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: {{guide:vitals.respawn@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- goombah-glance:end -->

## Los miembros {#the-members}

- **Boss Goombah**: un Goombah más grande, con el tinte del enjambre y su nombre encima, con casco, escudo y una andanada láser propios (las cifras están más abajo). Es pasivo: merodea hasta que un piloto lo impacta, entonces va tras ese piloto y le dispara, y las naves de su enjambre cercanas se suman al combate. El alcance de su arma y su velocidad son los de un Goombah, y nunca repara su casco por sí solo. Sus [tres pasos](#the-leaders-three-steps) y una [habilidad especial](/wiki/03-Mechanics/Special-Abilities.md) pueden cambiar eso.
- **Goombah Guard**: un Goombah más pequeño con el tinte del enjambre. Los Guards se mantienen cerca del jefe, se suman al combate cuando una nave de enjambre cercana es impactada, y cada uno que está cerca del jefe cura su casco. Un Guard repara su propio casco tras un descanso, como hace un Goombah.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Lleva un grupo de las naves más fuertes.** Tres pilotos de nivel 8 con munición x2 lo destruyen en unos 75 segundos en Alpha, perdiendo como mucho una nave; dos de ellos necesitan munición x4, y los pilotos de niveles más bajos no causan daño suficiente para ganar.
- **Dispara al jefe, no a los Guards.** Un Guard cae en segundos, pero llega uno nuevo con la frecuencia que dice la lista *De un vistazo*, y lo que curan los Guards es una parte pequeña de lo que causa un grupo: dejarlos en paz cuesta un poco de tiempo, perseguirlos cuesta más.
- **Beta y Gamma son más duros.** Los enjambres de esos mundos son más fuertes ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)), así que piden más pilotos o mejor munición.
- **Vigila el sector.** `x-4` es un sector PvP en Alpha, y `x-3` y `x-4` lo son en Beta y Gamma ([Mundos](/wiki/03-Mechanics/Wipe-Timeline.md#worlds-alpha-beta-and-gamma)): un rival puede unirse al combate o esperar la caja. Deja una nave del grupo de guardia.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, con toda su fuerza, en el mismo sector, y sus Guards llegan uno tras otro.

## Los tres pasos del líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Su combate tiene tres pasos ([cómo funcionan](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uno ocurre una vez.

- **Al empezar**: Recibe 50 % de cada impacto durante 6 s.
- **Por debajo de dos tercios**: Su daño se multiplica por ×1,5 y su velocidad por ×1,25 durante 10 s.
- **Por debajo de un tercio**: Repara 25 % de su casco y su escudo (una ráfaga de daño la interrumpe), y sus Goombah Guards lo reparan ×2 más rápido entretanto.

<!-- mob-ladder:end -->

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
| Casco | {{guide:vitals.hull@Boss Goombah#1}} | {{guide:vitals.hull@Boss Goombah#2}} | {{guide:vitals.hull@Boss Goombah#3}} |
| Escudo | {{guide:vitals.shield@Boss Goombah#1}} | {{guide:vitals.shield@Boss Goombah#2}} | {{guide:vitals.shield@Boss Goombah#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Boss Goombah#1}} | {{guide:vitals.dps@Boss Goombah#2}} | {{guide:vitals.dps@Boss Goombah#3}} |
| Velocidad | {{guide:vitals.speed@Boss Goombah#1}} | {{guide:vitals.speed@Boss Goombah#2}} | {{guide:vitals.speed@Boss Goombah#3}} |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Créditos | {{guide:spoils.pay.credits@Boss Goombah#1}} | {{guide:spoils.pay.credits@Boss Goombah#2}} | {{guide:spoils.pay.credits@Boss Goombah#3}} |
| Thulium | {{guide:spoils.pay.thulium@Boss Goombah#1}} | {{guide:spoils.pay.thulium@Boss Goombah#2}} | {{guide:spoils.pay.thulium@Boss Goombah#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Boss Goombah#1}} | {{guide:spoils.pay.experience@Boss Goombah#2}} | {{guide:spoils.pay.experience@Boss Goombah#3}} |
| Honor | {{guide:spoils.pay.honor@Boss Goombah#1}} | {{guide:spoils.pay.honor@Boss Goombah#2}} | {{guide:spoils.pay.honor@Boss Goombah#3}} |
| Puntos PvE por derribo | 14 | 14 | 14 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@Boss Goombah#1;Boss Goombah#2;Boss Goombah#3}} |

### Goombah Guard

Base: Goombah, con 20 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Goombah Guard#1}} | {{guide:vitals.hull@Goombah Guard#2}} | {{guide:vitals.hull@Goombah Guard#3}} |
| Escudo | {{guide:vitals.shield@Goombah Guard#1}} | {{guide:vitals.shield@Goombah Guard#2}} | {{guide:vitals.shield@Goombah Guard#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Goombah Guard#1}} | {{guide:vitals.dps@Goombah Guard#2}} | {{guide:vitals.dps@Goombah Guard#3}} |
| Velocidad | {{guide:vitals.speed@Goombah Guard#1}} | {{guide:vitals.speed@Goombah Guard#2}} | {{guide:vitals.speed@Goombah Guard#3}} |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Cura al líder, cada uno, por segundo (solo el casco) | 110 | 165 | 220 |
| Créditos | {{guide:spoils.pay.credits@Goombah Guard#1}} | {{guide:spoils.pay.credits@Goombah Guard#2}} | {{guide:spoils.pay.credits@Goombah Guard#3}} |
| Thulium | {{guide:spoils.pay.thulium@Goombah Guard#1}} | {{guide:spoils.pay.thulium@Goombah Guard#2}} | {{guide:spoils.pay.thulium@Goombah Guard#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Goombah Guard#1}} | {{guide:spoils.pay.experience@Goombah Guard#2}} | {{guide:spoils.pay.experience@Goombah Guard#3}} |
| Honor | {{guide:spoils.pay.honor@Goombah Guard#1}} | {{guide:spoils.pay.honor@Goombah Guard#2}} | {{guide:spoils.pay.honor@Goombah Guard#3}} |
| Puntos PvE por derribo | 3 | 3 | 3 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- goombah-members:end -->
