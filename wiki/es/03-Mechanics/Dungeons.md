<!-- wiki-i18n source: a3ead40fe6402d78 -->
<!-- wiki-i18n title: Mazmorras -->
# Mazmorras {#dungeons}

<!-- wiki-search: dungeon; dungeons; gate; gates; clan gate; clan gates; clan dungeon; summon; warlord; gate warlord; boss; maze; loot zone; chest; card; vote; stage; instance; gate delta; gate epsilon; gate zeta; gate eta; gate theta; gate iota; gate goombah; gate pirate; gate crystalys; mazmorra; mazmorras; puerta; puertas; señor de la guerra; laberinto; fase; zona de botín; carta -->

Una **mazmorra** es lo que el juego llama una **puerta**: un laberinto cerrado con un **Señor de la guerra** al final. Un colíder o el líder de un [clan](/wiki/03-Mechanics/Clans.md) abre una y la paga con el banco del clan, y los miembros del clan vuelan juntos hacia dentro como un solo [grupo](/wiki/03-Mechanics/Groups.md). Abren camino entre los alienígenas del laberinto, abren zonas de botín para elegir una carta en cada una y derrotan al Señor de la guerra. Todo piloto que participó en el combate cobra cuando cae el Señor de la guerra, dentro de los límites más abajo. Las puertas están en la pestaña **Puertas** de la página del clan.

Una puerta es un combate solo contra los alienígenas: nadie puede atacar dentro a un compañero de clan ni a nadie más. Los alienígenas no pagan nada. El pago es solo del Señor de la guerra, así que la única manera de cobrar es estar en el combate cuando cae.

## De un vistazo {#at-a-glance}

<!-- dungeons-glance:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Se abre**: Desde el día 4 de la temporada
- **Quién abre una puerta**: Un colíder o el líder, que paga el precio con cargo al banco del clan
- **Grupo**: De 4 a 10 miembros del clan, en un mismo grupo
- **Puertas al día**: 3 por clan y día UTC, una abierta a la vez
- **Puertas a la vez**: 6 en un mundo
- **Mapas**: Gate Delta, Gate Epsilon, Gate Zeta, Gate Eta, Gate Theta, Gate Iota
- **Laberintos**: 8; se elige uno al abrir una puerta
- **Reunión**: 10 min para reunirse y empezar. Una puerta que nadie inicia se cierra, y su precio vuelve al banco del clan
- **Límite de tiempo**: Fase 1: 80 min, Fase 2: 110 min, Fase 3: 150 min desde el inicio. Si se agota, la puerta fracasa y no paga nada
- **Vacía**: Una puerta sin nadie dentro durante 3 min fracasa
- **Cuando cae el Señor de la guerra**: La puerta sigue abierta 2 min para los pilotos que están dentro
- **Volver**: Un piloto que salió o fue destruido puede volver a entrar volando 3 veces, con 20 s entre una y otra

<!-- dungeons-glance:end -->

## Cómo es una partida {#how-a-run-goes}

