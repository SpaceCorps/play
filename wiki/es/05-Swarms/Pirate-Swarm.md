<!-- wiki-i18n source: 33448f95d2520b3a -->
<!-- wiki-i18n title: Enjambre Pirate -->
# Enjambre Pirate {#pirate-swarm}

El enjambre Pirate es un **Pirate Boss** con sus **Pirate Scouts**: una nave enorme y lenta que no ataca a nadie y responde con cohetes, y una manada de naves más rápidas que lo protegen y lo curan. Vive en los sectores entre la base de una corporación y su frontera, donde se juegan los niveles medios del juego, y es un combate largo para un grupo de pilotos, no un derribo rápido.

## De un vistazo {#at-a-glance}

<!-- pirate-glance:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

- **Dónde**: Los sectores `x-2` y `x-3` de cada corporación
- **Cuántos**: Uno en cada uno de esos sectores, 6 en cada mundo
- **Aparece**: Desde el día 4 de la temporada hasta el reinicio (Beta y Gamma: desde el día 1 de la temporada)
- **Líder**: Pirate Boss
- **Seguidores**: Hasta 5 × Pirate Scout, uno nuevo cada 10 s
- **Los seguidores se mantienen**: a no más de 900 unidades del líder
- **Curación**: Cada Pirate Scout a menos de 600 unidades del líder cura su casco, 40 HP por segundo en Alpha
- **Líder destruido**: Los seguidores se van 1 min después de que destruyan al líder, salvo que estén atacando
- **Vuelve**: {{guide:vitals.respawn@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} después de que destruyan al líder, en el mismo sector
- **Avisos**: Se avisa a los pilotos del sector cuándo aparece el líder y cuándo es destruido. Son líneas del Sistema: aparecen en la pestaña **Sistema** del chat, con un contador de no leídas, y no en **Global** ni en **Local**. El registro de bajas nombra al piloto al que se acredita el derribo.

<!-- pirate-glance:end -->

## Los miembros {#the-members}

- **Pirate Boss**: una nave basada en la Ironclad, con una parte de su fuerza (las cifras están más abajo). Es pasivo y no dispara **ningún láser**: su única arma es un **cohete recto** ([Cohetes](/wiki/06-Items/Rockets.md); cuál depende del sector, mira la tabla), contra el piloto que lo atacó, y sigue merodeando mientras dispara. Nunca repara su casco por sí solo. Sus [tres pasos](#the-leaders-three-steps) y una [habilidad especial](/wiki/03-Mechanics/Special-Abilities.md) pueden cambiar eso.
- **Pirate Scout**: una nave basada en la Kitefin, con una parte de su fuerza. Los Scouts atacan a cualquier piloto que se les acerque, se mantienen cerca del jefe, y cada uno que está cerca del jefe cura su casco.

## Cómo transcurre el combate {#how-the-fight-goes}

- **Dispara al jefe, no a los Scouts.** Los Scouts curan al jefe, pero la curación es pequeña comparada con su casco, y llega un Scout nuevo con la frecuencia que indica la lista *De un vistazo*: un grupo que mata primero a los Scouts nunca les saca ventaja, y solo un grupo muy grande puede despejarlos y aun así tarda más en acabar con el jefe que uno que los dejó en paz. Los Scouts te cuestan tiempo, no deciden el combate.
- **Aleja a los Scouts.** Un Scout cura solo mientras está al alcance del jefe, así que un Scout que te sigue fuera de ese alcance no cura nada, y una Ostirion es más rápida que un Scout.
- **No dejes de moverte.** El cohete del jefe es recto y no teledirigido: una nave que no deja de moverse lo esquiva, una que se queda quieta recibe el impacto.
- **Lleva un grupo.** Tres pilotos en Ostirions con munición x2 lo derriban en `x-2` sin perder ninguna nave, aunque por poco, y son destruidos en `x-3`, incluso mientras los golpes se reparten; cuatro lo derriban en unos tres minutos en Alpha. Con munición x4, tres lo derriban en `x-3` en unos dos minutos. Cinco lo derriban en unos dos minutos y medio cuando los golpes se reparten y en unos tres cuando un piloto recibe todo el fuego, y entonces pierden dos naves: un grupo que deja que un piloto reciba todo el fuego necesita cinco. En Beta hacen falta cinco pilotos y en Gamma siete, con los golpes repartidos (el jefe es más grande allí y sus Scouts curan más). En Alpha, en `x-3` y con munición x2, una Ostirion sola no lo consigue, una Paragon sola tampoco lo consigue, y dos Paragons lo consiguen con holgura. En Beta y Gamma, en `x-3`, una Paragon sola es destruida con munición x2 y con munición x4. El jefe responde al primer piloto que lo impactó, así que deja que empiece la nave más resistente, y usa tus habilidades (Emergency Repair, Shield Surge: [Habilidades](/wiki/03-Mechanics/Abilities.md)) en un combate tan largo. Los pilotos que aún son de nivel 2 o 3 son demasiado débiles para él, incluso donde vuelan: mantente lejos hasta que seas más fuerte.
- **El jefe vuelve** pasado el tiempo de la lista *De un vistazo*, en el mismo sector.

## Los tres pasos del líder {#the-leaders-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

Su combate tiene tres pasos ([cómo funcionan](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uno ocurre una vez.

- **Al empezar**: Dispara un abanico de 3 cohetes, separados 12 grados, al primer piloto que lo golpeó.
- **Por debajo de dos tercios**: Llama a 5 Pirate Scouts más de golpe, como máximo 10 vivos. No pagan nada y se van tras 45 s.
- **Por debajo de un tercio**: Vuela a velocidad ×1,8 hacia la puerta más cercana durante 10 s y luego se vuelve contra los pilotos.

<!-- mob-ladder:end -->

## Recompensas y botín {#rewards-and-drops}

El Pirate Boss paga por el combate que es: un minuto de combate contra él paga más que un minuto de combate contra un Goombah. La paga se reparte según el daño entre los pilotos que lo combatieron ([cómo paga el derribo de un jefe](/wiki/05-Swarms/Swarms.md#how-a-boss-kill-pays)). Su caja es para el piloto que más daño causó y puede contener una **Reinforced Hull Plate**, cohetes y munición. Su caja vale un poco menos de la mitad de lo que paga el derribo mismo. Los Scouts pagan poco y no sueltan nada.

## Las cifras {#the-numbers}

Las cifras de las naves del enjambre en los tres mundos ([Mundos](/wiki/05-Swarms/Swarms.md#the-worlds)).

<!-- pirate-members:begin -->
<!-- Generated from server/Resources/Swarms.json (and Rockets.json, Values/ranking-config.json, Data/Seeds/items.json) by scripts/swarms-wiki.sh: don't edit by hand. -->

### Pirate Boss

Base: Ironclad, con 50 % de casco, escudo y daño; la velocidad y el alcance son los de la nave original. Dispara un cohete recto cada 5 s: [Rivet I](/wiki/06-Items/Rockets.md#the-twelve-rockets) en `x-2`, [Rivet II](/wiki/06-Items/Rockets.md#the-twelve-rockets) en `x-3`.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Pirate Boss#1}} | {{guide:vitals.hull@Pirate Boss#2}} | {{guide:vitals.hull@Pirate Boss#3}} |
| Escudo | {{guide:vitals.shield@Pirate Boss#1}} | {{guide:vitals.shield@Pirate Boss#2}} | {{guide:vitals.shield@Pirate Boss#3}} |
| Daño de los láseres (una salva por segundo) | ninguno | ninguno | ninguno |
| Velocidad | {{guide:vitals.speed@Pirate Boss#1}} | {{guide:vitals.speed@Pirate Boss#2}} | {{guide:vitals.speed@Pirate Boss#3}} |
| Alcance de los láseres | – | – | – |
| Radio de agresión | solo si lo atacan | solo si lo atacan | solo si lo atacan |
| Daño de los cohetes, como máximo | {{guide:behaviour.ability:rocket.damage@Pirate Boss#1}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#2}} | {{guide:behaviour.ability:rocket.damage@Pirate Boss#3}} |
| Créditos | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits@Pirate Boss#2}} | {{guide:spoils.pay.credits@Pirate Boss#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium@Pirate Boss#2}} | {{guide:spoils.pay.thulium@Pirate Boss#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience@Pirate Boss#2}} | {{guide:spoils.pay.experience@Pirate Boss#3}} |
| Honor | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor@Pirate Boss#2}} | {{guide:spoils.pay.honor@Pirate Boss#3}} |
| Puntos PvE por derribo | 15 | 15 | 15 |

**Botín**: una caja, para el piloto que más daño causó.

| Objeto |
| :--- |
| {{guide:spoils.box@Pirate Boss#1;Pirate Boss#2;Pirate Boss#3}} |

### Pirate Scout

Base: Kitefin, con 50 % del casco y 113 % del daño de los láseres; la velocidad y el alcance son los de la nave original.

| | Alpha | Beta | Gamma |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Pirate Scout#1}} | {{guide:vitals.hull@Pirate Scout#2}} | {{guide:vitals.hull@Pirate Scout#3}} |
| Escudo | {{guide:vitals.shield@Pirate Scout#1}} | {{guide:vitals.shield@Pirate Scout#2}} | {{guide:vitals.shield@Pirate Scout#3}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Pirate Scout#1}} | {{guide:vitals.dps@Pirate Scout#2}} | {{guide:vitals.dps@Pirate Scout#3}} |
| Velocidad | {{guide:vitals.speed@Pirate Scout#1}} | {{guide:vitals.speed@Pirate Scout#2}} | {{guide:vitals.speed@Pirate Scout#3}} |
| Alcance de los láseres | 700 | 700 | 700 |
| Radio de agresión | {{guide:vitals.aggro@Pirate Scout#1}} | {{guide:vitals.aggro@Pirate Scout#2}} | {{guide:vitals.aggro@Pirate Scout#3}} |
| Cura al líder, cada uno, por segundo (solo el casco) | 40 | 60 | 80 |
| Créditos | {{guide:spoils.pay.credits@Pirate Scout#1}} | {{guide:spoils.pay.credits@Pirate Scout#2}} | {{guide:spoils.pay.credits@Pirate Scout#3}} |
| Thulium | {{guide:spoils.pay.thulium@Pirate Scout#1}} | {{guide:spoils.pay.thulium@Pirate Scout#2}} | {{guide:spoils.pay.thulium@Pirate Scout#3}} |
| Experiencia (XP) | {{guide:spoils.pay.experience@Pirate Scout#1}} | {{guide:spoils.pay.experience@Pirate Scout#2}} | {{guide:spoils.pay.experience@Pirate Scout#3}} |
| Honor | {{guide:spoils.pay.honor@Pirate Scout#1}} | {{guide:spoils.pay.honor@Pirate Scout#2}} | {{guide:spoils.pay.honor@Pirate Scout#3}} |
| Puntos PvE por derribo | 4 | 4 | 4 |

**Botín**: ninguno. El derribo solo paga sus créditos, su Thulium, su XP y su honor.

<!-- pirate-members:end -->
