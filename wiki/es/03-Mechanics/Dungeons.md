<!-- wiki-i18n source: 76933ad9dd56b71f -->
<!-- wiki-i18n title: Mazmorras -->
# Mazmorras {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; portal; clan portal; join; clan gate alerts; clan dungeon window; start room; fog; guards; locked room; boss room; booster; boosters; swarm assist; focus most wanted; zone of chaos; rocket barrage; mazmorra; mazmorras; puerta; puertas; señor de la guerra; laberinto; fase; zona de botín; carta; portal; portal del clan; potenciador; potenciadores; niebla; guardianes; sala de inicio; sala bloqueada; apoyo de enjambre; zona del caos; avisos de puerta del clan -->

Una **mazmorra** es lo que el juego llama una **puerta**: un laberinto cerrado con un **Señor de la guerra** al final. Un colíder o el líder de un [clan](/wiki/03-Mechanics/Clans.md) abre una y la paga con el banco del clan, y los miembros del clan vuelan juntos hacia dentro como un solo [grupo](/wiki/03-Mechanics/Groups.md). Abren camino entre los alienígenas del laberinto, abren zonas de botín para elegir una carta en cada una y derrotan al Señor de la guerra. Todo piloto que participó en el combate cobra cuando cae el Señor de la guerra, dentro de los límites más abajo. Las puertas están en la pestaña **Puertas** de la página del clan.

Una puerta es un combate solo contra los alienígenas: nadie puede atacar dentro a un compañero de clan ni a nadie más. Los alienígenas no pagan nada. El pago es solo del Señor de la guerra, así que la única manera de cobrar es estar en el combate cuando cae.

## De un vistazo {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Se abre**: Desde el día 1 de la temporada
- **Quién abre una puerta**: Un colíder o el líder, que paga el precio con cargo al banco del clan
- **Grupo**: De 4 a 10 miembros del clan, en un mismo grupo
- **Puertas al día**: 3 por clan y día UTC, una abierta a la vez
- **Puertas a la vez**: 6 en un mundo
- **Mapas**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Laberintos**: 8; se elige uno al abrir una puerta
- **Reunión**: 10 min para reunirse y empezar. Una puerta que nadie inicia se cierra, y su precio vuelve al banco del clan
- **Límite de tiempo**: Fase 1: 95 min, Fase 2: 130 min, Fase 3: 165 min desde el inicio. Si se agota, la puerta fracasa y no paga nada
- **Vacía**: Una puerta sin nadie dentro durante 3 min fracasa
- **Cuando cae el Señor de la guerra**: La puerta sigue abierta 2 min para los pilotos que están dentro
- **Volver**: Un piloto que salió o fue destruido puede volver a entrar volando 3 veces, con 20 s entre una y otra

<!-- dungeons-glance:end -->

## Cómo es una partida {#how-a-run-goes}

