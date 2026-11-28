<!-- wiki-i18n source: f9b2d026af543d87 -->
<!-- wiki-i18n title: Mazmorras -->
# Mazmorras {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; clan dungeon alerts; dungeon goombah; dungeon pirate; dungeon crystalys; dungeon warlord; 75 percent; three quarters; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; mazmorra; mazmorras; mazmorra; mazmorras; señor de la guerra; laberinto; fase; zona de botín; carta; portal; portal del clan; potenciador; potenciadores; niebla; guardianes; sala de inicio; sala bloqueada; apoyo de enjambre; zona del caos; avisos de mazmorra del clan; mazmorra del clan; avisos de mazmorra del clan; tres cuartas partes; 75 por ciento; radiation donut; donut; rosquilla de radiación -->

Una **mazmorra** es un laberinto cerrado con un **Señor de la guerra** al final (antes de la 0.5.2 el juego la llamaba mazmorra). Un colíder o el líder de un [clan](/wiki/03-Mechanics/Clans.md) abre una y la paga con el banco del clan, y los miembros del clan vuelan juntos hacia dentro como un solo [grupo](/wiki/03-Mechanics/Groups.md). Abren camino entre los alienígenas del laberinto, abren zonas de botín para elegir una carta en cada una y derrotan al Señor de la guerra. Todos vuelan como un solo grupo, y un grupo no se libra del daño de área de un cohete: la explosión de un Ember, un Scatter o una N.U.K.E. y la zona de radiación que deja una N.U.K.E. te dañan a ti y a los miembros de tu grupo con la mitad de lo que hacen a otra nave. Cuida, pues, adónde disparas (ver [Grupos](/wiki/03-Mechanics/Groups.md#rules-of-engagement)). Todo piloto que participó en el combate cobra cuando cae el Señor de la guerra, dentro de los límites más abajo. Las mazmorras están en la pestaña **Mazmorras** de la página del clan.

Una mazmorra es un combate solo contra los alienígenas: nadie puede atacar dentro a un compañero de clan ni a nadie más. Los alienígenas pagan al caer, como los alienígenas del juego en los que se basan ([lo que pagan los alienígenas](#what-the-aliens-pay)). El pago de la partida es del Señor de la guerra, así que la única manera de cobrarlo es estar en el combate cuando cae.

Una mazmorra no es una [puerta en solitario](/wiki/03-Mechanics/Solo-Gates.md). Una puerta en solitario es una arena en la que solo vuelas tú, abierta con piezas que encuentras con el Materializador de Energía; las dos tienen reglas, pagos y límites separados.

## De un vistazo {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Se abre**: Desde el día 1 de la temporada
- **Quién abre una mazmorra**: Un colíder o el líder, que paga el precio con cargo al banco del clan
- **Grupo**: De 3 a 10 miembros del clan, en un mismo grupo
- **Mazmorras al día**: 3 por clan y día UTC, una abierta a la vez
- **Mazmorras a la vez**: 6 en un mundo
- **Mapas**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Laberintos**: 8; se elige una al abrir una mazmorra
- **Sala del jefe**: Se abre cuando se destruye el 75 % de los Crystalys y sus Twins, redondeando hacia arriba
- **Reunión**: 10 min para reunirse y empezar. Una mazmorra que nadie inicia se cierra, y su precio vuelve al banco del clan
- **Límite de tiempo**: Fase 1: 95 min, Fase 2: 130 min, Fase 3: 165 min desde el inicio. Si se agota, la mazmorra fracasa y la partida no paga nada
- **Vacía**: Una mazmorra sin nadie dentro durante 3 min fracasa
- **Cuando cae el Señor de la guerra**: La mazmorra sigue abierta 2 min para los pilotos que están dentro
- **Volver**: Un piloto que salió o fue destruido puede volver a entrar volando tantas veces como quiera, con al menos 20 s entre dos regresos

<!-- dungeons-glance:end -->

## Cómo es una partida {#how-a-run-goes}

1. **Invocar.** En la pestaña Mazmorras, un [colíder o el líder](/wiki/03-Mechanics/Clans.md#hierarchy-roles) elige una fase y pulsa **Invocar**. El precio sale del [banco del clan](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), y la mazmorra toma uno de los mapas de la lista de arriba. Una mazmorra que nadie inicia se cierra, y el precio vuelve al banco.
2. **Entrar.** Los miembros del clan pulsan **Entrar** en la ventana del Clan mientras vuelan, saltan por el portal del clan o pulsan **Unirse** en la tarjeta de aviso (consulta Entrar). Todos aparecen en la sala de inicio, y los pilotos de dentro son el grupo de la mazmorra.
3. **Iniciar.** La sala de inicio es una sala pequeña en un extremo del laberinto, y su compuerta está cerrada mientras la mazmorra espera a los pilotos. No hay alienígenas dentro, así que se puede esperar con seguridad. La mazmorra **se inicia sola** cuando están dentro todos los pilotos a los que espera y el grupo es lo bastante grande. Espera a los miembros del clan que están conectados, no ausentes y en el grupo de un piloto que ha entrado, y se inicia de inmediato cuando el grupo está lleno. El piloto que abrió la mazmorra, o un oficial, puede pulsar **Iniciar** para empezar antes con los pilotos que estén dentro, si son suficientes. Un piloto que se va deja de ser esperado, y tampoco se espera a uno que aún no ha entrado y ha dejado el grupo o se ha desconectado. Cuando la mazmorra se inicia, la compuerta se abre para siempre, y después solo pueden volver los pilotos que ya estaban dentro.
4. **Abrirse paso por el laberinto.** Entras por un extremo del laberinto y el Señor de la guerra espera en el otro, en una sala bloqueada. El laberinto está a oscuras: solo ves lo que el grupo ha explorado y lo que está cerca de sus naves. Los alienígenas esperan en manadas en los pasillos, y una manada sale en cuanto un piloto vuela al tramo de pasillo donde espera, y luego persigue al grupo por el laberinto.
5. **Abrir las zonas de botín.** Unos anillos en el laberinto marcan las zonas. Mantén una y el grupo vota una carta, que se paga junto con el pago del Señor de la guerra.
6. **Desbloquear la sala del Señor de la guerra.** Destruye tres cuartas partes de los Crystalys y sus Twins del laberinto, y la compuerta de su sala se abre. Hasta entonces el Señor de la guerra no puede ser dañado. Los demás alienígenas se quedan donde están, y también puedes destruirlos.
7. **Derrotar al Señor de la guerra.** Rompe su escudo y su casco, y responde a sus habilidades. Cuando cae, la mazmorra queda superada.
8. **Cobrar.** El pago llega en el momento en que cae el Señor de la guerra. La mazmorra sigue abierta un poco más para los pilotos que están dentro y luego se cierra.

## Entrar {#entering}

Para entrar en una mazmorra necesitas una **nave en vuelo**, así que despega primero y abre después la ventana del Clan, y un [grupo](/wiki/03-Mechanics/Groups.md) con suficientes miembros del clan. También necesitas el **nivel** que pide la fase, y no puedes estar dentro de otra mazmorra. El grupo de la mazmorra tiene un tamaño máximo: cuando está lleno, nadie más puede entrar.

Un colíder o el líder abre una mazmorra, de una en una para el clan, y solo hasta el número de mazmorras al día. El banco del clan tiene que tener el precio. Un clan solo puede abrir una fase después de haber superado la anterior.

Dentro de una mazmorra no puedes cambiar de mundo, y la Jump CPU y la Base CPU no funcionan. El botón **Salir** de la ventana Mazmorra de clan te saca. Antes pide confirmación, salvo que el Señor de la guerra ya haya caído: entonces sales de inmediato. Un piloto que se fue, o que fue destruido, puede volver a entrar; la lista de **De un vistazo** dice cuántas veces y cuánto espera entre dos regresos.

### El portal del clan y el aviso {#the-clan-portal-and-the-call}

Cuando se abre una mazmorra, el clan recibe un **portal** para ella en el mapa de origen de cada corporación (`M-1`, `T-1` y `G-1`), un poco fuera de la zona segura de la estación. Solo los pilotos del clan lo ven: para todos los demás no existe. No tiene zona segura propia. Vuela hasta él y salta como en cualquier otro portal, y te lleva a la mazmorra con las reglas de **Entrar**: una nave en vuelo, un grupo con suficientes miembros del clan, el nivel de la fase y sitio en el grupo. Una vez iniciada la mazmorra, solo pueden usarlo los pilotos que ya estaban dentro. El portal desaparece cuando la mazmorra termina.

Mientras la mazmorra de tu clan espera a los pilotos y tú vuelas en otra parte, te llega un **aviso**: una tarjeta en la parte superior de la pantalla de vuelo, con un sonido. Dice quién abrió la mazmorra, cuántos pilotos hay dentro y cuánto tiempo seguirá abierta. **Unirse** te lleva dentro, igual que **Entrar** en la pestaña Mazmorras, y cuando sales de la mazmorra tu nave vuelve adonde estaba. Unirse aparece atenuado mientras tu grupo es demasiado pequeño. **Ahora no** oculta la tarjeta para esa mazmorra. Si tu grupo ya está dentro y la mazmorra te espera, la tarjeta lo dice. La tarjeta llega a los pilotos del clan que están volando (no a los que están atracados en una estación) y que tienen el nivel que pide la fase. Puedes desactivar la tarjeta y su sonido con **Avisos de mazmorra del clan** en Configuración › General › Grupos.

### La ventana Mazmorra de clan {#the-clan-dungeon-window}

Dentro de una mazmorra, la partida tiene una ventana propia, **Mazmorra de clan**. Muestra el tiempo transcurrido y el que queda, cuántos alienígenas vuelan y cuántos se han destruido, qué debe hacer el grupo ahora (explorar el laberinto, mantener una zona, encontrar al jefe, destruir tres cuartas partes de los Crystalys y sus Twins, derrotar al Señor de la guerra), la barra de la zona mientras estás en una, la habilidad del Señor de la guerra con su cuenta atrás y el botón **Salir**. Es una ventana como las demás: arrástrala por su barra de título y ciérrala con la luz roja de su esquina. Se abre sola cuando entras en una mazmorra, una vez por cada mazmorra: si la cierras, sigue cerrada hasta la siguiente mazmorra. La barra de herramientas tiene un botón **Mazmorra de clan** para ella mientras estás en una mazmorra. Con la ventana cerrada, una habilidad del Señor de la guerra que está a punto de empezar o en marcha aparece como una franja de una línea con su nombre y su cuenta atrás. Haz clic en la franja para volver a abrir la ventana. Mientras una votación de recompensa o una elección de potenciador esté abierta y su ventana cerrada, la ventana Mazmorra de clan tiene una línea para ella, con su reloj y un botón **Elegir** que la vuelve a abrir.

## Las fases {#the-stages}

Una mazmorra tiene una fase, y la fase es su dificultad. Una fase superior tiene alienígenas más duros que golpean más fuerte, y paga más. Los multiplicadores de la tabla son los de los alienígenas. El daño se refiere a sus láseres y cohetes. El Señor de la guerra no sigue la tabla: tiene valores propios para cada fase, más abajo. La tabla también dice cuántos alienígenas envía una fase en comparación con la primera. El **precio** se toma del banco del clan cuando se abre la mazmorra.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Requisito | Casco y escudo de los alienígenas | Número de alienígenas | Daño de los alienígenas | Precio de la mazmorra (créditos, del banco del clan) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Fase 1** | Desde el nivel 6 | ×1 | ×1 | ×1 | 500.000 |
| **Fase 2** | Desde el nivel 7 | ×1,5 | ×1 | ×1,5 | 1.000.000 |
| **Fase 3** | Desde el nivel 8 | ×2 | ×1 | ×2 | 2.000.000 |

<!-- dungeons-stages:end -->

## El laberinto {#the-maze}

Cada mazmorra es un laberinto cerrado en un mapa propio, uno de los mapas de la lista de arriba, y el laberinto es uno de varios diseños. El laberinto ocupa todo el mapa, de borde a borde: una cuadrícula de salas y pasillos con paredes sólidas. Las naves no pueden cruzar una pared, y una pared bloquea los disparos, así que es una cobertura. Un meteoro cae desde arriba, y una pared no lo detiene.

**Salas y compuertas.** La sala de inicio, donde aterrizas, y la sala del Señor de la guerra, en el extremo lejano, tienen cada una una compuerta. Una compuerta cerrada es una pared para las naves, los disparos y los alienígenas por igual. La compuerta de inicio se abre cuando la mazmorra empieza. La del Señor de la guerra sigue bloqueada hasta que tres cuartas partes de los Crystalys y sus Twins son destruidos (consulta [La sala bloqueada](#the-locked-room)). Entre ambas, el laberinto tiene una sala de botín para cada zona de botín.

**Niebla.** El laberinto está a oscuras. En vuelo ves sus paredes y sus alienígenas solo donde ha estado el grupo, y a poca distancia alrededor de cada nave del grupo. Una sala cuenta como explorada en cuanto uno de vosotros está dentro. El minimapa funciona igual: es un plano de toda la planta que se va rellenando a medida que el grupo la explora, con la entrada, la compuerta de la sala del Señor de la guerra, las zonas que habéis encontrado y el Señor de la guerra cuando lo habéis encontrado. Los pilotos de tu propio grupo siempre se muestran.

## Los alienígenas {#the-aliens}

Cuatro tipos de alienígenas guardan el laberinto. Esperan en manadas en los pasillos, nunca en una sala, y una manada sale en cuanto un piloto vuela al tramo de pasillo donde espera. No hay nada en el mapa donde no ha estado ningún piloto, así que ninguna manada espera tras los muros, en lo profundo del laberinto, antes de que llegues. Una manada no espera sitio: está en el mapa en ese mismo instante, por muchos alienígenas que ya haya fuera. Un tramo de pasillo tiene una sola manada, así que en el tramo al que vuelas te espera una manada y no la suma de varias (un grupo de diez tiene más manadas que tramos, y allí un tramo tiene dos, y salen las dos). Una manada que ha salido no te espera: persigue al grupo por el laberinto, y una manada que pierde a todos vuelve a donde salió y se cura. Una manada sale una sola vez: la que destruyes no vuelve, y aquella de la que te alejas volando se queda en el mapa. Las oleadas de las zonas de botín son distintas: la mazmorra mantiene en el aire solo un número limitado de alienígenas a la vez, y ese número crece con el tamaño del grupo, así que una oleada que lo superaría espera sitio, y una manada que destruyes deja entrar a la siguiente oleada. Un grupo más grande se encuentra con más alienígenas en proporción, uno más pequeño con menos, y un tipo de alienígena nunca baja de uno.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Alienígenas, para un grupo de 5 | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Dungeon Goombah | 156 | 156 | 156 |
| Dungeon Pirate | 34 | 34 | 34 |
| Dungeon Crystalys | 34 | 34 | 34 |
| Dungeon Crystalys Twin | 11 | 11 | 11 |
| En total | 235 | 235 | 235 |
| Para abrir la sala del jefe | 34 | 34 | 34 |
| La oleada de una zona de botín | 12 × Dungeon Goombah y 1 × Dungeon Crystalys | 12 × Dungeon Goombah y 1 × Dungeon Crystalys | 12 × Dungeon Goombah y 1 × Dungeon Crystalys |

- **La oleada de una zona de botín espera sitio**: Cuando hay 10 vivos por cada piloto del grupo, o 70 en total

<!-- dungeons-population:end -->

Cada tipo por turno. El casco y el escudo son los habituales multiplicados por el factor de la fase de la columna.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Dungeon Goombah

- **Se parece a**: Goombah
- **Vuela en manadas de**: 6
- **Paga y suelta como**: Goombah

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dungeon Goombah}} | {{guide:vitals.hull*1.5@Dungeon Goombah}} | {{guide:vitals.hull*2@Dungeon Goombah}} |
| Escudo | {{guide:vitals.shield@Dungeon Goombah}} | {{guide:vitals.shield*1.5@Dungeon Goombah}} | {{guide:vitals.shield*2@Dungeon Goombah}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Dungeon Goombah}} | {{guide:vitals.dps*1.5@Dungeon Goombah}} | {{guide:vitals.dps*2@Dungeon Goombah}} |
| Velocidad | {{guide:vitals.speed@Dungeon Goombah}} | {{guide:vitals.speed@Dungeon Goombah}} | {{guide:vitals.speed@Dungeon Goombah}} |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | {{guide:vitals.aggro@Dungeon Goombah}} | {{guide:vitals.aggro@Dungeon Goombah}} | {{guide:vitals.aggro@Dungeon Goombah}} |
| Pago y botín, veces el del original | ×1 | ×1,5 | ×2 |
| Créditos por baja | {{guide:spoils.pay.credits@Goombah#1}} | {{guide:spoils.pay.credits*1.5@Goombah#1}} | {{guide:spoils.pay.credits*2@Goombah#1}} |
| Thulium por baja | {{guide:spoils.pay.thulium@Goombah#1}} | {{guide:spoils.pay.thulium*1.5@Goombah#1}} | {{guide:spoils.pay.thulium*2@Goombah#1}} |
| Experiencia por baja | {{guide:spoils.pay.experience@Goombah#1}} | {{guide:spoils.pay.experience*1.5@Goombah#1}} | {{guide:spoils.pay.experience*2@Goombah#1}} |
| Honor por baja | {{guide:spoils.pay.honor@Goombah#1}} | {{guide:spoils.pay.honor*1.5@Goombah#1}} | {{guide:spoils.pay.honor*2@Goombah#1}} |

### Dungeon Pirate

- **Se parece a**: Pirate Boss
- **Vuela en manadas de**: 2
- **Paga y suelta como**: Pirate Boss
- **Cohete**: Un cohete recto cada 5 s, alcance de 1.100 unidades

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dungeon Pirate}} | {{guide:vitals.hull*1.5@Dungeon Pirate}} | {{guide:vitals.hull*2@Dungeon Pirate}} |
| Escudo | {{guide:vitals.shield@Dungeon Pirate}} | {{guide:vitals.shield*1.5@Dungeon Pirate}} | {{guide:vitals.shield*2@Dungeon Pirate}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Dungeon Pirate}} | {{guide:vitals.dps*1.5@Dungeon Pirate}} | {{guide:vitals.dps*2@Dungeon Pirate}} |
| Daño de cohete | {{guide:behaviour.ability:rocket.damage@Dungeon Pirate}} | {{guide:behaviour.ability:rocket.damage*1.5@Dungeon Pirate}} | {{guide:behaviour.ability:rocket.damage*2@Dungeon Pirate}} |
| Velocidad | {{guide:vitals.speed@Dungeon Pirate}} | {{guide:vitals.speed@Dungeon Pirate}} | {{guide:vitals.speed@Dungeon Pirate}} |
| Alcance de los láseres | 700 | 700 | 700 |
| Radio de agresión | {{guide:vitals.aggro@Dungeon Pirate}} | {{guide:vitals.aggro@Dungeon Pirate}} | {{guide:vitals.aggro@Dungeon Pirate}} |
| Pago y botín, veces el del original | ×1 | ×1,5 | ×2 |
| Créditos por baja | {{guide:spoils.pay.credits@Pirate Boss#1}} | {{guide:spoils.pay.credits*1.5@Pirate Boss#1}} | {{guide:spoils.pay.credits*2@Pirate Boss#1}} |
| Thulium por baja | {{guide:spoils.pay.thulium@Pirate Boss#1}} | {{guide:spoils.pay.thulium*1.5@Pirate Boss#1}} | {{guide:spoils.pay.thulium*2@Pirate Boss#1}} |
| Experiencia por baja | {{guide:spoils.pay.experience@Pirate Boss#1}} | {{guide:spoils.pay.experience*1.5@Pirate Boss#1}} | {{guide:spoils.pay.experience*2@Pirate Boss#1}} |
| Honor por baja | {{guide:spoils.pay.honor@Pirate Boss#1}} | {{guide:spoils.pay.honor*1.5@Pirate Boss#1}} | {{guide:spoils.pay.honor*2@Pirate Boss#1}} |

### Dungeon Crystalys

- **Se parece a**: Crystalys
- **Vuela en manadas de**: 2
- **Paga y suelta como**: Crystalys

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dungeon Crystalys}} | {{guide:vitals.hull*1.5@Dungeon Crystalys}} | {{guide:vitals.hull*2@Dungeon Crystalys}} |
| Escudo | {{guide:vitals.shield@Dungeon Crystalys}} | {{guide:vitals.shield*1.5@Dungeon Crystalys}} | {{guide:vitals.shield*2@Dungeon Crystalys}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Dungeon Crystalys}} | {{guide:vitals.dps*1.5@Dungeon Crystalys}} | {{guide:vitals.dps*2@Dungeon Crystalys}} |
| Velocidad | {{guide:vitals.speed@Dungeon Crystalys}} | {{guide:vitals.speed@Dungeon Crystalys}} | {{guide:vitals.speed@Dungeon Crystalys}} |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | {{guide:vitals.aggro@Dungeon Crystalys}} | {{guide:vitals.aggro@Dungeon Crystalys}} | {{guide:vitals.aggro@Dungeon Crystalys}} |
| Pago y botín, veces el del original | ×1 | ×1,5 | ×2 |
| Créditos por baja | {{guide:spoils.pay.credits@Crystalys#1}} | {{guide:spoils.pay.credits*1.5@Crystalys#1}} | {{guide:spoils.pay.credits*2@Crystalys#1}} |
| Thulium por baja | {{guide:spoils.pay.thulium@Crystalys#1}} | {{guide:spoils.pay.thulium*1.5@Crystalys#1}} | {{guide:spoils.pay.thulium*2@Crystalys#1}} |
| Experiencia por baja | {{guide:spoils.pay.experience@Crystalys#1}} | {{guide:spoils.pay.experience*1.5@Crystalys#1}} | {{guide:spoils.pay.experience*2@Crystalys#1}} |
| Honor por baja | {{guide:spoils.pay.honor@Crystalys#1}} | {{guide:spoils.pay.honor*1.5@Crystalys#1}} | {{guide:spoils.pay.honor*2@Crystalys#1}} |

### Dungeon Crystalys Twin

- **Se parece a**: Crystalys, 1,4 veces más grande
- **Vuela en manadas de**: 1
- **Paga y suelta como**: Crystalys

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dungeon Crystalys Twin}} | {{guide:vitals.hull*1.5@Dungeon Crystalys Twin}} | {{guide:vitals.hull*2@Dungeon Crystalys Twin}} |
| Escudo | {{guide:vitals.shield@Dungeon Crystalys Twin}} | {{guide:vitals.shield*1.5@Dungeon Crystalys Twin}} | {{guide:vitals.shield*2@Dungeon Crystalys Twin}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps@Dungeon Crystalys Twin}} | {{guide:vitals.dps*1.5@Dungeon Crystalys Twin}} | {{guide:vitals.dps*2@Dungeon Crystalys Twin}} |
| Velocidad | {{guide:vitals.speed@Dungeon Crystalys Twin}} | {{guide:vitals.speed@Dungeon Crystalys Twin}} | {{guide:vitals.speed@Dungeon Crystalys Twin}} |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | {{guide:vitals.aggro@Dungeon Crystalys Twin}} | {{guide:vitals.aggro@Dungeon Crystalys Twin}} | {{guide:vitals.aggro@Dungeon Crystalys Twin}} |
| Pago y botín, veces el del original | ×2 | ×3 | ×4 |
| Créditos por baja | {{guide:spoils.pay.credits*2@Crystalys#1}} | {{guide:spoils.pay.credits*3@Crystalys#1}} | {{guide:spoils.pay.credits*4@Crystalys#1}} |
| Thulium por baja | {{guide:spoils.pay.thulium*2@Crystalys#1}} | {{guide:spoils.pay.thulium*3@Crystalys#1}} | {{guide:spoils.pay.thulium*4@Crystalys#1}} |
| Experiencia por baja | {{guide:spoils.pay.experience*2@Crystalys#1}} | {{guide:spoils.pay.experience*3@Crystalys#1}} | {{guide:spoils.pay.experience*4@Crystalys#1}} |
| Honor por baja | {{guide:spoils.pay.honor*2@Crystalys#1}} | {{guide:spoils.pay.honor*3@Crystalys#1}} | {{guide:spoils.pay.honor*4@Crystalys#1}} |

<!-- dungeons-enemies:end -->

## El Señor de la guerra {#the-warlord}

El Señor de la guerra espera en la sala del extremo lejano del laberinto, y su caída es lo que paga la partida. No paga una baja propia, como sí hacen los demás alienígenas. Es un Crystalys gigantesco. Su casco y su escudo crecen con el tamaño del grupo: cuantos más pilotos entran, más resistente es, en proporción. No sale nunca de su sala, con la mazmorra cerrada o abierta: se mantiene dentro de las paredes de la sala y no sale a cazar por los pasillos. Un piloto de fuera solo puede atraerlo hasta el borde de la sala, y aun así dispara por una mazmorra abierta a todo lo que alcanza su láser. Usa sus habilidades una a una, en orden aleatorio, cada una con su propia recarga. Desde la fase 2 su láser dispara a dos pilotos a la vez: los dos más cercanos que puede ver reciben cada uno una salva completa.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Se parece a**: Crystalys, 3 veces más grande
- **Recarga del escudo**: 3.000 por segundo, tras 15 s sin recibir daño

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | {{guide:vitals.hull@Dungeon Warlord}} | {{guide:vitals.hull*1.5@Dungeon Warlord}} | {{guide:vitals.hull*2.5@Dungeon Warlord}} |
| Escudo | {{guide:vitals.shield@Dungeon Warlord}} | {{guide:vitals.shield*1.5@Dungeon Warlord}} | {{guide:vitals.shield*2.5@Dungeon Warlord}} |
| Daño de los láseres (una salva por segundo) | {{guide:vitals.dps*0.875~1.125@Dungeon Warlord}} | {{guide:vitals.dps*1.3125~1.6875@Dungeon Warlord}} a cada uno de 2 pilotos | {{guide:vitals.dps*1.75~2.25@Dungeon Warlord}} a cada uno de 2 pilotos |
| Velocidad | {{guide:vitals.speed@Dungeon Warlord}} | {{guide:vitals.speed@Dungeon Warlord}} | {{guide:vitals.speed@Dungeon Warlord}} |
| Alcance de los láseres | 1.100 | 1.100 | 1.100 |

El casco y el escudo de arriba son para un grupo de 5. Crecen con el grupo: son el casco y el escudo del Señor de la guerra juntos, según el número de pilotos del grupo cuando empieza la mazmorra.

| Pilotos en el grupo | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| 3 | {{guide:vitals.hull*0.6@Dungeon Warlord}} + {{guide:vitals.shield*0.6@Dungeon Warlord}} | {{guide:vitals.hull*0.9@Dungeon Warlord}} + {{guide:vitals.shield*0.9@Dungeon Warlord}} | {{guide:vitals.hull*1.5@Dungeon Warlord}} + {{guide:vitals.shield*1.5@Dungeon Warlord}} |
| 4 | {{guide:vitals.hull*0.8@Dungeon Warlord}} + {{guide:vitals.shield*0.8@Dungeon Warlord}} | {{guide:vitals.hull*1.2@Dungeon Warlord}} + {{guide:vitals.shield*1.2@Dungeon Warlord}} | {{guide:vitals.hull*2@Dungeon Warlord}} + {{guide:vitals.shield*2@Dungeon Warlord}} |
| 5 | {{guide:vitals.hull@Dungeon Warlord}} + {{guide:vitals.shield@Dungeon Warlord}} | {{guide:vitals.hull*1.5@Dungeon Warlord}} + {{guide:vitals.shield*1.5@Dungeon Warlord}} | {{guide:vitals.hull*2.5@Dungeon Warlord}} + {{guide:vitals.shield*2.5@Dungeon Warlord}} |
| 6 | {{guide:vitals.hull*1.2@Dungeon Warlord}} + {{guide:vitals.shield*1.2@Dungeon Warlord}} | {{guide:vitals.hull*1.8@Dungeon Warlord}} + {{guide:vitals.shield*1.8@Dungeon Warlord}} | {{guide:vitals.hull*3@Dungeon Warlord}} + {{guide:vitals.shield*3@Dungeon Warlord}} |
| 7 | {{guide:vitals.hull*1.4@Dungeon Warlord}} + {{guide:vitals.shield*1.4@Dungeon Warlord}} | {{guide:vitals.hull*2.1@Dungeon Warlord}} + {{guide:vitals.shield*2.1@Dungeon Warlord}} | {{guide:vitals.hull*3.5@Dungeon Warlord}} + {{guide:vitals.shield*3.5@Dungeon Warlord}} |
| 8 | {{guide:vitals.hull*1.6@Dungeon Warlord}} + {{guide:vitals.shield*1.6@Dungeon Warlord}} | {{guide:vitals.hull*2.4@Dungeon Warlord}} + {{guide:vitals.shield*2.4@Dungeon Warlord}} | {{guide:vitals.hull*4@Dungeon Warlord}} + {{guide:vitals.shield*4@Dungeon Warlord}} |
| 9 | {{guide:vitals.hull*1.8@Dungeon Warlord}} + {{guide:vitals.shield*1.8@Dungeon Warlord}} | {{guide:vitals.hull*2.7@Dungeon Warlord}} + {{guide:vitals.shield*2.7@Dungeon Warlord}} | {{guide:vitals.hull*4.5@Dungeon Warlord}} + {{guide:vitals.shield*4.5@Dungeon Warlord}} |
| 10 | {{guide:vitals.hull*2@Dungeon Warlord}} + {{guide:vitals.shield*2@Dungeon Warlord}} | {{guide:vitals.hull*3@Dungeon Warlord}} + {{guide:vitals.shield*3@Dungeon Warlord}} | {{guide:vitals.hull*5@Dungeon Warlord}} + {{guide:vitals.shield*5@Dungeon Warlord}} |

<!-- dungeons-boss:end -->

### La sala bloqueada {#the-locked-room}

La compuerta de la sala del Señor de la guerra está cerrada desde el momento en que se abre la mazmorra, y mientras lo está el Señor de la guerra no puede ser dañado: ningún láser, cohete ni explosión lo toca, y no usa ninguna habilidad. La compuerta se abre para siempre cuando se han destruido **tres cuartas partes de los Crystalys y sus Twins** con los que se creó la mazmorra, redondeando hacia arriba (la tabla de los alienígenas de arriba los cuenta para un grupo de 5, y su última fila dice cuántos hacen falta). Cuentan los Crystalys y los Twins de las manadas del laberinto, y quien los destruya. Una manada sale solo cuando un piloto vuela a su tramo de pasillo, así que el grupo tiene que encontrar suficientes para abrir la compuerta. No cuentan para la compuerta los demás alienígenas, las oleadas de las zonas de botín, los Goombahs que llama el Señor de la guerra ni el propio Señor de la guerra.

La ventana Mazmorra de clan cuenta cuántos de ellos faltan por destruir para abrir la sala y dice, en una etiqueta, que el Señor de la guerra no puede ser dañado, y un mensaje te avisa cuando la sala se desbloquea. Una manada que aún no ha salido cuenta entera, así que el grupo tiene que encontrar a los Crystalys y sus Twins en el laberinto y volar a sus tramos de pasillo. **Los demás alienígenas no desaparecen cuando se abre la compuerta.** Se quedan en el laberinto, salen cuando un piloto vuela a su tramo de pasillo y se pueden destruir como antes, así que un grupo que quiera puede destruirlos todos antes de combatir al Señor de la guerra: la cuenta de alienígenas de la ventana sigue hasta todos los alienígenas con los que se creó la mazmorra, y se ve completa cuando no queda ninguno. Pagan al caer ([lo que pagan los alienígenas](#what-the-aliens-pay)), y los que siguen vivos cuando cae el Señor de la guerra se van con la mazmorra. En el minimapa la compuerta es una línea roja mientras está bloqueada y una verde cuando está abierta. Una mazmorra nunca es una trampa: el límite de tiempo sigue terminando una mazmorra cuya compuerta sigue cerrada, y un administrador puede desbloquear la sala de una mazmorra atascada.

### Sus habilidades {#its-abilities}

- **El anillo rojo** del Aura de robo de vida hiere a todo piloto que está dentro y cura al Señor de la guerra con ese daño. La Absorción de escudo también tiene un anillo rojo: drena los escudos de los pilotos de dentro y carga el del Señor de la guerra. En ambos casos, sal del anillo o ponte detrás de una pared.
- **Los anillos ámbar** de la Lluvia de meteoros muestran dónde caerán los meteoros un instante después. Sigue moviéndote y sal del anillo antes de que caiga.
- **Foco en el más buscado** marca al piloto que más daño ha hecho al Señor de la guerra, con un corchete dorado en su nave, y el Señor de la guerra le dispara un tiro extra cada segundo mientras dura. Su puntería no cambia: sigue disparando al piloto más cercano que puede ver, así que un piloto marcado que además es el más cercano recibe ambos. El tiro extra necesita línea libre y el alcance del láser del Señor de la guerra, así que una pared o algo de distancia lo salva. No empieza mientras nadie haya hecho daño.
- **La Andanada de cohetes** lanza un cohete teledirigido contra cada piloto que el Señor de la guerra puede ver, y mientras dura lanza otra ronda cada pocos segundos. Una pared en el camino detiene un cohete. Un anillo muestra a qué piloto sigue un cohete. Una EMP Charge o un camuflaje los despista.
- **El Apoyo de enjambre** es el Señor de la guerra llamando a sus Goombahs. Mientras viven, no puede ser dañado, y no dispara ni usa otra habilidad. Destrúyelos todos: el cartel de la habilidad cuenta cuántos quedan. Si pasa un minuto, el Señor de la guerra vuelve a poder ser dañado y los Goombahs que quedan siguen luchando. No cuentan para la sala del Señor de la guerra, y no pagan nada.
- **La Zona del Caos** es un anillo violeta en el suelo, alrededor del Señor de la guerra, y mientras dura va adonde vaya el Señor de la guerra. Nadie dentro del anillo puede atacar, ni con láseres ni con cohetes, aunque las reparaciones, el camuflaje y el vuelo siguen funcionando, y el Señor de la guerra y sus alienígenas disparan como siempre. El anillo aparece un momento antes de hacer efecto: sal de él y quédate fuera, porque sigue al Señor de la guerra. Un piloto que está fuera puede seguir disparando, hasta donde alcancen sus armas.
- **La Lanza fantasma** hace que el Señor de la guerra desaparezca durante un segundo. Vuelve a otro lugar de su sala junto con tres ilusiones de sí mismo. Mientras una ilusión vive, dispara al piloto más cercano que puede ver con la mitad de la salva del Señor de la guerra y cura cada segundo el casco y el escudo del Señor de la guerra (los números están en la tabla de las habilidades). Las ilusiones tienen un casco propio: destrúyelas para detener la curación. No pagan nada, y se van con el Señor de la guerra cuando cae. El Señor de la guerra puede ser destruido mientras ellas viven.
- **La Rosquilla de radiación** enciende tres anillos de radiación alrededor del lugar donde estaba el Señor de la guerra cuando empezó la habilidad, uno tras otro desde el Señor de la guerra hacia fuera, con uno o dos segundos entre dos anillos. Cada anillo muestra sus dos bordes un momento antes de encenderse y después quema a todo piloto que esté dentro durante unos segundos, directamente del casco (la tabla de las habilidades da los tiempos y la parte del casco por segundo). Un anillo no se apaga cuando se enciende el siguiente: dos anillos, y en las fases más altas los tres, pueden arder a la vez. El hueco alrededor del Señor de la guerra, el suelo entre los anillos y el suelo fuera del último son seguros: quédate en ellos y sal de un anillo antes de que se encienda. Una pared no detiene la radiación y un camuflaje no salva a un piloto de ella; la Tecnología de radiación reduce la dosis.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Habilidad | Preparación | Duración | Recarga | Radio del anillo (unidades) | El Señor de la guerra recupera, como máximo |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura de robo de vida** | 2 s | 15 s | 2 min | 900 | 8 % de su casco y escudo |
| **Lluvia de meteoros** | 1,5 s | 3 salvas, con 4 s entre una y otra | 2 min | 546 | – |
| **Foco en el más buscado** | 1 s | 20 s | 2 min | – | – |
| **Andanada de cohetes** | 1,5 s | 45 s | 2 min | – | – |
| **Absorción de escudo** | 2 s | 15 s | 2 min | 900 | 6 % de su escudo |
| **Apoyo de enjambre** | 2 s | Hasta 1 min | 3 min | – | – |
| **Zona del Caos** | 2 s | 15 s | 2 min | 900 | – |
| **Lanza fantasma** | 1,5 s | 1 s | 2 min | – | – |
| **Rosquilla de radiación** | 1 s | Hasta 8,5 s | 75 s | 2.150 | – |

| Habilidad | Fase 1 | Fase 2 | Fase 3 |
| :--- | :--- | :--- | :--- |
| **Aura de robo de vida** | {{guide:behaviour.ability:lifesteal.drainPerSec@Dungeon Warlord}} por segundo | {{guide:behaviour.ability:lifesteal.drainPerSec*1.25@Dungeon Warlord}} por segundo | {{guide:behaviour.ability:lifesteal.drainPerSec*1.5@Dungeon Warlord}} por segundo |
| **Lluvia de meteoros** | 6 meteoros por salva, {{guide:behaviour.ability:meteor.damage@Dungeon Warlord}} cada uno | 8 meteoros por salva, {{guide:behaviour.ability:meteor.damage*1.25@Dungeon Warlord}} cada uno | 10 meteoros por salva, {{guide:behaviour.ability:meteor.damage*1.5@Dungeon Warlord}} cada uno |
| **Foco en el más buscado** | {{guide:vitals.dps*1.3125~1.6875@Dungeon Warlord}} por disparo adicional al piloto que más daño ha causado, uno cada 1 s | {{guide:vitals.dps*1.96875~2.53125@Dungeon Warlord}} por disparo adicional al piloto que más daño ha causado, uno cada 1 s | {{guide:vitals.dps*2.625~3.375@Dungeon Warlord}} por disparo adicional al piloto que más daño ha causado, uno cada 1 s |
| **Andanada de cohetes** | {{guide:behaviour.ability:barrage.damageMin@Dungeon Warlord}}–{{guide:behaviour.ability:barrage.damage@Dungeon Warlord}} por cohete a cada piloto, uno cada 15 s | {{guide:behaviour.ability:barrage.damageMin*1.25@Dungeon Warlord}}–{{guide:behaviour.ability:barrage.damage*1.25@Dungeon Warlord}} por cohete a cada piloto, uno cada 15 s | {{guide:behaviour.ability:barrage.damageMin*1.5@Dungeon Warlord}}–{{guide:behaviour.ability:barrage.damage*1.5@Dungeon Warlord}} por cohete a cada piloto, uno cada 15 s |
| **Absorción de escudo** | {{guide:behaviour.ability:absorb.drainPerSec@Dungeon Warlord}} de escudo por segundo | {{guide:behaviour.ability:absorb.drainPerSec*1.25@Dungeon Warlord}} de escudo por segundo | {{guide:behaviour.ability:absorb.drainPerSec*1.5@Dungeon Warlord}} de escudo por segundo |
| **Apoyo de enjambre** | 12 Goombahs | 18 Goombahs | 24 Goombahs |
| **Zona del Caos** | Los pilotos dentro del anillo no pueden atacar | Los pilotos dentro del anillo no pueden atacar | Los pilotos dentro del anillo no pueden atacar |
| **Lanza fantasma** | 3 ilusiones; cada una dispara el 50 % de la salva del Señor de la guerra y, mientras vive, cura al Señor de la guerra 50.000 de casco y 50.000 de escudo por segundo | 3 ilusiones; cada una dispara el 50 % de la salva del Señor de la guerra y, mientras vive, cura al Señor de la guerra 50.000 de casco y 50.000 de escudo por segundo | 3 ilusiones; cada una dispara el 50 % de la salva del Señor de la guerra y, mientras vive, cura al Señor de la guerra 50.000 de casco y 50.000 de escudo por segundo |
| **Rosquilla de radiación** | 3 anillos, encendidos uno tras otro; cada uno arde durante 2 s y quita el 8 % del casco de un piloto por segundo | 3 anillos, encendidos uno tras otro; cada uno arde durante 3 s y quita el 8 % del casco de un piloto por segundo | 3 anillos, encendidos uno tras otro; cada uno arde durante 4,5 s y quita el 8 % del casco de un piloto por segundo |

<!-- dungeons-abilities:end -->

### Sus tres pasos {#its-three-steps}

<!-- mob-ladder:begin -->
<!-- Generated from server/Resources/MobAbilities.json (and the client's locales/<language>/mobs.toml) by scripts/mob-abilities-wiki.sh: don't edit by hand. -->

El Señor de la guerra tiene tres pasos ([cómo funcionan](/wiki/03-Mechanics/Special-Abilities.md#the-bosses-three-steps)); cada uno ocurre una vez.

- **Por debajo de dos tercios**: La pausa entre sus habilidades baja a 4 s y sus esperas a ×0,75.
- **Por debajo de un tercio**: La pausa baja a 2 s, sus esperas a ×0,5 y su daño sube a ×1,25; lanza una andanada de Meteor gratis, y su Swarm nunca vuelve más rápido que cada 120 s.
- **Una pausa en cada paso.** Cuando empieza un paso, el Señor de la guerra no puede ser dañado durante 3 s.

<!-- mob-ladder:end -->

## Zonas de botín {#loot-zones}

Un anillo en el suelo del laberinto marca cada zona de botín en cuanto el grupo la encuentra. Quédate un momento dentro y la zona despierta, y una oleada de alienígenas va a por ella. Entonces el grupo tiene que **mantener** la zona: dejar a un piloto dentro hasta que la barra se llene. Cuantos más pilotos haya en el anillo, más rápido se llena la barra: un número junto a la barra dice cuántas veces más rápido, y la tabla de abajo da los tiempos. Suficientes alienígenas en el anillo detienen la barra (la lista de abajo dice cuántos), y esta retrocede mientras no haya nadie dentro, así que acaba antes con la oleada. Cuando la zona se abre, el grupo ve tres cartas distintas y **vota** una. Una zona se abre una sola vez, y su oleada no vuelve. La votación es una ventana pequeña propia en el lado derecho de la pantalla, con una fila para cada recompensa: su imagen, su nombre, cuántas recibes y cuántos votos tiene. Apunta a una fila para leer qué es y quién la recibe, y pulsa una fila para votarla (pulsa otra fila para cambiar tu voto). La ventana se abre sola en cada votación y no tapa el combate, así que puedes seguir volando mientras el grupo elige. Arrástrala adonde quieras o ciérrala con la luz roja; el botón **Elegir** de la ventana Mazmorra de clan la vuelve a abrir. Tu voto sigue contando, y el reloj sigue corriendo, mientras la ventana está cerrada.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zonas de botín**: 6 en cada laberinto
- **Radio**: 450 unidades
- **Despertar**: Quédate dentro del anillo 2 s
- **Mantener**: Mantén a un piloto dentro durante 30 s. La barra se detiene mientras haya 3 o más alienígenas en el anillo y retrocede mientras no haya nadie
- **Elegir**: El grupo tiene 45 s para votar. La votación termina antes si todos los pilotos presentes han votado o si una carta tiene más de la mitad de los votos

Más pilotos en el anillo mantienen una zona más rápido. Lo que tarda en mantenerse una zona:

| Pilotos en el anillo | Tiempo para mantener la zona |
| :--- | ---: |
| 1 | 30 s |
| 2 | 20 s |
| 3 | 15 s |
| 4 | 12 s |
| 5 o más | 10 s |

<!-- dungeons-zones:end -->

### Potenciadores {#boosters}

En las fases 2 y 3 el grupo gana potenciadores destruyendo a los alienígenas de la mazmorra. Cae un potenciador por cada décima parte de ellos: cuando se ha destruido una décima parte de los alienígenas, luego dos décimas, y así hasta todos ellos, diez caídas en total. Cuenta cada alienígena con el que se hizo la mazmorra, sea quien sea quien lo destruya (es el recuento de alienígenas destruidos de la ventana Mazmorra de clan); las oleadas de las zonas de botín y los alienígenas que llama el Señor de la guerra no cuentan, así que una zona no trae ningún potenciador. En cada caída cada piloto recibe una ventana de medio minuto para elegir un potenciador temporal para sí mismo entre tres que el juego saca al azar de cinco: **Daño** (tus láseres golpean más fuerte), **Puntos de vida** (tu nave aguanta más casco), **Escudo** (tu escudo aguanta más), **Velocidad** (tu nave vuela más rápido) y **Recarga de escudo** (tu escudo se recarga más rápido). Pulsa una carta para elegirla. Si no respondes a tiempo, el juego elige Puntos de vida por ti, o el primero de los tres si Puntos de vida no está entre ellos. Una elección vale un 3 % en la fase 3 y un 1,5 % en la fase 2, así que diez elecciones suman como máximo un treinta por ciento en la fase 3 y un quince por ciento en la fase 2, sean del tipo que sean. La fase 1 no tiene potenciadores. Los tres potenciadores son las filas de una ventana pequeña propia, como la votación de recompensa: se abre sola en cada caída en el lado derecho de la pantalla, y el medio minuto es su reloj. Apunta a una fila para leer qué hace el tipo y cuánto tienes ya de él. Arrastra la ventana, ciérrala con la luz roja o ábrela de nuevo con el botón **Elegir** de la ventana Mazmorra de clan.

La décima caída llega con el último alienígena. Un grupo que destruye a todos los alienígenas antes de luchar contra el Señor de la guerra obtiene las diez caídas; un grupo que abre la sala del Señor de la guerra y sigue adelante obtiene las caídas de los alienígenas que ha destruido hasta entonces, y los que quedan se quedan y aún pueden destruirse. Cuando ha empezado el combate contra el Señor de la guerra, ya no cae ningún potenciador.

Un potenciador dura hasta que se supera la mazmorra. Si sales de la mazmorra o eres destruido, pierdes tus potenciadores, y los recuperas cuando vuelves a entrar. Una etiqueta bajo la ventana Mazmorra de clan muestra lo que tienes.

### Las cartas {#the-cards}

Las cartas se sacan una a una del conjunto de abajo. La probabilidad es la de una carta en un sorteo. Cada carta va a todos los pilotos que cobran, también las de equipo: una carta con muchas copias da a cada uno todas esas copias, y una carta de equipo da a cada uno una pieza propia, forjada para él. Un piloto que no cobra tampoco recibe carta, y una zona abierta en una mazmorra que fracasa no paga nada.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carta | Fase 1 | Fase 2 | Fase 3 | Probabilidad | Para |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 4.000 | 6.000 | 10.000 | 23,9 % | Cada piloto pagado |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13,65 % | Cada piloto pagado |
| Velkonite | 200 | 300 | 500 | 13,65 % | Cada piloto pagado |
| Orvium | 200 | 300 | 500 | 13,65 % | Cada piloto pagado |
| Ultra Core | 5.000 | 7.500 | 12.500 | 11,4 % | Cada piloto pagado |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 9,1 % | Cada piloto pagado |
| Dark Matter | 10 | 16 | 24 | 9,1 % | Cada piloto pagado |
| Dark Matter Plate | 4 | 6 | 8 | 4,55 % | Cada piloto pagado |
| Starfire-III | – | – | 1 | 0,07 % | Cada piloto pagado |
| Helios Beam | – | – | 1 | 0,07 % | Cada piloto pagado |
| Engine III | – | – | 1 | 0,07 % | Cada piloto pagado |
| Adaptive Core III | – | – | 1 | 0,07 % | Cada piloto pagado |
| Heavy Shield Core | – | – | 1 | 0,07 % | Cada piloto pagado |
| Momentum Thruster IV | – | – | 1 | 0,07 % | Cada piloto pagado |
| Impulse Thruster IV | – | – | 1 | 0,07 % | Cada piloto pagado |
| Hull Plating II | – | – | 1 | 0,07 % | Cada piloto pagado |
| Hull Plating III | – | – | 1 | 0,07 % | Cada piloto pagado |
| Damage Amp IV | – | – | 1 | 0,07 % | Cada piloto pagado |
| Crit Amp IV | – | – | 1 | 0,07 % | Cada piloto pagado |
| Penetration Amp IV | – | – | 1 | 0,07 % | Cada piloto pagado |
| Capacity Shield Cell IV | – | – | 1 | 0,08 % | Cada piloto pagado |
| Absorption Shield Cell IV | – | – | 1 | 0,08 % | Cada piloto pagado |

- **Equipo**: Las cartas con un solo ejemplar son equipo: juntas, 1 % de las cartas

<!-- dungeons-cards:end -->

Las cartas con una sola copia son **equipo**, y solo una mazmorra de fase 3 puede ofrecerlas. Una pieza de equipo se forja para cada piloto que cobra, al pagarse: cada uno saca su propio [grado de encantamiento](/wiki/06-Items/Overview.md#item-enchants) con las mismas probabilidades que una pieza que construyes en Ensamblaje, así que la mayoría sale Estándar, y un grado superior, hasta Ascendido, con mejoras, es un hallazgo raro. Cada pieza sortea además su [integridad](/wiki/06-Items/Forge.md#integrity-and-fractures), igual que una pieza fabricada.

## Pago {#pay}

Cuando cae el Señor de la guerra, todo piloto que se lo ha ganado cobra, una vez por partida. Las cartas que eligió el grupo se suman al pago de la fase. No hay multiplicador de mundo: el pago es el mismo en todos los mundos.

Las **Orvium Reinforced Plates** y las **Echo Shards** y **Lattice Shards** de la Forja no son una carta de la votación. Forman parte del pago de la fase, y cada piloto que cobra las recibe una vez por partida. Los **Heartshards** se pagan de otro modo: la línea bajo la tabla lo explica. Los objetos que paga la partida no son Comercializables: no puedes [venderlos en la Subasta](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Honor | Experiencia | Créditos | Thulium | Munición x4 | Orvium Reinforced Plates | Echo Shards | Lattice Shards | Puntos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Fase 1** | 25.000 | 600.000 | 5.000.000 | 8.000 | 4.000 | 5 | 24 | 10 | 850 |
| **Fase 2** | 50.000 | 1.500.000 | 10.000.000 | 18.000 | 9.000 | 10 | 16 | 12 | 2.000 |
| **Fase 3** | 100.000 | 2.400.000 | 17.500.000 | 30.000 | 15.000 | 15 | 16 | 14 | 3.400 |

- **Heartshards**: 1 con la primera finalización pagada de cada etapa en una temporada, y un 5 % de probabilidad de uno más con cada finalización pagada.

<!-- dungeons-pay:end -->

### Quién cobra {#who-is-paid}

Estas reglas deciden quién cobra **la partida**. Una partida se juega entera aunque no pague nada, y la pantalla de resultados dice por qué. Nunca se te niega la entrada por haber cobrado ya una fase: esa partida simplemente no paga. Los alienígenas leen las mismas reglas, baja por baja, salvo la parte en el combate ([lo que pagan los alienígenas](#what-the-aliens-pay)).

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Un día**: Una fase paga a un piloto una vez por día UTC: el día en que cae el Señor de la guerra
- **Una semana**: Un piloto cobra como máximo 14 fases completadas por semana UTC, de lunes a domingo
- **Dentro**: Al menos 2 min en total
- **Parte en el combate**: Al menos una de estas: infligió 0,1 % del casco y el escudo del Señor de la guerra; destruyó 10 de los alienígenas de la mazmorra; curó a otros pilotos por 50.000 durante el combate contra el Señor de la guerra

<!-- dungeons-rules:end -->

### Lo que valen un día y una semana {#what-a-day-and-a-week-are-worth}

Lo que un piloto puede cobrar en un día y en la mejor semana que permiten los límites. La última columna es lo que el pago suma a tus [puntos PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Pago por piloto | Honor | Experiencia | Créditos | Thulium | Munición x4 | Orvium Reinforced Plates | Echo Shards | Lattice Shards | Puntos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Un día, cada fase una vez | 175.000 | 4.500.000 | 32.500.000 | 56.000 | 28.000 | 30 | 56 | 36 | 6.250 |
| La mejor semana: 7 × Fase 3 y 7 × Fase 2 | 1.050.000 | 27.300.000 | 192.500.000 | 336.000 | 168.000 | 175 | 224 | 182 | 37.800 |

La experiencia y el honor de una fase completada y pagada cuentan para tus puntos de ranking PvE: un punto por cada 1.000 de experiencia y uno por cada 100 de honor.

<!-- dungeons-totals:end -->

### Lo que pagan los alienígenas {#what-the-aliens-pay}

Cada alienígena de una mazmorra paga al caer, y suelta botín, como el alienígena del juego en el que se basa: un Dungeon Goombah como un [Goombah](/wiki/04-Aliens/Goombah.md), un Dungeon Crystalys y su Twin como un [Crystalys](/wiki/04-Aliens/Crystalys.md), un Dungeon Pirate como el Pirate Boss del [Enjambre Pirate](/wiki/05-Swarms/Pirate-Swarm.md). Lo que paga y suelta una baja es lo del original **multiplicado por la proporción entre el casco y el escudo de ambos juntos**: un alienígena tan resistente como su original paga lo que paga el original, uno el doble de resistente paga el doble y suelta el doble de cada objeto, y así sucesivamente. La sección de cada tipo de alienígena en [Los alienígenas](#the-aliens) da la proporción y el pago de una baja en cada fase.

- **Quién cobra.** Los pilotos que dañaron al alienígena, según el daño que hicieron, como con los alienígenas de los enjambres: un piloto o un grupo que apenas lo rozó no recibe nada, un grupo cobra como uno solo, y dentro de un grupo los miembros que están cerca de los restos y han disparado hace poco se reparten por nivel lo que se paga. Un piloto que no hizo daño al alienígena no cobra nada por él, por cerca que haya volado, y un alienígena al que ningún piloto dañó no paga a nadie. Solo entran los pilotos a los que pagan las reglas de arriba: quien se fue, no lleva dentro el tiempo suficiente, ya cobró hoy por la fase o ya tuvo todas las partidas pagadas de la semana no cobra nada por los alienígenas, y los demás se quedan con su parte. Una baja no pide la parte en el combate: haber dañado al alienígena es la parte. Si el miembro de un grupo que más daño hizo ha sido destruido o ya no está en el mapa, los miembros que están cerca de los restos y han disparado hace poco se reparten el pago sin él.
- **Qué se paga.** Créditos, Thulium, experiencia y honor, una vez por baja. El pago es lo que paga el original en Alpha, en todos los mundos: una mazmorra no tiene multiplicador de mundo. Tus potenciadores, formación y las bonificaciones de tu clan cuentan como en cualquier baja, y la experiencia cuenta para tus [puntos PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points) como la de la partida.
- **El botín.** Se tira con las probabilidades del original, salvo que el Echo Shard es el doble de probable y cae de dos en dos, y después cada cantidad se multiplica por la proporción (una fracción de unidad es una probabilidad de una más). Cae como una caja en los restos, primero para el piloto que más daño hizo y su clan, después para cualquiera en el mapa, y luego desaparece. Si el [grupo](/wiki/03-Mechanics/Groups.md) del piloto que más daño causó tiene dos o más pilotos que dañaron al alienígena y siguen volando en la mazmorra, el botín se reparte en cambio en [cajas personales](/wiki/03-Mechanics/Cargo.md#personal-crates), una para cada uno según el daño que causó, y cada una es primero solo de su piloto y después de cualquiera en el mapa. Un compañero de grupo que no causó daño o al que las reglas de arriba dejan fuera no recibe caja. Los demás grupos y los pilotos que vuelan solos cobran su parte y no reciben caja de este botín. El mapa admite solo cierto número de cajas a la vez, así que recógelas sobre la marcha, y lo que quede en el mapa cuando se cierra la mazmorra se va con ella. A diferencia de los objetos de la partida, son botín corriente de un alienígena: se pueden [vender en la Subasta](/wiki/03-Mechanics/Auction.md#marketable-items) si el objeto es Comercializable.
- **Lo que no paga.** El Señor de la guerra no paga baja, solo la partida. Los Goombahs que llama no pagan nada, porque la llamada se repite mientras dura el combate.
- **No es una baja del juego.** Una baja en una mazmorra no cuenta para misiones, logros, contadores de bajas, puntos de reinicio, los puntos PvE de una baja, drones ni P.E.T.s: un Dungeon Goombah no es un Goombah del juego.
- **Los límites.** Los límites diarios y semanales de arriba frenan el pago de los alienígenas igual que el de la partida: quien ya cobró hoy por la fase o ya tuvo todas las partidas pagadas de la semana tampoco cobra nada por sus alienígenas, y el bote de cada baja va a los demás. Una mazmorra que no se supera paga sus bajas a los pilotos a los que pagan las reglas, y nada por la partida.

## La recompensa del banco del clan {#clan-bank-reward}

El banco del clan también cobra, en créditos y no en Thulium, la primera vez que el clan supera una fase en una temporada. El clan tiene que tener suficiente antigüedad, y deben cobrar suficientes pilotos de esa partida. El banco cobra una vez por fase en una temporada.

<!-- dungeons-clan:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Créditos para el banco del clan |
| :--- | ---: |
| **Fase 1** | 10.000.000 |
| **Fase 2** | 20.000.000 |
| **Fase 3** | 30.000.000 |

- **Antigüedad del clan**: Al menos 3 d
- **Pilotos pagados**: Al menos 3 en la mazmorra

<!-- dungeons-clan:end -->

## Consejos {#tips}

- Acaba con la oleada de una zona antes de intentar mantenerla, y lucha dentro del anillo si entran alienígenas.
- Lleva a todo el grupo a una zona: cuantos más pilotos haya en el anillo, más rápido se mantiene.
- Busca a los Crystalys y sus Twins en el laberinto: la compuerta del Señor de la guerra se abre cuando tres cuartas partes de ellos están muertos, y no antes. Los demás alienígenas pueden esperar, o destruirse también.
- Usa las paredes: los láseres no las cruzan, los anillos rojos de las auras del Señor de la guerra se detienen en ellas, y una pared también detiene sus cohetes.
- Guarda una EMP Charge para la Andanada de cohetes.
- Cuando el Señor de la guerra llame a sus Goombahs, destrúyelos primero: no puede ser dañado hasta que desaparezcan. En la Zona del Caos, sal del anillo antes de disparar.
- Vigila el reloj de la ventana Mazmorra de clan. Cuando se acaba el tiempo, la mazmorra fracasa y la partida no paga nada.
