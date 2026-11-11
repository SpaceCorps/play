<!-- wiki-i18n source: d75ffd5e6e894c46 -->
<!-- wiki-i18n title: Destrezas de piloto -->
# Destrezas de piloto {#pilot-skills}

<!-- wiki-search: skills; skill tree; pilot skill tree; pilot skills; skill xp; xp; level up; stats; attributes; heft; grit; reflex; instinct; laser tech; rocket tech; antimatter; marksmanship; sabotage; evasion; tactics; radiation tech; thruster theory; science; extraction; logistics; fabrication; commerce; soft cap; hold; training; day one; pilot button; pilot page; buffs; destrezas; destrezas de piloto; árbol de destrezas; experiencia; subir de nivel; estadísticas; atributos; masa; temple; reflejos; instinto; tecnología láser; tecnología de cohetes; antimateria; puntería; sabotaje; evasión; táctica; tecnología de radiación; teoría de propulsores; ciencia; extracción; logística; fabricación; comercio; límite por hora; bodega -->

Tu piloto tiene un **árbol de destrezas**: un conjunto de estadísticas que suben de nivel según lo que haces. Combate, y suben tu Tecnología láser y tu Temple; recoge de tu Skylab, y sube tu Extracción. Cada nivel da un pequeño bonificador permanente a algo que ya haces, y no se gasta ni se elige nada: no hay puntos que repartir ni nada que reasignar. Subes de nivel lo que usas.