1. **Invocar.** En la pestaña Puertas, un [colíder o el líder](/wiki/03-Mechanics/Clans.md#hierarchy-roles) elige una fase y pulsa **Invocar**. El precio sale del [banco del clan](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), y la puerta toma uno de los mapas de la lista de arriba. Una puerta que nadie inicia se cierra, y el precio vuelve al banco.
2. **Entrar.** Los miembros del clan pulsan **Entrar** en la ventana del Clan mientras vuelan, saltan por el portal del clan o pulsan **Unirse** en la tarjeta de aviso (consulta Entrar). Todos aparecen en la sala de inicio, y los pilotos de dentro son el grupo de la puerta.
3. **Iniciar.** La sala de inicio es una sala pequeña en un extremo del laberinto, y su compuerta está cerrada mientras la puerta espera a los pilotos. No hay alienígenas dentro, así que se puede esperar con seguridad. La puerta **se inicia sola** cuando están dentro todos los pilotos a los que espera y el grupo es lo bastante grande. Espera a los miembros del clan que están conectados, no ausentes y en el grupo de un piloto que ha entrado, y se inicia de inmediato cuando el grupo está lleno. El piloto que abrió la puerta, o un oficial, puede pulsar **Iniciar** para empezar antes con los pilotos que estén dentro, si son suficientes. Un piloto que se va deja de ser esperado. Cuando la puerta se inicia, la compuerta se abre para siempre, y después solo pueden volver los pilotos que ya estaban dentro.
4. **Abrirse paso por el laberinto.** Entras por un extremo del laberinto y el Señor de la guerra espera en el otro, en una sala bloqueada. El laberinto está a oscuras: solo ves lo que el grupo ha explorado y lo que está cerca de sus naves. Los alienígenas duermen en manadas en los pasillos, y una manada que despierta persigue al grupo por el laberinto.
5. **Abrir las zonas de botín.** Unos anillos en el laberinto marcan las zonas. Mantén una y el grupo vota una carta, que se paga junto con el pago del Señor de la guerra.
6. **Desbloquear la sala del Señor de la guerra.** Destruye a los guardianes, los Crystalys y sus Gemelos, y la compuerta de su sala se abre. Hasta entonces el Señor de la guerra no puede ser dañado.
7. **Derrotar al Señor de la guerra.** Rompe su escudo y su casco, y responde a sus habilidades. Cuando cae, la puerta queda superada.
8. **Cobrar.** El pago llega en el momento en que cae el Señor de la guerra. La puerta sigue abierta un poco más para los pilotos que están dentro y luego se cierra.

## Entrar {#entering}

Para entrar en una puerta necesitas una **nave en vuelo**, así que despega primero y abre después la ventana del Clan, y un [grupo](/wiki/03-Mechanics/Groups.md) con suficientes miembros del clan. También necesitas el **nivel** que pide la fase, y no puedes estar dentro de otra puerta. El grupo de la puerta tiene un tamaño máximo: cuando está lleno, nadie más puede entrar.

Un colíder o el líder abre una puerta, de una en una para el clan, y solo hasta el número de puertas al día. El banco del clan tiene que tener el precio. Un clan solo puede abrir una fase después de haber superado la anterior.

Dentro de una puerta no puedes cambiar de mundo, y la Jump CPU y la Base CPU no funcionan. El botón **Salir** de la ventana Puerta de clan te saca. Antes pide confirmación, salvo que el Señor de la guerra ya haya caído: entonces sales de inmediato. Un piloto que se fue, o que fue destruido, puede volver a entrar unas pocas veces, con una breve espera entre ellas.

### El portal del clan y el aviso {#the-clan-portal-and-the-call}

Cuando se abre una puerta, el clan recibe un **portal** para ella en el mapa de origen de cada corporación (`M-1`, `T-1` y `G-1`), un poco fuera de la zona segura de la estación. Solo los pilotos del clan lo ven: para todos los demás no existe. No tiene zona segura propia. Vuela hasta él y salta como en cualquier otro portal, y te lleva a la puerta con las reglas de **Entrar**: una nave en vuelo, un grupo con suficientes miembros del clan, el nivel de la fase y sitio en el grupo. Una vez iniciada la puerta, solo pueden usarlo los pilotos que ya estaban dentro. El portal desaparece cuando la puerta termina.

Mientras la puerta de tu clan espera a los pilotos y tú vuelas en otra parte, te llega un **aviso**: una tarjeta en la parte superior de la pantalla de vuelo, con un sonido. Dice quién abrió la puerta, cuántos pilotos hay dentro y cuánto tiempo seguirá abierta. **Unirse** te lleva dentro, igual que **Entrar** en la pestaña Puertas, y cuando sales de la puerta tu nave vuelve adonde estaba. Unirse aparece atenuado mientras tu grupo es demasiado pequeño. **Ahora no** oculta la tarjeta para esa puerta. Si tu grupo ya está dentro y la puerta te espera, la tarjeta lo dice. La tarjeta llega a los pilotos del clan que están volando (no a los que están atracados en una estación) y que tienen el nivel que pide la fase. Puedes desactivar la tarjeta y su sonido con **Avisos de puerta del clan** en Configuración › General › Grupos.

### La ventana Puerta de clan {#the-clan-dungeon-window}

Dentro de una puerta, la partida tiene una ventana propia, **Puerta de clan**. Muestra el tiempo transcurrido y el que queda, cuántos alienígenas vuelan y cuántos se han destruido, qué debe hacer el grupo ahora (explorar el laberinto, mantener una zona, encontrar al jefe, destruir a los guardianes, derrotar al Señor de la guerra), las barras de casco del grupo, la barra de la zona mientras estás en una, la habilidad del Señor de la guerra con su cuenta atrás y el botón **Salir**. Es una ventana como las demás: arrástrala por su barra de título y ciérrala con la luz roja de su esquina. Se abre sola cuando entras en una puerta, una vez por cada puerta: si la cierras, sigue cerrada hasta la siguiente puerta. La barra de herramientas tiene un botón **Puerta de clan** para ella mientras estás en una puerta. Con la ventana cerrada, una habilidad del Señor de la guerra que está a punto de empezar o en marcha aparece como una franja de una línea con su nombre y su cuenta atrás. Haz clic en la franja para volver a abrir la ventana.

## Las fases {#the-stages}

Una puerta tiene una fase, y la fase es su dificultad. Una fase superior tiene alienígenas más duros que golpean más fuerte, y paga más. Los multiplicadores de la tabla son los de los alienígenas. El daño se refiere a sus láseres y cohetes. El Señor de la guerra no sigue la tabla: tiene valores propios para cada fase, más abajo. La tabla también dice cuántos alienígenas envía una fase en comparación con la primera. El **precio** se toma del banco del clan cuando se abre la puerta.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Requisito | Casco y escudo de los alienígenas | Número de alienígenas | Daño de los alienígenas | Precio de la puerta (créditos, del banco del clan) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Fase 1** | Desde el nivel 6 | ×1 | ×1 | ×1 | 500.000 |
| **Fase 2** | Desde el nivel 7 | ×1,5 | ×1 | ×1,5 | 1.000.000 |
| **Fase 3** | Desde el nivel 8 | ×2 | ×1 | ×2 | 2.000.000 |

<!-- dungeons-stages:end -->

## El laberinto {#the-maze}

Cada puerta es un laberinto cerrado en un mapa propio, uno de los mapas de la lista de arriba, y el laberinto es uno de varios diseños. El laberinto ocupa todo el mapa, de borde a borde: una cuadrícula de salas y pasillos con paredes sólidas. Las naves no pueden cruzar una pared, y una pared bloquea los disparos, así que es una cobertura. Un meteoro cae desde arriba, y una pared no lo detiene.

**Salas y compuertas.** La sala de inicio, donde aterrizas, y la sala del Señor de la guerra, en el extremo lejano, tienen cada una una compuerta. Una compuerta cerrada es una pared para las naves, los disparos y los alienígenas por igual. La compuerta de inicio se abre cuando la puerta empieza. La del Señor de la guerra sigue bloqueada hasta que los guardianes son destruidos (consulta [La sala bloqueada](#the-locked-room)). Entre ambas, el laberinto tiene una sala de botín para cada zona de botín.

**Niebla.** El laberinto está a oscuras. En vuelo ves sus paredes y sus alienígenas solo donde ha estado el grupo, y a poca distancia alrededor de cada nave del grupo. Una sala cuenta como explorada en cuanto uno de vosotros está dentro. El minimapa funciona igual: es un plano de toda la planta que se va rellenando a medida que el grupo la explora, con la entrada, la compuerta de la sala del Señor de la guerra, las zonas que habéis encontrado y el Señor de la guerra cuando lo habéis encontrado. Los pilotos de tu propio grupo siempre se muestran.

## Los alienígenas {#the-aliens}

Cuatro tipos de alienígenas guardan el laberinto. Duermen en manadas en los pasillos, nunca en una sala, y una manada despierta cuando un piloto se acerca. Una manada despierta no te espera: persigue al grupo por el laberinto, y una manada que pierde a todos vuelve a donde dormía y se cura. Unas pocas manadas están despiertas desde el primer segundo, en los pasillos lejos de la entrada, hasta que un piloto se acerca. La puerta mantiene en el aire solo un número limitado de alienígenas a la vez, y ese número crece con el tamaño del grupo, así que una manada que despierta puede tener que esperar sitio, y una manada que destruyes deja entrar a la siguiente. Un grupo más grande se encuentra con más alienígenas en proporción, uno más pequeño con menos, y un tipo de alienígena nunca baja de uno.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Alienígenas, para un grupo de 5 | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 156 | 156 | 156 |
| Gate Pirate | 34 | 34 | 34 |
| Gate Crystalys | 34 | 34 | 34 |
| Gate Crystalys Twin | 11 | 11 | 11 |
| En total | 235 | 235 | 235 |
| La oleada de una zona de botín | 12 × Gate Goombah y 1 × Gate Crystalys | 12 × Gate Goombah y 1 × Gate Crystalys | 12 × Gate Goombah y 1 × Gate Crystalys |

- **Vivos a la vez**: Como máximo 10 por cada piloto del grupo, y 70 en total

<!-- dungeons-population:end -->

Cada tipo por turno. El casco y el escudo son los habituales multiplicados por el factor de la fase de la columna.

<!-- dungeons-enemies:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

### Gate Goombah

- **Se parece a**: Goombah
- **Vuela en manadas de**: 6

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 32.000 | 48.000 | 64.000 |
| Escudo | 48.000 | 72.000 | 96.000 |
| Daño de los láseres (una salva por segundo) | 3.000 | 4.500 | 6.000 |
| Velocidad | 180 | 180 | 180 |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | 1.800 | 1.800 | 1.800 |

### Gate Pirate

- **Se parece a**: Pirate Boss
- **Vuela en manadas de**: 2
- **Cohete**: Un cohete recto cada 5 s, alcance de 970 unidades

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 300.000 | 450.000 | 600.000 |
| Escudo | 50.100 | 75.150 | 100.200 |
| Daño de los láseres (una salva por segundo) | 200 | 300 | 400 |
| Daño de cohete | 5.000 | 7.500 | 10.000 |
| Velocidad | 92 | 92 | 92 |
| Alcance de los láseres | 700 | 700 | 700 |
| Radio de agresión | 1.800 | 1.800 | 1.800 |

### Gate Crystalys

- **Se parece a**: Crystalys
- **Vuela en manadas de**: 2

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 256.000 | 384.000 | 512.000 |
| Escudo | 160.000 | 240.000 | 320.000 |
| Daño de los láseres (una salva por segundo) | 10.000 | 15.000 | 20.000 |
| Velocidad | 230 | 230 | 230 |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | 2.400 | 2.400 | 2.400 |

### Gate Crystalys Twin

- **Se parece a**: Crystalys, 1,4 veces más grande
- **Vuela en manadas de**: 1

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 512.000 | 768.000 | 1.024.000 |
| Escudo | 320.000 | 480.000 | 640.000 |
| Daño de los láseres (una salva por segundo) | 20.000 | 30.000 | 40.000 |
| Velocidad | 230 | 230 | 230 |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## El Señor de la guerra {#the-warlord}

El Señor de la guerra espera en la sala del extremo lejano del laberinto, y es lo único de una puerta que paga. Es un Crystalys gigantesco. Su casco y su escudo crecen con el tamaño del grupo: cuantos más pilotos entran, más resistente es, en proporción. No sale nunca de su sala, con la puerta cerrada o abierta: se mantiene dentro de las paredes de la sala y no sale a cazar por los pasillos. Un piloto de fuera solo puede atraerlo hasta el borde de la sala, y aun así dispara por una puerta abierta a todo lo que alcanza su láser. Usa sus habilidades una a una, en orden aleatorio, cada una con su propia recarga.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Se parece a**: Crystalys, 3 veces más grande
- **Recarga del escudo**: 3.000 por segundo, tras 15 s sin recibir daño

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 10.000.000 | 15.000.000 | 25.000.000 |
| Escudo | 8.000.000 | 12.000.000 | 20.000.000 |
| Daño de los láseres (una salva por segundo) | 12.500–15.000 | 15.000–17.500 | 20.000–25.000 |
| Velocidad | 120 | 120 | 120 |
| Alcance de los láseres | 1.100 | 1.100 | 1.100 |

El casco y el escudo de arriba son para un grupo de 5. Crecen con el grupo: son el casco y el escudo del Señor de la guerra juntos, según el número de pilotos del grupo cuando empieza la puerta.

| Pilotos en el grupo | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| 4 | 14.400.000 | 21.600.000 | 36.000.000 |
| 5 | 18.000.000 | 27.000.000 | 45.000.000 |
| 6 | 21.600.000 | 32.400.000 | 54.000.000 |
| 7 | 25.200.000 | 37.800.000 | 63.000.000 |
| 8 | 28.800.000 | 43.200.000 | 72.000.000 |
| 9 | 32.400.000 | 48.600.000 | 81.000.000 |
| 10 | 36.000.000 | 54.000.000 | 90.000.000 |

<!-- dungeons-boss:end -->

### La sala bloqueada {#the-locked-room}

La compuerta de la sala del Señor de la guerra está cerrada desde el momento en que se abre la puerta, y mientras lo está el Señor de la guerra no puede ser dañado: ningún láser, cohete ni explosión lo toca, y no usa ninguna habilidad. La compuerta se abre para siempre cuando el grupo ha destruido a los **guardianes**: el Gate Crystalys y el Gate Crystalys Twin con los que se creó la puerta, alrededor de una quinta parte de sus alienígenas. El Gate Goombah y el Gate Pirate no cuentan, ni las oleadas de las zonas de botín ni los Goombahs que llama el Señor de la guerra.

La ventana Puerta de clan cuenta los guardianes que quedan y dice, en una etiqueta, que el Señor de la guerra no puede ser dañado, y un mensaje te avisa cuando la sala se desbloquea. Una manada de guardianes que sigue dormida cuenta entera, así que el grupo tiene que explorar el laberinto y encontrarlos a todos. En el minimapa la compuerta es una línea roja mientras está bloqueada y una verde cuando está abierta. Una puerta nunca es una trampa: el límite de tiempo sigue terminando una puerta cuyos últimos guardianes no se encuentran, y un administrador puede desbloquear la sala de una puerta atascada.

### Sus habilidades {#its-abilities}

- **El anillo rojo** del Aura de robo de vida hiere a todo piloto que está dentro y cura al Señor de la guerra con ese daño. La Absorción de escudo también tiene un anillo rojo: drena los escudos de los pilotos de dentro y carga el del Señor de la guerra. En ambos casos, sal del anillo o ponte detrás de una pared.
- **Los anillos ámbar** de la Lluvia de meteoros muestran dónde caerán los meteoros un instante después. Sigue moviéndote y sal del anillo antes de que caiga.
- **Foco en el más buscado** marca al piloto que más daño ha hecho al Señor de la guerra, con un corchete dorado en su nave, y el Señor de la guerra le dispara un tiro extra cada segundo mientras dura. Su puntería no cambia: sigue disparando al piloto más cercano que puede ver, así que un piloto marcado que además es el más cercano recibe ambos. El tiro extra necesita línea libre y el alcance del láser del Señor de la guerra, así que una pared o algo de distancia lo salva. No empieza mientras nadie haya hecho daño.
- **La Andanada de cohetes** lanza cohetes teledirigidos contra pilotos al azar, pero solo contra pilotos que el Señor de la guerra puede ver, y una pared en el camino detiene un cohete. Un anillo muestra a qué piloto sigue un cohete. Una EMP Charge o un camuflaje los despista.
- **El Apoyo de enjambre** es el Señor de la guerra llamando a sus Goombahs. Mientras viven, no puede ser dañado, y no dispara ni usa otra habilidad. Destrúyelos todos: el cartel de la habilidad cuenta cuántos quedan. Si pasa un minuto, el Señor de la guerra vuelve a poder ser dañado y los Goombahs que quedan siguen luchando. No son guardianes, y no pagan nada.
- **La Zona del Caos** es un anillo violeta en el suelo, alrededor del lugar donde estaba el Señor de la guerra cuando la lanzó. Nadie dentro del anillo puede atacar, ni con láseres ni con cohetes, aunque las reparaciones, el camuflaje y el vuelo siguen funcionando, y el Señor de la guerra y sus alienígenas disparan como siempre. El anillo aparece un momento antes de hacer efecto: sal de él, y dispara hacia dentro desde fuera.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Habilidad | Preparación | Duración | Recarga | Radio del anillo (unidades) | El Señor de la guerra recupera, como máximo |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura de robo de vida** | 2 s | 15 s | 2 min | 900 | 8 % de su casco y escudo |
| **Lluvia de meteoros** | 1,5 s | 3 salvas, con 4 s entre una y otra | 2 min | 420 | – |
| **Foco en el más buscado** | 1 s | 20 s | 2 min | – | – |
| **Andanada de cohetes** | 1,5 s | 45 s | 2 min | – | – |
| **Absorción de escudo** | 2 s | 15 s | 2 min | 900 | 6 % de su escudo |
| **Apoyo de enjambre** | 2 s | Hasta 1 min | 3 min | – | – |
| **Zona del Caos** | 2 s | 15 s | 2 min | 900 | – |

| Habilidad | Fase 1 | Fase 2 | Fase 3 |
| :--- | :--- | :--- | :--- |
| **Aura de robo de vida** | 8.000 por segundo | 10.000 por segundo | 12.000 por segundo |
| **Lluvia de meteoros** | 6 meteoros por salva, 40.000 cada uno | 8 meteoros por salva, 50.000 cada uno | 10 meteoros por salva, 60.000 cada uno |
| **Foco en el más buscado** | 18.750–22.500 por disparo adicional al piloto que más daño ha causado, uno cada 1 s | 22.500–26.250 por disparo adicional al piloto que más daño ha causado, uno cada 1 s | 30.000–37.500 por disparo adicional al piloto que más daño ha causado, uno cada 1 s |
| **Andanada de cohetes** | 6.500 por cohete, uno cada 15 s | 8.125 por cohete, uno cada 15 s | 9.750 por cohete, uno cada 15 s |
| **Absorción de escudo** | 10.000 de escudo por segundo | 12.500 de escudo por segundo | 15.000 de escudo por segundo |
| **Apoyo de enjambre** | 12 Goombahs | 18 Goombahs | 24 Goombahs |
| **Zona del Caos** | Los pilotos dentro del anillo no pueden atacar | Los pilotos dentro del anillo no pueden atacar | Los pilotos dentro del anillo no pueden atacar |

<!-- dungeons-abilities:end -->

## Zonas de botín {#loot-zones}

Un anillo en el suelo del laberinto marca cada zona de botín en cuanto el grupo la encuentra. Quédate un momento dentro y la zona despierta, y una oleada de alienígenas va a por ella. Entonces el grupo tiene que **mantener** la zona: dejar a un piloto dentro hasta que la barra se llene. Cuantos más pilotos haya en el anillo, más rápido se llena la barra: un número junto a la barra dice cuántas veces más rápido, y la tabla de abajo da los tiempos. Suficientes alienígenas en el anillo detienen la barra (la lista de abajo dice cuántos), y esta retrocede mientras no haya nadie dentro, así que acaba antes con la oleada. Cuando la zona se abre, el grupo ve tres cartas distintas y **vota** una. Una zona se abre una sola vez, y su oleada no vuelve.

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

En las fases 2 y 3, las oleadas de las zonas de botín traen también potenciadores. Cuando el grupo ha destruido a todos los alienígenas de una oleada, la oleada cuenta, y tras cada segunda oleada (la segunda, la cuarta y la sexta) cada piloto recibe una ventana de medio minuto para elegir un potenciador temporal para sí mismo: **Daño** (tus láseres golpean más fuerte), **Puntos de vida** (tu nave aguanta más casco) o **Velocidad** (tu nave vuela más rápido). Pulsa una carta para elegirla. Si no respondes a tiempo, el juego elige Puntos de vida por ti. Una elección vale un 3 % en la fase 3 y un 1,5 % en la fase 2, y un tipo suma como máximo un 9 % en la fase 3 y un 4,5 % en la fase 2, por muchas veces que lo elijas. La fase 1 no tiene potenciadores. Un grupo que deja viva una oleada no recibe ventana por ella.

Un potenciador dura hasta que se supera la puerta. Si sales de la puerta o eres destruido, pierdes tus potenciadores, y los recuperas cuando vuelves a entrar. Una etiqueta bajo la ventana Puerta de clan muestra lo que tienes.

### Las cartas {#the-cards}

Las cartas se sacan una a una del conjunto de abajo. La probabilidad es la de una carta en un sorteo. Cada carta va a todos los pilotos que cobran, también las de equipo: una carta con muchas copias da a cada uno todas esas copias, y una carta de equipo da a cada uno una pieza propia, forjada para él. Un piloto que no cobra tampoco recibe carta, y una zona abierta en una puerta que fracasa no paga nada.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carta | Fase 1 | Fase 2 | Fase 3 | Probabilidad | Para |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | 23,9 % | Cada piloto pagado |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 13,65 % | Cada piloto pagado |
| Velkonite | 200 | 300 | 500 | 13,65 % | Cada piloto pagado |
| Orvium | 200 | 300 | 500 | 13,65 % | Cada piloto pagado |
| Ultra Core | 5.000 | 7.500 | 12.500 | 11,4 % | Cada piloto pagado |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 9,1 % | Cada piloto pagado |
| Dark Matter | 5 | 8 | 12 | 9,1 % | Cada piloto pagado |
| Dark Matter Plate | 1 | 1 | 2 | 4,55 % | Cada piloto pagado |
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

Las cartas con una sola copia son **equipo**, y solo una puerta de fase 3 puede ofrecerlas. Una pieza de equipo se forja para cada piloto que cobra, al pagarse: cada uno saca su propio [grado de encantamiento](/wiki/06-Items/Overview.md#item-enchants) con las mismas probabilidades que una pieza que construyes en Ensamblaje, así que la mayoría sale Estándar, y un grado superior, hasta Eterno, con mejoras, es un hallazgo raro.

## Pago {#pay}

Cuando cae el Señor de la guerra, todo piloto que se lo ha ganado cobra, una vez por partida. Las cartas que eligió el grupo se suman al pago de la fase. No hay multiplicador de mundo: el pago es el mismo en todos los mundos.

Las **Orvium Reinforced Plates** no son una carta de la votación. Forman parte del pago de la fase, y cada piloto que cobra las recibe una vez por partida. Los objetos que paga una puerta no son Comercializables: no puedes [venderlos en la Subasta](/wiki/03-Mechanics/Auction.md#marketable-items).

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Honor | Experiencia | Créditos | Thulium | Munición x4 | Orvium Reinforced Plates | Puntos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Fase 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 5 | 600 |
| **Fase 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 10 | 1.500 |
| **Fase 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 15 | 2.400 |

<!-- dungeons-pay:end -->

### Quién cobra {#who-is-paid}

Los alienígenas nunca pagan. Una partida se juega entera aunque no pague nada, y la pantalla de resultados dice por qué. Nunca se te niega la entrada por haber cobrado ya una fase: esa partida simplemente no paga.

<!-- dungeons-rules:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Un día**: Una fase paga a un piloto una vez por día UTC: el día en que cae el Señor de la guerra
- **Una semana**: Un piloto cobra como máximo 10 fases completadas por semana UTC, de lunes a domingo
- **Dentro**: Al menos 2 min en total
- **Parte en el combate**: Al menos una de estas: infligió 2 % del casco y el escudo del Señor de la guerra; destruyó 10 de los alienígenas de la puerta; curó a otros pilotos por 50.000 durante el combate contra el Señor de la guerra

<!-- dungeons-rules:end -->

### Lo que valen un día y una semana {#what-a-day-and-a-week-are-worth}

Lo que un piloto puede cobrar en un día y en la mejor semana que permiten los límites. La última columna es lo que el pago suma a tus [puntos PvE](/wiki/03-Mechanics/Ranks.md#how-you-earn-pve-points).

<!-- dungeons-totals:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Pago por piloto | Honor | Experiencia | Créditos | Thulium | Munición x4 | Orvium Reinforced Plates | Puntos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Un día, cada fase una vez | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 30 | 4.500 |
| La mejor semana: 7 × Fase 3 y 3 × Fase 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 135 | 21.300 |

La experiencia de una fase completada y pagada cuenta para tus puntos de ranking PvE: un punto por cada 1.000 de experiencia.

<!-- dungeons-totals:end -->

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
- **Pilotos pagados**: Al menos 3 en la puerta

<!-- dungeons-clan:end -->

## Consejos {#tips}

- Acaba con la oleada de una zona antes de intentar mantenerla, y lucha dentro del anillo si entran alienígenas.
- Lleva a todo el grupo a una zona: cuantos más pilotos haya en el anillo, más rápido se mantiene.
- Explora cada rincón del laberinto: una manada de guardianes que nunca encuentras mantiene cerrada la compuerta del Señor de la guerra.
- Usa las paredes: los láseres no las cruzan, los anillos rojos de las auras del Señor de la guerra se detienen en ellas, y una pared también detiene sus cohetes.
- Guarda una EMP Charge para la Andanada de cohetes.
- Cuando el Señor de la guerra llame a sus Goombahs, destrúyelos primero: no puede ser dañado hasta que desaparezcan. En la Zona del Caos, sal del anillo antes de disparar.
- Vigila el reloj de la ventana Puerta de clan. Cuando se acaba el tiempo, la puerta fracasa y no paga nada.