1. **Invocar.** En la pestaña Puertas, un [colíder o el líder](/wiki/03-Mechanics/Clans.md#hierarchy-roles) elige una fase y pulsa **Invocar**. El precio sale del [banco del clan](/wiki/03-Mechanics/Clans.md#clan-economy-taxation), y la puerta toma uno de los mapas de la lista de arriba. Una puerta que nadie inicia se cierra, y el precio vuelve al banco.
2. **Entrar.** Los miembros del clan pulsan **Entrar** en la ventana del Clan mientras vuelan. Los pilotos que están dentro forman el grupo de la puerta.
3. **Iniciar.** El piloto que abrió la puerta, o un oficial, pulsa **Iniciar** cuando hay suficientes pilotos dentro. Después solo pueden volver los pilotos que ya estaban dentro.
4. **Abrirse paso por el laberinto.** Entras por un extremo del laberinto y el Señor de la guerra espera en el otro. Los alienígenas duermen en sus salas y despiertan en grupos cuando el grupo se acerca.
5. **Abrir las zonas de botín.** Unos anillos en el laberinto marcan las zonas. Mantén una y el grupo vota una carta, que se paga junto con el pago del Señor de la guerra.
6. **Derrotar al Señor de la guerra.** Rompe su escudo y su casco, y responde a sus habilidades. Cuando cae, la puerta queda superada.
7. **Cobrar.** El pago llega en el momento en que cae el Señor de la guerra. La puerta sigue abierta un poco más para los pilotos que están dentro y luego se cierra.

## Entrar {#entering}

Para entrar en una puerta necesitas una **nave en vuelo**, así que despega primero y abre después la ventana del Clan, y un [grupo](/wiki/03-Mechanics/Groups.md) con suficientes miembros del clan. También necesitas el **nivel** que pide la fase, y no puedes estar dentro de otra puerta. El grupo de la puerta tiene un tamaño máximo: cuando está lleno, nadie más puede entrar.

Un colíder o el líder abre una puerta, de una en una para el clan, y solo hasta el número de puertas al día. El banco del clan tiene que tener el precio. Un clan solo puede abrir una fase después de haber superado la anterior.

Dentro de una puerta no puedes cambiar de mundo, y la Jump CPU y la Base CPU no funcionan. El botón **Salir** de la barra de la puerta te saca después de confirmar. Un piloto que se fue, o que fue destruido, puede volver a entrar unas pocas veces, con una breve espera entre ellas.

## Las fases {#the-stages}

Una puerta tiene una fase, y la fase es su dificultad. Una fase más alta tiene alienígenas más resistentes que golpean más fuerte, y paga más. Los multiplicadores de la tabla se aplican a todos los alienígenas y al Señor de la guerra. Daño significa láseres, cohetes y las habilidades del Señor de la guerra. La tabla también dice cuántos alienígenas envía una fase en comparación con la primera. El **precio** se toma del banco del clan cuando se abre la puerta.

<!-- dungeons-stages:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Requisito | Casco y escudo de los alienígenas | Número de alienígenas | Daño de los alienígenas | Precio de la puerta (créditos, del banco del clan) |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Fase 1** | Desde el nivel 6 | ×1 | ×1 | ×1 | 500.000 |
| **Fase 2** | Desde el nivel 7 | ×1,5 | ×1 | ×1,25 | 1.000.000 |
| **Fase 3** | Desde el nivel 8 | ×2,5 | ×1 | ×1,5 | 2.000.000 |

<!-- dungeons-stages:end -->

## El laberinto {#the-maze}

Cada puerta es un laberinto cerrado en un mapa propio, uno de los mapas de la lista de arriba, y el laberinto es uno de varios diseños. Un laberinto es una cuadrícula de salas y pasillos con paredes sólidas. Las naves no pueden cruzar una pared, y una pared bloquea los disparos, así que sirve de cobertura. Un meteoro cae desde arriba, y una pared no lo detiene.

## Los alienígenas {#the-aliens}

Cuatro tipos de alienígenas guardan el laberinto. Duermen en sus salas y despiertan cuando un piloto se acerca. La puerta mantiene en el aire solo un número limitado de alienígenas a la vez, y ese número crece con el tamaño del grupo, así que un grupo de alienígenas que destruyes deja entrar al siguiente. Un grupo más grande se encuentra con más alienígenas en proporción, uno más pequeño con menos, y un tipo de alienígena nunca baja de uno.

<!-- dungeons-population:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Alienígenas, para un grupo de 5 | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Gate Goombah | 130 | 130 | 130 |
| Gate Pirate | 28 | 28 | 28 |
| Gate Crystalys | 28 | 28 | 28 |
| Gate Crystalys Twin | 9 | 9 | 9 |
| En total | 195 | 195 | 195 |
| La oleada de una zona de botín | 10 × Gate Goombah y 1 × Gate Crystalys | 10 × Gate Goombah y 1 × Gate Crystalys | 10 × Gate Goombah y 1 × Gate Crystalys |

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
| Casco | 32.000 | 48.000 | 80.000 |
| Escudo | 48.000 | 72.000 | 120.000 |
| Daño de los láseres (una salva por segundo) | 3.000 | 3.750 | 4.500 |
| Velocidad | 180 | 180 | 180 |
| Alcance de los láseres | 800 | 800 | 800 |
| Radio de agresión | 1.800 | 1.800 | 1.800 |

### Gate Pirate

- **Se parece a**: Pirate Boss
- **Vuela en manadas de**: 2
- **Cohete**: Un cohete recto cada 5 s, alcance de 970 unidades

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 300.000 | 450.000 | 750.000 |
| Escudo | 50.100 | 75.150 | 125.250 |
| Daño de los láseres (una salva por segundo) | 200 | 250 | 300 |
| Daño de cohete | 5.000 | 6.250 | 7.500 |
| Velocidad | 92 | 92 | 92 |
| Alcance de los láseres | 700 | 700 | 700 |
| Radio de agresión | 1.800 | 1.800 | 1.800 |

### Gate Crystalys

- **Se parece a**: Crystalys
- **Vuela en manadas de**: 2

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 256.000 | 384.000 | 640.000 |
| Escudo | 160.000 | 240.000 | 400.000 |
| Daño de los láseres (una salva por segundo) | 10.000 | 12.500 | 15.000 |
| Velocidad | 230 | 230 | 230 |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | 2.400 | 2.400 | 2.400 |

### Gate Crystalys Twin

- **Se parece a**: Crystalys, 1,4 veces más grande
- **Vuela en manadas de**: 1

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 512.000 | 768.000 | 1.280.000 |
| Escudo | 320.000 | 480.000 | 800.000 |
| Daño de los láseres (una salva por segundo) | 20.000 | 25.000 | 30.000 |
| Velocidad | 230 | 230 | 230 |
| Alcance de los láseres | 900 | 900 | 900 |
| Radio de agresión | 2.400 | 2.400 | 2.400 |

<!-- dungeons-enemies:end -->

## El Señor de la guerra {#the-warlord}

El Señor de la guerra espera en la sala del extremo lejano del laberinto, y es lo único de una puerta que paga. Es un Crystalys gigantesco. Su casco y su escudo crecen con el tamaño del grupo: cuantos más pilotos entran, más resistente es, en proporción. Se queda en su sala y usa sus habilidades una a una, en orden aleatorio, cada una con su propia recarga.

<!-- dungeons-boss:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Se parece a**: Crystalys, 3 veces más grande
- **Recarga del escudo**: 3.000 por segundo, tras 15 s sin recibir daño

|  | Fase 1 | Fase 2 | Fase 3 |
| :--- | ---: | ---: | ---: |
| Casco | 10.000.000 | 15.000.000 | 25.000.000 |
| Escudo | 8.000.000 | 12.000.000 | 20.000.000 |
| Daño de los láseres (una salva por segundo) | 8.000 | 10.000 | 12.000 |
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

### Sus habilidades {#its-abilities}

- **El anillo rojo** del Aura de robo de vida hiere a todo piloto que está dentro y cura al Señor de la guerra con ese daño. La Absorción de escudo también tiene un anillo rojo: drena los escudos de los pilotos de dentro y carga el del Señor de la guerra. En ambos casos, sal del anillo o ponte detrás de una pared.
- **Los anillos ámbar** de la Lluvia de meteoros muestran dónde caerán los meteoros un instante después. Sigue moviéndote y sal del anillo antes de que caiga.
- **Objetivo: los sanadores** vuelve al Señor de la guerra contra quien cura a otro piloto, y golpea más fuerte a ese piloto. Reparte las curaciones.
- **La Andanada de cohetes** lanza cohetes teledirigidos contra pilotos al azar. Una EMP Charge o un camuflaje los despista.

<!-- dungeons-abilities:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Habilidad | Preparación | Duración | Recarga | Radio del anillo (unidades) | El Señor de la guerra recupera, como máximo |
| :--- | ---: | :--- | ---: | ---: | :--- |
| **Aura de robo de vida** | 2 s | 15 s | 2 min | 900 | 8 % de su casco y escudo |
| **Lluvia de meteoros** | 1,5 s | 3 salvas, con 4 s entre una y otra | 2 min | 420 | – |
| **Objetivo: los sanadores** | 1 s | 45 s | 2 min | – | – |
| **Andanada de cohetes** | 1,5 s | 45 s | 2 min | – | – |
| **Absorción de escudo** | 2 s | 15 s | 2 min | 900 | 6 % de su escudo |

| Habilidad | Fase 1 | Fase 2 | Fase 3 |
| :--- | :--- | :--- | :--- |
| **Aura de robo de vida** | 8.000 por segundo | 10.000 por segundo | 12.000 por segundo |
| **Lluvia de meteoros** | 6 meteoros por salva, 40.000 cada uno | 8 meteoros por salva, 50.000 cada uno | 10 meteoros por salva, 60.000 cada uno |
| **Objetivo: los sanadores** | Su láser golpea con ×1,5 de fuerza al piloto contra el que se vuelve | Su láser golpea con ×1,5 de fuerza al piloto contra el que se vuelve | Su láser golpea con ×1,5 de fuerza al piloto contra el que se vuelve |
| **Andanada de cohetes** | 6.500 por cohete, uno cada 15 s | 8.125 por cohete, uno cada 15 s | 9.750 por cohete, uno cada 15 s |
| **Absorción de escudo** | 10.000 de escudo por segundo | 12.500 de escudo por segundo | 15.000 de escudo por segundo |

<!-- dungeons-abilities:end -->

## Zonas de botín {#loot-zones}

Un anillo en el suelo del laberinto marca cada zona de botín en cuanto el grupo la encuentra. Quédate un momento dentro y la zona despierta, y una oleada de alienígenas va a por ella. Entonces el grupo tiene que **mantener** la zona: dejar a un piloto dentro hasta que la barra se llene. Los alienígenas en el anillo detienen la barra, y esta retrocede mientras no haya nadie dentro, así que acaba antes con la oleada. Cuando la zona se abre, el grupo ve tres cartas distintas y **vota** una. Una zona se abre una sola vez, y su oleada no vuelve.

<!-- dungeons-zones:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

- **Zonas de botín**: 4 en cada laberinto
- **Radio**: 450 unidades
- **Despertar**: Quédate dentro del anillo 2 s
- **Mantener**: Mantén a un piloto dentro durante 30 s. La barra se detiene mientras haya 3 o más alienígenas en el anillo y retrocede mientras no haya nadie
- **Elegir**: El grupo tiene 45 s para votar. La votación termina antes si todos los pilotos presentes han votado o si una carta tiene más de la mitad de los votos

<!-- dungeons-zones:end -->

### Las cartas {#the-cards}

Las cartas se sacan una a una del conjunto de abajo. La probabilidad es la de una carta en un sorteo. Una carta con muchas copias va a todos los pilotos que cobran, y una carta de equipo, con una sola copia, va a un piloto del grupo. Un piloto que no cobra tampoco recibe carta, y una zona abierta en una puerta que fracasa no paga nada.

<!-- dungeons-cards:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Carta | Fase 1 | Fase 2 | Fase 3 | Probabilidad | Para |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Thulium | 2.000 | 3.000 | 5.000 | 21 % | Cada piloto pagado |
| Velkonite Reinforced Plate | 10 | 15 | 25 | 12 % | Cada piloto pagado |
| Orvium Reinforced Plate | 10 | 15 | 25 | 12 % | Cada piloto pagado |
| Velkonite | 200 | 300 | 500 | 12 % | Cada piloto pagado |
| Orvium | 200 | 300 | 500 | 12 % | Cada piloto pagado |
| Ultra Core | 5.000 | 7.500 | 12.500 | 10 % | Cada piloto pagado |
| Experimental Fusion Core | 3.000 | 4.500 | 7.500 | 8 % | Cada piloto pagado |
| Dark Matter | 5 | 8 | 12 | 8 % | Cada piloto pagado |
| Dark Matter Plate | 1 | 1 | 2 | 4 % | Cada piloto pagado |
| Engine III | 1 | 1 | 1 | 0,25 % | Un piloto del grupo |
| Heavy Shield Core | 1 | 1 | 1 | 0,25 % | Un piloto del grupo |
| Adaptive Core III | 1 | 1 | 1 | 0,25 % | Un piloto del grupo |
| Starfire-III | 1 | 1 | 1 | 0,25 % | Un piloto del grupo |

- **Equipo**: Las cartas con un solo ejemplar son equipo: juntas, 1 % de las cartas

<!-- dungeons-cards:end -->

## Pago {#pay}

Cuando cae el Señor de la guerra, todo piloto que se lo ha ganado cobra, una vez por partida. Las cartas que eligió el grupo se suman al pago de la fase. No hay multiplicador de mundo: el pago es el mismo en todos los mundos.

<!-- dungeons-pay:begin -->
<!-- Generated from server/Resources/Dungeons.json (and DungeonMazes.json, client/locales/<language>/dungeon.toml) by scripts/dungeons-wiki.sh: don't edit by hand. -->

| Fase | Honor | Experiencia | Créditos | Thulium | Munición x4 | Puntos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| **Fase 1** | 25.000 | 600.000 | 5.000.000 | 4.000 | 4.000 | 600 |
| **Fase 2** | 50.000 | 1.500.000 | 10.000.000 | 9.000 | 9.000 | 1.500 |
| **Fase 3** | 100.000 | 2.400.000 | 17.500.000 | 15.000 | 15.000 | 2.400 |

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

| Pago por piloto | Honor | Experiencia | Créditos | Thulium | Munición x4 | Puntos de ranking PvE |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Un día, cada fase una vez | 175.000 | 4.500.000 | 32.500.000 | 28.000 | 28.000 | 4.500 |
| La mejor semana: 7 × Fase 3 y 3 × Fase 2 | 850.000 | 21.300.000 | 152.500.000 | 132.000 | 132.000 | 21.300 |

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
- Usa las paredes: los láseres no las cruzan, y los anillos del Señor de la guerra se detienen en ellas.
- Guarda una EMP Charge para la Andanada de cohetes.
- Vigila el reloj de la barra de la puerta. Cuando se acaba el tiempo, la puerta fracasa y no paga nada.