El árbol es **tuyo**, no de una nave. Cada nave que pilotas tiene tus niveles, también la que compres mañana, y los niveles se conservan en todos los reinicios ([qué se conserva](#what-is-kept)).

Un piloto nuevo no tiene toda su fuerza. En el nivel 1 un láser y un cohete hacen menos daño del que indican las páginas de objetos, y la Tecnología láser y la Tecnología de cohetes lo llevan más allá de las cifras indicadas a medida que suben. Cada cifra de las páginas de objetos es la del propio objeto, antes de tus destrezas.

## De un vistazo {#at-a-glance}

<!-- skills-glance:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

- **Estadísticas**: 18 estadísticas: 4 atributos y 14 destrezas en 5 grupos
- **Niveles**: De 1 a 100. Todo piloto empieza cada estadística en el nivel 1, y no hay nada que gastar ni que reasignar
- **Coste de un nivel**: 40 XP del nivel 1 al 2, 875 XP del nivel 50 al 51, 19.157 XP del nivel 99 al 100; 313.258 XP en total
- **Lo que da un nivel**: Un bonificador crece en línea recta desde su valor en el nivel 1 hasta su valor en el nivel 100. Nada tiene límite
- **Tu láser en el nivel 1**: Hace el 80 % de su daño y acierta el 80 % de las veces, es decir, el 64 % del daño que indican las páginas de objetos
- **Tu cohete en el nivel 1**: Hace el 80 % de su daño y falla al encenderse el 20 % de las veces, es decir, el 64 % del daño que indican las páginas de objetos
- **Esquiva**: La nave de todo piloto esquiva el 3 % de los impactos que se pueden esquivar, antes de que ninguna destreza o formación sume
- **Nivel de casco**: La rareza de tu nave lo fija, como muestra la tabla de abajo. El tamaño de tu bodega y la XP de la Masa lo siguen
- **Bodega**: Cuenta las unidades de recursos que recoges después de despegar, hasta el tamaño que le da su nivel de casco. Está llena desde el 90 % de eso, y una bodega llena hace que la Masa pague ×1,5. Nunca se rechaza nada
- **Límite blando por hora**: La mayoría de las estadísticas pagan la XP completa solo hasta un límite por hora, contado en la unidad propia de la estadística durante la hora del reloj UTC. Por encima, un evento paga el 25 % de su XP
- **Entrenamiento**: La XP de una destreza también paga el 10 % de sí misma a su atributo. Un atributo en el nivel 100 entrena sus destrezas un 25 % más rápido que en el nivel 1

| Nivel de casco | Rareza de la nave | Tamaño de la bodega |
| :--- | :--- | ---: |
| 1 | Deficiente / Común | 60 |
| 2 | Poco común | 120 |
| 3 | Raro | 250 |
| 4 | Épico | 500 |
| 5 | Mítico / Legendario / Eterno | 1.000 |

<!-- skills-glance:end -->

## Las estadísticas {#the-stats}

Las estadísticas son de dos tipos. Los **atributos** (Masa, Temple, Reflejos e Instinto) son lo básico de un piloto. Las **destrezas** están en cinco grupos, y cada una está regida por un atributo, que las tablas nombran entre paréntesis: la XP de una destreza también alimenta a su atributo, y un atributo alto entrena más rápido a sus destrezas ([cómo se paga la XP](#how-xp-is-paid)). Los nombres son los de la página Destrezas de piloto del juego.

Las tablas dan cada bonificador en el nivel 1 y en el último nivel; entre ambos crece en línea recta. Un **factor** multiplica una cifra: uno por encima de 1 la hace mayor, uno por debajo de 1 menor. La mayoría de los bonificadores cambian una cifra de tu nave, y la descripción emergente de una cifra que una destreza ha movido tiene una línea que dice cuánto viene de tus destrezas.

<!-- skills-buffs:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

### Atributos {#attributes}

| Estadística | Qué cambia | Nivel 1 | Nivel 100 |
| :--- | :--- | ---: | ---: |
| **Masa** | Casco | +0 % | +10 % |
| **Temple** | Daño recibido | ×1 | ×0,9 |
| **Reflejos** | Velocidad de recarga de habilidades | ×1 | ×1,11 |
| **Instinto** | Probabilidad de cada línea de botín | +0 puntos | +5 puntos |
|  | Orvium y Velkonite de los colectores | ×1 | ×1,5 |

### Armas {#weapons}

| Estadística | Qué cambia | Nivel 1 | Nivel 100 |
| :--- | :--- | ---: | ---: |
| **Tecnología láser** (Reflejos) | Daño láser | ×0,8 | ×1,1 |
|  | Probabilidad de que una ráfaga láser acierte | 80 % | 90 % |
| **Tecnología de cohetes** (Reflejos) | Daño de cohete | ×0,8 | ×1,1 |
|  | Probabilidad de que un cohete falle al encenderse | 20 % | 0 % |
| **Antimateria** (Instinto) | Dark Matter de las recogidas | ×1 | ×1,25 |

### Combate {#combat}

| Estadística | Qué cambia | Nivel 1 | Nivel 100 |
| :--- | :--- | ---: | ---: |
| **Puntería** (Reflejos) | Alcance del lanzamiento de una Mine | ×1 | ×1,15 |
|  | Velocidad de una Mine lanzada | ×1 | ×1,15 |
| **Sabotaje** (Reflejos) | Daño de venenos y Mines | ×1 | ×1,3 |
|  | Duración de los venenos | ×1 | ×1,2 |
| **Evasión** (Reflejos) | Probabilidad de esquivar un golpe, sumada a la propia de la nave | 0 % | 15 % |
| **Táctica** (Reflejos) | Duración de las habilidades | ×1 | ×1,2 |

### Control de la nave {#ship-control}

| Estadística | Qué cambia | Nivel 1 | Nivel 100 |
| :--- | :--- | ---: | ---: |
| **Tecnología de radiación** (Temple) | Dosis de radiación | ×1 | ×0,4 |
| **Teoría de propulsores** (Masa) | Velocidad | +0 % | +15 % |
| **Ciencia** (Instinto) | Ciencia por cada unidad de combustible | ×1 | ×1,25 |

### Skylab

| Estadística | Qué cambia | Nivel 1 | Nivel 100 |
| :--- | :--- | ---: | ---: |
| **Extracción** (Instinto) | Lo que produce el Skylab | ×1 | ×1,3 |
| **Logística** (Masa) | Lo que guarda el banco del Almacén de recursos | ×1 | ×1,4 |
| **Fabricación** (Reflejos) | Tiempo de una fabricación | ×1 | ×0,65 |

### Comercio {#trading}

| Estadística | Qué cambia | Nivel 1 | Nivel 100 |
| :--- | :--- | ---: | ---: |
| **Comercio** (Instinto) | Precios de la tienda | ×1 | ×0,85 |
|  | Lo que paga la tienda al recomprar | ×1 | ×1,1 |
|  | Tarifa de un anuncio de la Subasta | ×1 | ×0,5 |


<!-- skills-buffs:end -->

## Dónde lo notas {#where-you-feel-it}

- **Láseres.** La Tecnología láser cambia el daño de cada ráfaga y la probabilidad de que acierte; una ráfaga que se desvía muestra un «Miss» flotante y gasta igualmente su munición ([Combate](/wiki/03-Mechanics/Combat.md#laser-tech)). El alcance de tus láseres es el de tu nave: la Puntería sube con tus impactos con munición distinta de la simple x1, pero solo actúa sobre las Mines (abajo).
- **Cohetes.** La Tecnología de cohetes cambia el daño de cada cohete y la probabilidad de que uno falle al encenderse ([Tecnología de cohetes](/wiki/06-Items/Rockets.md#rocket-tech)).
- **Recibir golpes.** El Temple quita una parte de cada golpe que recibes, y la Evasión aumenta la probabilidad de que un impacto directo no haga nada ([Combate](/wiki/03-Mechanics/Combat.md#grit-and-evasion)). La Masa aumenta tu casco.
- **Habilidades.** Los Reflejos acortan el enfriamiento de tus habilidades y la Táctica hace que duren más ([Habilidades](/wiki/03-Mechanics/Abilities.md#pilot-skills)). El Sabotaje refuerza los venenos.
- **Mines.** El Sabotaje aumenta el daño de una Mine, y la Puntería la lanza más rápido y más lejos ([Extras](/wiki/06-Items/Extras.md#mine)).
- **Velocidad.** La Teoría de propulsores suma a tu velocidad, además de los motores y un Afterburner ([Velocidad](/wiki/03-Mechanics/Speed.md)).
- **Recogidas.** El Instinto aumenta la probabilidad de cada línea de botín, igual que un Loot Luck Booster, y los dos se suman; la Antimateria aumenta la Dark Matter que recoges ([Carga](/wiki/03-Mechanics/Cargo.md), [Dark Matter](/wiki/03-Mechanics/Dark-Matter.md)).
- **Radiación.** La Tecnología de radiación reduce la dosis del agujero negro, de los círculos de los excavadores, de los púlsares y del aura de los Unwakened ([Agujero negro](/wiki/03-Mechanics/Black-Hole.md)).
- **En casa.** La Extracción y la Logística cambian lo que el [Skylab](/wiki/03-Mechanics/Skylab.md) produce y guarda, el Instinto aumenta sus dos colectores, la Fabricación acorta las fabricaciones del Ensamblaje, la Ciencia llena más rápido el Centro de [Investigación](/wiki/03-Mechanics/Research.md), y el Comercio baja los precios de la tienda, sube lo que paga al recomprar y baja la tarifa de un anuncio de la [Subasta](/wiki/03-Mechanics/Auction.md).

## Cómo se paga la XP {#how-xp-is-paid}

El servidor paga XP por lo que haces, vueles donde vueles, en este orden:

1. **La regla antifarmeo.** Un impacto de o hacia un compañero de corporación o de grupo no paga nada, ni tampoco nada hecho a una nave en una zona segura o bajo el refugio de una reaparición, ni por ella. Los segundos de Masa, del casco bajo del Temple y de la Teoría de propulsores cuentan solo mientras tu nave está viva, fuera de un refugio y has dado una orden en el último minuto: una nave aparcada al aire libre no gana nada.
2. **El límite blando por hora.** Una estadística con límite paga la XP completa hasta él y una parte por encima, contada en la unidad propia de la estadística (los disparos que haces, las órdenes que das, la XP que ganó) durante la hora del reloj UTC. Un nuevo inicio de sesión no reabre la ventana, y las cifras están en la lista de arriba y en la tabla de abajo.
3. **Velocidad de entrenamiento.** El atributo que rige una destreza aumenta la XP que gana la destreza, más con cada nivel del atributo (el límite se cuenta antes de esto, así que limita la actividad y no la velocidad).
4. **La parte del atributo.** La destreza recibe la XP, y su atributo recibe una parte de ella, que nunca se limita ni se acelera.

La tabla indica qué paga XP, estadística por estadística. La XP es por cada unidad de lo que se nombra en la segunda columna.

<!-- skills-xp:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Estadística | Qué paga XP | XP | Límite blando por hora |
| :--- | :--- | ---: | ---: |
| **Masa** | Cada 10 s de vuelo con una orden dada en los últimos 1 min: el nivel de casco de la nave, más 0,2 por cada placa instalada, ×1,5 con la bodega llena | 1 | Ninguno |
| **Temple** | Cada 1 % de tu casco máximo perdido ante un enemigo o un peligro | 1 | 300 XP por hora |
|  | Cada 10 s por debajo del 25 % de tu casco máximo | 5 |  |
| **Reflejos** | Cada orden que acepta el juego: una habilidad, un extra, un objetivo nuevo, una recogida, una fabricación, un cambio de formación, un cohete o un salto. Un objetivo nuevo paga como mucho una vez cada 4 s, una recogida como mucho una vez cada 1 s y un cohete como mucho una vez cada 1 s | 1 | 600 órdenes por hora |
| **Instinto** | Cada caja de carga que recoges, a mano o con un Retriever | 2 | 600 XP por hora |
|  | Cada objeto de una recompensa de misión que reclamas | 10 |  |
|  | La primera vez que recoges un objeto de calidad Raro o mejor (una vez por objeto, para siempre) | 25 |  |
| **Tecnología láser** (Reflejos) | Cada ráfaga que disparas | 0,1 | 1.800 disparos por hora |
|  | Cada ráfaga que alcanza a una nave | 0,1 |  |
| **Tecnología de cohetes** (Reflejos) | Cada cohete que lanzas | 0,15 | 130 cohetes por hora |
|  | Cada cohete que alcanza a una nave (una vez por cohete, a cuantas naves hiera su explosión) | 0,3 |  |
| **Antimateria** (Instinto) | Cada unidad de Dark Matter que recibes al recoger | 0,1 | Ninguno |
| **Puntería** (Reflejos) | Cada impacto de una ráfaga disparada con munición distinta de la simple x1 (×1,5 durante los primeros 10 min de cada tipo de munición en una hora del reloj) | 0,1 | 3.000 impactos por hora |
|  | Cada impacto de una Mine y cada segundo que un enemigo pasa en tu Energetic Wall | 0,1 |  |
| **Sabotaje** (Reflejos) | Cada impacto de una Mine y cada segundo que un enemigo pasa en tu Energetic Wall | 0,5 | 1.200 XP por hora |
|  | Cada segundo que un veneno tuyo actúa sobre un enemigo | 0,05 |  |
| **Evasión** (Reflejos) | Cada ataque hostil contra ti que falla o es esquivado | 1 | 600 XP por hora |
| **Táctica** (Reflejos) | Cada habilidad que pulsas con un hostil al alcance del láser | 2 | 600 XP por hora |
| **Tecnología de radiación** (Temple) | Cada segundo dentro de una banda de radiación | 0,2 | Ninguno |
|  | Cada 1 % de tu casco máximo que quita la radiación | 1 |  |
| **Teoría de propulsores** (Masa) | Cada segundo volado por encima del 80 % de la velocidad de tu nave, el doble con un Afterburner | 0,1 | Ninguno |
| **Ciencia** (Instinto) | Cada unidad de ciencia que quema el Centro de investigación | 0,1 | Ninguno |
|  | Cada tecnología que terminas | 50 |  |
| **Extracción** (Instinto) | Cada unidad de recurso que produce tu Skylab, pagada al recoger | 0,1 | Ninguno |
| **Logística** (Masa) | Cada unidad de recurso que depositas en el banco del Skylab | 0,05 | Ninguno |
| **Fabricación** (Reflejos) | Cada segundo de tiempo de fabricación que completas, pagado al recoger | 0,1 | Ninguno |
| **Comercio** (Instinto) | Cada operación en la Subasta o la tienda, contada como el logaritmo decimal de 1 más su valor en Credits (un Thulium vale lo que la Subasta lo valora) | 2 | 600 XP por hora |

<!-- skills-xp:end -->

Mientras vuelas, la pantalla de vuelo muestra la XP que ganas en líneas cortas, reunidas cada pocos segundos, y un cartel te avisa cuando una estadística sube de nivel y qué cambió (el Registro de juego guarda una línea). Una estadística que gana su primera XP se anuncia una vez. Las descripciones emergentes de las cifras que movieron las destrezas también lo dicen, en una línea de piloto propia, y el recuadro de Daño del hangar deja fuera las destrezas y lo indica: se aplican cuando disparas.

## Subir de nivel {#levelling-up}

Un nivel cuesta más XP que el anterior, en una proporción fija, así que los primeros niveles llegan rápido y los últimos tardan. Todas las estadísticas tienen la misma curva. El bonificador que tienes en un nivel es el mismo para todos los pilotos: solo la velocidad a la que lo alcanzas depende de lo que hagas.

<!-- skills-curve:begin -->
<!-- Generated from server/Resources/PilotSkills.json by scripts/skills-wiki.sh: don't edit by hand. -->

| Nivel | XP del nivel | XP en total desde el nivel 1 | Parte de cada bonificador |
| :--- | ---: | ---: | ---: |
| 2 | 40 | 40 | 1,01 % |
| 10 | 66 | 468 | 9,09 % |
| 25 | 170 | 2.174 | 24,24 % |
| 50 | 822 | 12.851 | 49,49 % |
| 75 | 3.968 | 64.397 | 74,75 % |
| 100 | 19.157 | 313.258 | 100 % |

<!-- skills-curve:end -->

## La página Destrezas de piloto {#the-pilot-skills-page}

La página **Destrezas de piloto** es una página de la estación, con una fila propia en la barra lateral. Muestra todo el árbol: los atributos y las destrezas en sus grupos, cada una con su nivel. Elige una estadística para ver qué hace, qué atributo la rige, qué destrezas entrena, su barra de XP y qué la hace crecer, y usa el control deslizante para previsualizar cualquier nivel del 1 al último: una pequeña tabla da lo que la estadística cambia en el nivel que previsualizas y en tu nivel actual. Una estadística que aún no ha ganado XP aparece como sin usar, con un guion como nivel. La fila de la barra lateral lleva una insignia cuando una estadística ha subido de nivel desde la última vez que abriste la página, y una tarjeta de la ventana de Potenciadores resume lo que cambian tus destrezas.

## Qué se conserva {#what-is-kept}

- **En todos los reinicios.** El árbol es parte de tu cuenta: un reinicio no cambia ningún nivel ni nada de XP, y el Alijo de Transporte no tiene nada que ver con ello ([Lo que conservas](/wiki/03-Mechanics/Wipe-Timeline.md#what-you-keep)).
- **En los servidores regionales.** La XP que ganas volando en Singapore o US East se suma a tus destrezas cuando vuelves a casa, incluida una estadística que usaste allí por primera vez, y el límite por hora que gastaste allí te acompaña. La página Destrezas de piloto de un piloto que vuela allí lee las cifras del servidor regional, con la XP que su nave ha ganado desde su último guardado.
- **Hasta que se elimine la cuenta.** Eliminar una cuenta elimina sus niveles.

Los bonificadores no tienen más techo que el último nivel: un piloto que lo ha subido todo es tan fuerte como dicen las tablas.
