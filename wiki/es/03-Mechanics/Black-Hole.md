<!-- wiki-i18n source: 55d6cdfda1970b32 -->
<!-- wiki-i18n title: Agujero negro -->
# El agujero negro {#the-black-hole}

<!-- wiki-search: black hole -->

En el centro exacto del sector de peligro 4 (`DS-4`, el centro de la zona PvP), un agujero negro cuelga en la oscuridad. Es el mismo en todos los mundos (Alpha, Beta y Gamma), todos los días de la temporada, incluido el Protocolo de paz. Se lleva lo que se acerca demasiado y devuelve una sola cosa: [Dark Matter](#dark-matter), por un cohete N.I.K.E. disparado contra él. El camino entero, de la investigación a la plate, está en [Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md).

![A Wraith approaches the black hole from 3,500 units: the radiation and pull rings lie around it like a gravity well](../../img/wiki-img/shots/black-hole-approach.jpg)
![Looking down on the black hole from 1,300 units: the shadow, the photon ring and the spiral of the accretion disk, with the starfield bent around it](../../img/wiki-img/shots/black-hole-closeup.jpg)

## Los anillos {#the-rings}

Las distancias se miden desde el centro del sector, en unidades del mapa. El sector mide 32.000 por 18.000 unidades.

| Anillo | Distancia | Qué ocurre |
| :--- | ---: | :--- |
| **Radiación** | 4.000 | Tu nave recibe daño cada segundo, una parte de sus HP máximos totales. Cuanto más cerca, más. |
| **Atracción** | 3.000 | El agujero negro atrae tu nave hacia el centro, con más fuerza cuanto más cerca estás. Una nave que no vuela es arrastrada. |
| **Punto de no retorno** | de unos 1.000 a 2.600 | Donde la atracción iguala la velocidad de tu nave. Dentro de él, ni a toda potencia puedes evitar que te arrastre. Depende de tu velocidad. |
| **Horizonte de sucesos** | 300 | Toda nave que lo alcanza es destruida al instante, sean cuales sean su casco y su escudo. |

Los portales del sector de peligro 4 y las rutas entre ellos pasan todos muy por fuera de la radiación, así que nunca te la encuentras por accidente al cruzar.

## Radiación {#radiation}

El daño es un **porcentaje de los HP máximos totales de tu nave** (casco más escudo) cada segundo, así que todas las clases de nave duran exactamente lo mismo a una distancia dada: una Protos y una Wraith a 2.000 unidades consumen una nave completa en 50 segundos.

| Distancia | Daño por segundo | Una nave completa dura |
| ---: | ---: | ---: |
| 4.000 | 0,3 % | 333 s |
| 3.500 | 0,55 % | 182 s |
| 3.000 | 0,8 % | 125 s |
| 2.000 | 2 % | 50 s |
| 1.200 | 5 % | 20 s |
| 700 | 11 % | 9 s |
| 300 | 24 % | 4 s |

Entre dos filas el daño sube en línea recta. En puntos de vida por segundo, para las configuraciones de serie:

| Nave | HP máx. totales | A 3.500 | A 3.000 | A 2.000 | A 1.200 | A 700 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Protos | 30.000 | 165 | 240 | 600 | 1.500 | 3.300 |
| Kitefin | 46.000 | 253 | 368 | 920 | 2.300 | 5.060 |
| Ostirion | 82.500 | 454 | 660 | 1.650 | 4.125 | 9.075 |
| Nomad | 130.500 | 718 | 1.044 | 2.610 | 6.525 | 14.355 |
| Paragon | 162.500 | 894 | 1.300 | 3.250 | 8.125 | 17.875 |
| Storm | 198.000 | 1.089 | 1.584 | 3.960 | 9.900 | 21.780 |
| Wraith | 372.000 | 2.046 | 2.976 | 7.440 | 18.600 | 40.920 |
| Ironclad | 673.200 | 3.703 | 5.386 | 13.464 | 33.660 | 74.052 |

- El **escudo lo absorbe primero**, luego el casco. No es un impacto: la absorción del escudo no interviene y no se puede esquivar.
- La radiación cuenta como **daño recibido**: tu escudo no se recarga, un Repair Drone se detiene («Reparaciones interrumpidas: radiación.») y no se puede iniciar, y una zona segura no te protegería hasta 5 segundos después de la última dosis.
- Los potenciadores y las mejoras cambian lo grande que es tu total, no cuánto duras: el daño es una parte de él.
- Nada vuelve inmune a una nave. La radiación no es un impacto, así que nada la absorbe; pero las habilidades siguen funcionando dentro de ella: un Shield Surge sigue restaurando tu escudo y un Emergency Repair sigue reparando tu casco durante sus diez segundos (no son las reparaciones naturales que detiene la dosis). El camuflaje no oculta la nave de la radiación.

## La atracción {#the-pull}

Dentro de las 3.000 unidades, el agujero negro atrae a toda nave hacia el centro, y la atracción solo crece cuanto más cerca estás. Empieza suavemente en el borde y ya se nota 200 unidades más adentro:

| Distancia | Atracción (unidades por segundo) | Una nave que no vuela es arrastrada |
| ---: | ---: | :--- |
| 3.000 | 0 | todavía nada |
| 2.800 | 25 | 25 unidades en un segundo |
| 2.300 | 60 | 60 unidades en un segundo |
| 1.800 | 120 | 120 unidades en un segundo |
| 1.300 | 220 | 220 unidades en un segundo |
| 1.000 | 262 | 262 unidades en un segundo, y aumentando |
| 900 | 289 | 289 unidades en un segundo, y aumentando rápido |
| 700 | 496 | hasta el horizonte en alrededor de un segundo |
| 300 | 2.829 | el horizonte de sucesos |

De 3.000 a 925 unidades la atracción sube en línea recta entre dos filas; por dentro de 925 sigue una curva más empinada (las tres últimas filas están en ella). Es una corriente: mueve tu nave y tus motores luchan contra ella.

- **Una nave que no vuela no puede quedarse quieta.** Si te detienes (llegas al lugar en el que hiciste clic, o nunca diste ninguna orden), el agujero negro arrastra tu nave hacia el centro y tu orden se desplaza con ella, así que tu nave sigue cayendo por rápido que pudieran volar sus motores. Para mantener un lugar tienes que seguir volando hacia él: mantén el ratón sobre él, y tu nave se sostiene allí donde su velocidad supera la atracción, cediendo un poco entre una orden y otra. Dos naves que se detienen para intercambiar disparos dentro de la atracción son arrastradas las dos.
- **Una nave que vuela nota un viento en contra.** Al volar directamente alejándote del centro, la atracción del lugar en que estás reduce la velocidad de tu nave: a velocidad 155 haces 130 unidades por segundo a 2.800, 95 a 2.300 y 35 a 1.800, y a 1.500 (una atracción de 180) no avanzas nada.

Tu **punto de no retorno** es la distancia en la que la atracción iguala tu velocidad. Una nave con velocidad 150 lo tiene a 1.650 unidades; cuanto más rápido eres, más adentro queda:

| Nave (configuración de serie) | Velocidad | Punto de no retorno |
| :--- | ---: | ---: |
| Ironclad | 99 | 1.974 |
| Protos | 165 | 1.577 |
| Kitefin | 184 | 1.480 |
| Ostirion | 208 | 1.362 |
| Nomad | 211 | 1.347 |
| Paragon | 222 | 1.287 |
| Wraith | 233 | 1.208 |
| Storm | 263 | 995 |

Un diseño de nave cambia la velocidad de su nave, y con ella su punto de no retorno: una DUMA es más lenta que una Ironclad, una NOTSUM más rápida que una Storm.

Una nave más rápida que 272 unidades por segundo (una configuración de corredor, o una Wraith de serie con un Afterburner en marcha) tiene su punto de no retorno donde siempre estuvo: a velocidad 300 es 885, a 432 es 747.

Si optimizas la nave para la velocidad, puedes salir desde más adentro; si te cargas de escudos pesados, no (una Ironclad, la nave más lenta, con un Heavy Shield Core en cada una de sus 14 ranuras vuela a 39,1, con su punto de no retorno en unos 2.600). Solo una ráfaga de velocidad devuelve a una nave desde justo dentro de su punto de no retorno: cuenta un [Afterburner](/wiki/03-Mechanics/Abilities.md) en marcha, y desplaza el punto de no retorno más adentro mientras dura (diez segundos con un motor, quince con dos, veinte con tres; el Afterburner III lleva el de una Protos de serie de 1.577 a 989 y el de una Wraith de serie de 1.208 a 801). Nada puede salir desde menos de unas 390 unidades, ni siquiera una nave construida para la velocidad con todas las estadísticas de velocidad encantadas al máximo y la ráfaga más potente en marcha (un Afterburner III encantado hasta el límite, x1,69); una nave sin encantar construida para la velocidad (Engine III con un Impulse Thruster IV y dos Momentum Thruster IV, y Adaptive Core II con dos Impulse Thruster IV), con un Afterburner III, sale desde fuera de 427 en el mejor de los casos.

La caída desde el punto de no retorno empieza despacio: una nave a unas pocas unidades por dentro, a toda potencia, es arrastrada durante veinte segundos o más, y luego cada vez más rápido. La atracción no es vuelo: no cuenta para la distancia recorrida.

## El horizonte de sucesos {#the-event-horizon}

Una nave que llega a 300 unidades del centro es destruida. Una nave cuyo casco se agota por la radiación por el camino es destruida por la radiación. En cualquier caso:

- Es una destrucción normal: eliges dónde reaparecer (consulta [Morir y volver](/wiki/01-General/Getting-Started.md)), con un máximo de 10.000 de casco y el escudo vacío (consulta esa página), y cuesta lo que siempre cuesta una destrucción. «En el sitio» nunca te devuelve al interior del anillo: te lleva al punto más cercano fuera de él (a 4.500 unidades del centro) y te lo dice.
- **Sin restos, sin caja, sin botín**, y sin pérdida de honor.
- Tu destrucción se acredita como un derribo PvP al **último piloto enemigo que golpeó tu nave en los 15 segundos anteriores a su destrucción**: un piloto de otra corporación (donde y cuando se permita el PvP), por pequeño que sea el golpe. Es un derribo en sus estadísticas y en sus puntos de clasificación PvP según el tipo de tu nave, nada más. Basta un solo disparo, y si nadie de otra corporación te golpeó en esos 15 segundos, nadie recibe nada.
- Los compañeros de corporación que golpearon tu nave en esos 15 segundos siguen perdiendo el honor por fuego amigo, sea lo que sea lo que la destruyó.
- Los alienígenas y los pilotos de corporación nunca se acercan a él. Si alguno acaba dentro de todos modos, desaparece sin botín, recompensa ni reclamación.

## Lo que ves y oyes {#what-you-see-and-hear}

La vista es pequeña (unas 1.900 por 1.150 unidades en pantalla con el zoom por defecto, 4.400 por 2.650 con el zoom alejado al máximo), así que la imagen propia del agujero negro solo se ve a unas tres mil unidades de él (3.600 con el zoom alejado al máximo). Desde más lejos nada en la pantalla apunta hacia él (mira el minimapa o el mapa del Sistema estelar, más abajo); el aviso de la interfaz es para cuando estás cerca:

- **Desde lejos.** Si bajas la cámara para mirar a lo largo del plano, el agujero negro se dibuja donde se encuentra en la pantalla, desde cualquier punto del sector, siempre que esté en el encuadre: un disco negro con un anillo en un resplandor de luz de acreción, escalado para que se vea con facilidad (cerca del 2 % de la altura de la vista desde la esquina más lejana, que está a unas 18.000 unidades), y crece hasta convertirse en su propia imagen a medida que te acercas. Nada en él se mueve por sí solo. Con el agujero negro fuera de la vista no hay ningún marcador en la pantalla para él.
- **Anillos en el plano de vuelo.** Una banda violeta brilla hasta un borde nítido en el límite de la radiación (4.000 unidades), y otra más fina, ámbar, marca el borde de la atracción (3.000). Dentro de la atracción una **línea roja** muestra *tu propio* punto de no retorno. Sigue tu velocidad, así que se mueve a medida que tu nave va más rápida o más lenta.
- **El indicador**, sobre la barra rápida, aparece a menos de mil unidades del borde y se queda mientras te quemas. Muestra la radiación en porcentaje de los HP totales de tu nave por segundo, cuánto tardaría la radiación sola en consumir lo que te queda («Letal en 31 s», en rojo por debajo de diez), una barra de esos HP, la atracción donde estás frente a tu velocidad y la distancia que aún queda por volar hasta tu punto de no retorno, o un aviso parpadeante una vez que lo has pasado. Pasa el cursor por una fila para ver qué significa; la (i) abre una tarjeta.
- **Los bordes de la pantalla** brillan en violeta, se vuelven rojos a medida que sube la dosis y pulsan una vez por segundo.
- **El minimapa** dibuja el agujero negro con sus anillos como elipses (el plano se estira con su ventana), y su descripción emergente indica los radios. La carta estelar marca el sector con un pequeño agujero negro.
- **Un contador de radiación** hace clic más rápido a medida que sube la dosis, por encima del ruido del combate. Un aviso de dos tonos suena al cruzar el borde y de nuevo en tu punto de no retorno, y se oye un rumor grave desde unas 6.500 unidades, más grave cuanto más cerca estás.
- **La imagen:** desde la calidad gráfica **Media** (con el posprocesado activado) el agujero se dibuja siguiendo la luz a su alrededor, rayo a rayo: una sombra negra con un fino anillo de fotones blanco alrededor, y el disco de acreción tal como su luz llegaría hasta ti. Con la cámara alta es un anillo brillante alrededor de la oscuridad; si inclinas la cámara hacia abajo, la cara lejana del disco se curva por encima del agujero y su parte inferior por debajo, mientras la cara cercana cruza por delante. El cielo detrás del agujero también se curva, con moderación: las estrellas, la nebulosa, los planetas y los asteroides son empujados hacia fuera alrededor de la sombra y sus líneas se arquean a su alrededor. Las naves se dibujan por encima del agujero y ya no las tapa en negro: un casco entre tú y el agujero se queda delante. La calidad Media sigue la luz durante menos vueltas, dibuja menos imágenes del disco y omite el brillo extra del lado que gira hacia ti, que añaden Alta y Ultra. La calidad gráfica **Baja**, y un fotograma sin posprocesado, conservan la imagen anterior: un disco negro con un anillo brillante y un disco de acreción de tres capas que giran en sentido contrario, sin curvar el cielo. Una tarjeta gráfica que no puede construir la imagen nueva vuelve también a la imagen anterior, con la leve curvatura de las estrellas que esta tenía. En todas las calidades se suman estelas de materia que caen siguiendo la atracción (caen a la propia velocidad de la atracción, así que una nave que no vuela es arrastrada al mismo paso que ellas, y una que vuela alejándose contra la atracción las ve pasar a toda velocidad). Una nave que arrastra la atracción no emite llama de motor y no deja estela; una que vuela alejándose contra ella arde a toda su velocidad a través de la corriente, y su estela fluye hacia el agujero. El temblor de la cámara crece con la atracción, en proporción a la velocidad de tu nave, está en su nivel configurado en tu punto de no retorno y sigue subiendo hasta el horizonte. Una nave a la que el agujero quema suelta chispas violetas; una que este se traga es arrastrada hacia el centro y estirada hasta quedar fina. El cielo del sector es el violeta oscuro y verde de `DS-3`.
- **Los restos:** rocas y trozos de cascos destruidos giran alrededor del agujero negro y caen en espiral, desde el borde de su atracción hasta el horizonte: despacio al principio y luego cada vez más rápido, barriendo a su alrededor y girando más deprisa cuanto más se acercan. Brillan en naranja con la luz del disco, se estiran hasta convertirse en agujas al ser desgarrados y desaparecen antes de llegar al horizonte. Entre ellos hay unas pocas rocas grandes, y algunos flotan por encima del plano de vuelo, de modo que las naves pasan por debajo. Son solo decorado: nada los golpea y ellos no golpean nada, y solo se ven a menos de unas cuatro mil unidades del agujero negro, desvaneciéndose hacia las 6.500. La luz del disco también cae sobre tu nave cuando está cerca.
- **Cuando mueres**, la capa superpuesta dice por qué: «Tragado por el agujero negro» o «Consumido por la radiación», y el Registro de juego tiene la línea.

La configuración ayuda donde el agujero resulta pesado o cansa la vista: **Reducir movimiento** detiene el disco y las estelas, deja quietos los restos y detiene el pulso de los bordes de la pantalla, y **Reducir temblor de pantalla** detiene el temblor de la cámara cerca del agujero; la **calidad gráfica Baja** conserva la imagen anterior, sin la lente de trazado de rayos, y dibuja menos estelas (40, frente a 100 en Media y 200 en las superiores) y menos restos (30, frente a 80 en Media y 160 en las superiores), avivando el anillo para compensarlo, y dibuja la vista lejana con un resplandor menos. Una **calidad de partículas** más baja aclara los restos igual que aclara las rocas del fondo.

## Mantenerse fuera {#staying-out}

- El servidor te guía: una orden de movimiento que llevaría tu nave a través del anillo de radiación (a 4.200 unidades del centro, algo más ancho que la propia radiación) se vuela **rodeándolo**, a lo largo de su borde. Las órdenes que acaban dentro del anillo se vuelan tal como se dieron; entrar es decisión tuya. Las rutas a través del sector son hasta una quinta parte más largas; las rutas entre los portales, nada.
- La pestaña **Sistema** del chat te avisa cuando cruzas el borde de la radiación, el borde de la atracción y tu propio punto de no retorno, y de nuevo cuando estás a salvo. Esas líneas no están en **Global** ni en **Local**.
- Si sales del juego dentro de la radiación pero fuera de la atracción, vuelves en el borde exterior del anillo, manteniendo la posición, con el casco que tenías. Si sales **dentro de la atracción** (3.000 unidades), vuelves exactamente donde lo dejaste, con el casco que tenías, y la caída continúa: desconectarse no es una salida del agujero negro.
- Una versión más antigua del juego no muestra el agujero negro. Aun así recibe los avisos y la guía, y todavía puede entrar volando en el anillo si se le ordena.

Los drones vuelan con su nave. Nunca se deja carga dentro del anillo: una caja que fuera a caer allí se coloca en su borde. Las cajas de Dark Matter son la única excepción.

## Obtener Dark Matter {#dark-matter}

¿Nuevo con la Dark Matter? [Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) tiene el camino entero, de la investigación a la plate. Esta sección es la parte del agujero negro.

El agujero devuelve **Dark Matter** por un cohete **N.I.K.E.** que lo alcanza. Una N.I.K.E. es un cohete de 67.500 a 75.000 de daño que golpea a la primera nave a la que puede dañar y se gasta en ella; si no hay nada en el camino, vuela hasta el agujero y se consume al cruzar el horizonte de sucesos. El [Ensamblaje](/wiki/06-Items/Rockets.md) fabrica N.I.K.E. cuando su tecnología está investigada ([Investigación](/wiki/03-Mechanics/Research.md)), cinco por fabricación (100.000 créditos, 1.500 de Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite).

- **Disparo.** Una N.I.K.E. vuela 4.050 unidades en 4,5 segundos (900 por segundo) en línea recta hacia donde apuntaste: sin objetivo seleccionado, pon el cursor sobre el agujero negro (o apunta tu nave hacia él). Llega al horizonte desde cualquier punto entre el borde de la radiación (4.000 unidades) y 4.380 unidades del centro. Más lejos se queda corta y se desperdicia. Como todos los cohetes, usa el temporizador compartido, y después esperas 4,6 segundos hasta el siguiente cohete (no hace falta tener un láser equipado); dispararla pone fin a tu protección de zona segura y a tu camuflaje. **Una nave en la línea de tiro la recibe en su lugar**: un rival que espera en el borde, o un piloto de otra corporación que recoge cajas en el camino, recibe de 67.500 a 75.000 de daño y el agujero no recibe nada. Los alienígenas y los pilotos de corporación nunca entran en el anillo, así que mantener despejada la línea depende de ti; atraviesa a tu propia corporación y a las naves que están a salvo de ti. Si sales del mapa después del disparo, sigue volando sin dañar a nadie y aun así genera tu Dark Matter. Una formación de drones puede cambiar el daño del impacto, pero no la espera tras una N.I.K.E. (consulta [Formaciones de drones y cohetes](/wiki/06-Items/Rockets.md#drone-formations-and-rockets)).
- **Qué se obtiene.** Cada N.I.K.E. que llega al horizonte da **1, 2 o 3 Dark Matter** (2 de media, así que unas cinco N.I.K.E. dan diez), en una o dos cajas pequeñas que aparecen en el borde de la zona del agujero, **a entre 3.050 y 3.950 unidades del centro**, cerca de la línea por la que entró tu disparo. La atracción termina en 3.000, así que las cajas y las naves que las toman no son atraídas, y la radiación allí es del 0,3 al 0,8 % de los HP de una nave por segundo: un minuto en medio de la banda cuesta un tercio de tu nave. Una nave completa dura tres minutos allí.
- **De quién.** Las cajas son tuyas, y de tu clan, durante **60 segundos** desde el disparo. Después, cualquiera que esté en el mapa puede tomarlas, y se alejan a la deriva a los **4 minutos**. El sector de peligro es un sector PvP, así que espera compañía. Un piloto que se desconecta tras disparar conserva sus cajas.
- **Cuántas.** Un mapa admite como máximo 32 cajas de Dark Matter; una nueva desplaza a la más antigua de ellas, y nunca a otro tipo de caja. El [Resource Magnet Booster](/wiki/03-Mechanics/Cargo.md) no suma nada al Dark Matter.
- **Lo que ves.** Cuando una N.I.K.E. cruza el horizonte, es estirada hacia el agujero, el espacio ondula desde donde entró, y el disco y el anillo de fotones destellan durante aproximadamente un segundo y medio (una tercera parte de eso, con la mitad de luz, con **Reducir movimiento**). Un momento después las cajas salen del agujero y derivan hasta sus lugares en el borde: cada una es una esfera de color negro violáceo con un borde brillante y destellos, fácil de ver desde lejos, y se titula **Dark Matter** cuando pasas el cursor por ella. Las tuyas muestran encima los segundos que te quedan, y aparecen en el minimapa como una pequeña marca violeta, igual que para tu clan; las cajas de otros pilotos aparecen en el minimapa solo cuando termina su minuto.
- **Para qué sirve.** El Ensamblaje combina 5 Dark Matter con una Velkonite Reinforced Plate y una Orvium Reinforced Plate para obtener una **Dark Matter Plate**, y [la Forja de Ensamblaje](/wiki/06-Items/Forge.md) pide dos de ellas para subir un objeto de Divino a Rompedor y de nuevo de Rompedor a Eterno: diez Dark Matter por paso. El último nivel de cada cadena de mejora pide 3 plates, 15 Dark Matter por pieza: los amps, las células de escudo y los propulsores del nivel IV, el Heavy Shield Core, el Engine III, el Helios Beam, el Extra Slots CPU III y el Base CPU II. El [Centro de investigación](/wiki/03-Mechanics/Research.md#dark-matter) del Skylab también necesita Dark Matter: 10 por cada una de las 16 tecnologías de lo más alto de su árbol, 160 en total, añadidos al Centro antes de que empiece la investigación. Las formaciones de drones también la piden, 5, 13 o 20 según su fuerza: 189 más, 349 en total. Las dos investigaciones del Hull Plating piden 65 más, y los diseños de naves y las ranuras de blindaje 490 ([Investigación](/wiki/03-Mechanics/Research.md#ship-technologies)). Un Helios Beam con sus tres amps del nivel IV contiene 60 Dark Matter, y un Wraith que lleva solo piezas del último nivel, 900 ([Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#what-the-last-tier-asks-for)).
