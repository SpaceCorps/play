<!-- wiki-i18n source: abed58eb82eb0e72 -->
<!-- wiki-i18n title: Cohetes -->
# Cohetes {#rockets}

Los cohetes son una segunda arma junto a tus láseres: un disparo cada pocos segundos que golpea mucho más fuerte que una andanada láser. Doce cohetes en cuatro tipos, tres gamas cada uno, dos más que solo fabrica Ensamblaje, y **un único temporizador de recarga de 3 segundos que comparten todos**, sea cual sea el que dispares (los dos que solo fabrica Ensamblaje esperan un poco más, por su largo vuelo). Los cohetes comunes y raros se compran con **créditos**; los cuatro cohetes épicos se compran con **Thulium**. Una [formación de drones](/wiki/03-Mechanics/Formations.md) puede aumentar el daño de un cohete y alargar o acortar ese temporizador: consulta [Formaciones de drones y cohetes](#drone-formations-and-rockets).

## En un minuto {#in-one-minute}

- **Doce cohetes que comprar.** Cuatro tipos (Lancet, Rivet, Ember, Scatter), tres gamas cada uno. Los comunes y raros cuestan créditos, los épicos Thulium. Otros dos cohetes, la N.U.K.E. y la N.I.K.E., los fabrica el Ensamblaje.
- **Cada cohete sortea su daño.** Al dispararlo, el juego elige un número entre el daño más bajo y el más alto del cohete (un Lancet I: de 1.700 a 2.100). Tu nave, tus láseres, tus amplificadores y tus potenciadores no lo cambian; solo una formación de drones lo hace. Los cohetes que disparan los alienígenas no se sortean: causan una cifra fija ([Contra los alienígenas](#against-the-aliens)).
- **Las explosiones son más fuertes en el medio.** Los cohetes Ember y Scatter estallan y dañan a toda nave dentro del anillo: la cifra completa en el centro, la mitad en el borde.
- **Un solo temporizador para todos.** Tras cualquier lanzamiento esperas 3 segundos antes del siguiente, sea cual sea el cohete. Solo el N.U.K.E. y el N.I.K.E. te hacen esperar más (4,1 y 4,6 segundos), porque se quedan tanto tiempo en el aire.
- **Guiado o recto.** Un cohete guiado (Lancet, Ember) necesita un objetivo que hayas seleccionado. Uno recto (Rivet, Scatter) vuela hacia tu cursor.

<!-- item-tree:begin -->
<!-- Generated from server/Data/Seeds/{items,recipes}.json and Resources/Rockets.json by scripts/trees-wiki.sh: don't edit by hand. -->

## Árbol de objetos {#item-tree}

Lo que fabrica Ensamblaje necesita antes su tecnología; pasa el cursor por un objeto para ver cuánto tarda en investigarse. El árbol de tecnologías, el combustible y el impulso: [Investigación](/wiki/03-Mechanics/Research.md).

```tree
Lancet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter I | rocket, common | buy 500 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter II | rocket, rare | buy 800 Credits | /wiki/06-Items/Rockets.md#the-twelve-rockets
Lancet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Rivet III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Ember III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
Scatter III | rocket, epic | buy 5 Thulium | /wiki/06-Items/Rockets.md#the-twelve-rockets
N.I.K.E. | rocket, mythical | craft 100000 Credits, 1500 Thulium, 300 s, x5 | research 10800 s, 10800 science | 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets
N.U.K.E. | rocket, legendary | craft 150000 Credits, 3000 Thulium, 900 s | research 86400 s, 86400 science, 10 Dark Matter | 6 Scatter III, 40 Ship Fragment, 10 Reinforced Hull Plate, 4 Power Core, 80 Cataclysite | /wiki/06-Items/Rockets.md#the-craft-only-rockets

Lancet I -> Lancet II -> Lancet III
Rivet I -> Rivet II -> Rivet III
Ember I -> Ember II -> Ember III
Scatter I -> Scatter II -> Scatter III => N.U.K.E.
```
<!-- item-tree:end -->

## Los cuatro tipos {#the-four-kinds}

| | Un objetivo: golpea una nave | Explosión en área: estalla y daña todo lo cercano |
| :--- | :--- | :--- |
| **Guiado**: fija el objetivo que seleccionaste y lo persigue | Lancet I, Lancet II, Lancet III | Ember I, Ember II, Ember III |
| **Recto**: vuela hacia tu cursor | Rivet I, Rivet II, Rivet III | Scatter I, Scatter II, Scatter III |

Cada tipo es una **familia**, con el nombre de su cohete común, y la gama es un número romano: **Lancet I**, **Lancet II** y **Lancet III** son el cohete guiado de un solo objetivo común, raro y épico, y las familias Rivet, Ember y Scatter siguen el mismo patrón. El código de un cohete en su casilla del selector de cohetes y en el hangar son las tres letras de su familia y su número (LNC II, RVT III, EMB I, SCT II); los dos cohetes que solo se fabrican en el Ensamblaje conservan su nombre y su código (N.U.K.E., NUK; N.I.K.E., NIK).

- Los cohetes **guiados** necesitan un objetivo seleccionado dentro de su **alcance de fijación** cuando salen. Lo persiguen con una velocidad de giro limitada, así que una nave rápida y lejana puede dejar atrás a uno barato. Si el objetivo muere, se va o llega a una zona segura, el cohete sigue volando recto y no elige otro.
- Los cohetes **rectos** no necesitan objetivo e ignoran el que tengas seleccionado: siempre vuelan hacia tu **cursor**, hacia el punto que hay bajo él en la vista de vuelo. **Haz clic en la ranura de un cohete recto para armarlo** (la ranura recibe un marco blanco y una mira, y el cursor del ratón se convierte en una mira sobre el espacio), y luego **haz clic en el espacio**: el cohete vuela hacia el punto en el que hiciste clic y tu nave se queda donde está. Esc, un clic derecho o volver a pulsar la misma ranura lo desarman. Si los cohetes aún se están recargando, el clic solo te lo dice y el cohete sigue armado. Las teclas numéricas y **Disparar cohete** disparan al instante hacia el último punto que tuvo el cursor en la vista de vuelo; si el cursor aún no ha estado ahí, vuelan hacia donde **apunta** tu nave. Vuelan rectos, así que una nave que cruza a toda velocidad puede esquivarlos.
- Un cohete de **un solo objetivo** golpea la primera nave que puede golpear (uno guiado, solo a su objetivo). Una **explosión en área** estalla junto a la primera nave que encuentra, en el punto al que la apuntaste, o donde termina su vuelo, y daña a toda nave dentro de su **radio de explosión**: daño completo en el centro, la mitad en el borde. El anillo que la explosión dibuja en el mapa es su alcance exacto.
- **Asteroides.** Un cohete disparado contra un [asteroide](/wiki/03-Mechanics/Asteroid-Mining.md) golpea ese asteroide y nada más, y un cohete que no se dispara contra uno atraviesa todos los asteroides. Los doce cohetes de la tienda y el N.U.K.E. pueden romper uno; el N.I.K.E. no. Tus láseres también dañan un asteroide, pero solo con el 5 % de lo que hacen a una nave: el cohete es la herramienta para ese trabajo.

## Los doce cohetes {#the-twelve-rockets}

Cada cohete tiene **su propio daño, que se sortea al dispararlo**: en cualquier punto entre su cifra más baja y su cifra más alta, y la tabla muestra las dos y la media. No depende de tu nave, de tus láseres y sus amplificadores, de tus potenciadores, de tu munición ni de tus drones, y un cohete nunca es crítico. Solo una **formación de drones** lo cambia: la tabla de aquí da el daño sin formación (consulta [Formaciones de drones y cohetes](#drone-formations-and-rockets)). Un cohete de un objetivo causa el daño que sacó a la nave que golpea; una explosión sortea una sola vez y lo causa a **toda nave dentro de ella**, el número completo en el centro y la mitad en el borde. La *penetración de escudo* se resta de la absorción de tu objetivo en ese impacto (la absorción de una nave es la parte de un impacto que se llevan sus escudos, consulta [Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md#shield-penetration)): el 35 % de un Lancet III deja a los escudos de una nave con 80 % el 45 % del impacto y manda el otro 55 % al casco. Una explosión no tiene.

| Nombre | Tipo | Rareza | Daño | Media | Penetración de escudo | Radio de explosión | Alcance de fijación | Alcance | Velocidad | Precio | Máximo que puedes llevar |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Guiado · un objetivo | Común | 1.700–2.100 | 1.900 | 10 % | – | 700 | 1.040 | 520 | 500 créditos | 5.000 |
| **Lancet II** | Guiado · un objetivo | Raro | 3.500–4.200 | 3.850 | 25 % | – | 1.000 | 1.584 | 660 | 800 créditos | 2.000 |
| **Lancet III** | Guiado · un objetivo | Épico | 5.200–6.200 | 5.700 | 35 % | – | 1.300 | 2.296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Recto · un objetivo | Común | 2.200–2.700 | 2.450 | 5 % | – | – | 1.080 | 900 | 500 créditos | 5.000 |
| **Rivet II** | Recto · un objetivo | Raro | 4.500–5.250 | 4.875 | 25 % | – | – | 1.120 | 700 | 800 créditos | 2.000 |
| **Rivet III** | Recto · un objetivo | Épico | 7.000–8.000 | 7.500 | 35 % | – | – | 1.100 | 500 | 5 Thulium | 500 |
| **Ember I** | Guiado · explosión en área | Común | 1.200–1.400 | 1.300 | – | 170 | 700 | 1.000 | 500 | 500 créditos | 5.000 |
| **Ember II** | Guiado · explosión en área | Raro | 2.400–2.900 | 2.650 | – | 230 | 920 | 1.500 | 600 | 800 créditos | 2.000 |
| **Ember III** | Guiado · explosión en área | Épico | 3.500–4.500 | 4.000 | – | 300 | 1.150 | 2.030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Recto · explosión en área | Común | 1.500–1.750 | 1.625 | – | 210 | – | 1.088 | 640 | 500 créditos | 5.000 |
| **Scatter II** | Recto · explosión en área | Raro | 3.000–3.500 | 3.250 | – | 290 | – | 1.080 | 540 | 800 créditos | 2.000 |
| **Scatter III** | Recto · explosión en área | Épico | 4.500–5.500 | 5.000 | – | 400 | – | 1.092 | 420 | 5 Thulium | 500 |

Cuanto más cara es la gama, más fuerte golpea un cohete, más lejos llega, más penetración de escudo tiene y menos puedes llevar; los caros también dan el mayor daño por lo que cuestan. Un cohete recto causa entre un cuarto y un tercio más que el cohete guiado de su gama y tipo por el mismo precio (del 23 al 32 % de media), porque hay que apuntarlo. Una explosión causa casi dos tercios de lo que causa el cohete de un objetivo de su gama y tipo (del 66 al 70 % de media: un Ember frente a un Lancet, un Scatter frente a un Rivet), a toda nave que cubre. El daño de una explosión es completo en su centro y cae en línea recta hasta **la mitad en el borde**: una nave cuyo casco está a medio camino del borde recibe el 75 %, y una con el casco fuera del anillo no recibe nada. Un disparo causa de media el punto medio de su intervalo, del 89 al 94 % de su cifra máxima, y la tabla de más abajo, que cuenta cohetes, usa ese valor.

## Lo que cuestan {#what-they-cost}

Un cohete común cuesta 500 créditos, uno raro 800 créditos y uno épico 5 Thulium, en todos los tipos. Disparados en cada temporizador, son 10.000 créditos por minuto con un cohete común, 16.000 con uno raro y 100 Thulium con uno épico, frente a los 900 créditos por minuto que gastan los tres láseres de una Ostirion con munición x1. Una reserva llena son 5.000 cohetes comunes (2.500.000 créditos), 2.000 raros (1.600.000 créditos) o 500 épicos (2.500 Thulium): puedes comprar tantos como quieras hasta ese límite, y el *máximo que puedes llevar* de un cohete es el único límite de cuántos tienes. Los cohetes no pesan nada: no ocupan sitio en el Alijo de Transporte. Un cohete cada 3 segundos son solo veinte por minuto, así que un cohete es la ráfaga que se suma a tus láseres: los baratos para los alienígenas débiles, los caros para los grandes combates. Lo que has puesto en la [Subasta](/wiki/03-Mechanics/Auction.md#limits) y los lotes en los que vas en cabeza cuentan para ese límite cuando compras un cohete o pujas por él.

La tienda lista los cohetes un tipo tras otro, cada uno bajo su nombre, con el cohete común primero y el épico al final; el hangar, el Alijo de Transporte y el selector de Cohetes usan el mismo orden.

## Contra los alienígenas {#against-the-aliens}

Los cohetes que hacen falta para matar a un alienígena, con un solo tipo de cohete cada vez, sacando cada cohete la media de su intervalo (Alpha; los alienígenas de Beta y de Gamma son 1,5 y 2 veces más fuertes). Una explosión cuenta como la recibe la nave junto a la que estalla, algo por debajo del centro (del 87 al 93 % del daño del centro). El escudo de un alienígena se lleva el 80 % de un impacto, menos la penetración de escudo del cohete. Con la tirada más baja un derribo requiere hasta un 15 % más de cohetes de los que dice la tabla (un Lancet I necesita 48 para un Goombah, no 43); con la mejor, hasta un 13 % menos (39). Un Rivet II, un Lancet III y un Rivet III matan a un Phantasm de un impacto con cualquier tirada; un Rivet I necesita dos con una tirada de 2.600 o más, y tres con menos.

| Cohetes para matar | Seeker (1.600) | Phantasm (5.200) | Bulwark (26.000) | Goombah (80.000) | Crystalys (416.000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 14 | 43 | 219 |
| **Lancet II** | 1 | 2 | 7 | 19 | 109 |
| **Lancet III** | 1 | 1 | 5 | 11 | 73 |
| **Rivet I** | 1 | 3 | 11 | 33 | 170 |
| **Rivet II** | 1 | 1 | 6 | 15 | 86 |
| **Rivet III** | 1 | 1 | 4 | 8 | 56 |
| **Ember I** | 2 | 5 | 24 | 71 | 369 |
| **Ember II** | 1 | 3 | 12 | 34 | 177 |
| **Ember III** | 1 | 2 | 8 | 23 | 116 |
| **Scatter I** | 2 | 4 | 18 | 56 | 287 |
| **Scatter II** | 1 | 2 | 9 | 27 | 141 |
| **Scatter III** | 1 | 2 | 6 | 18 | 90 |

- Los cohetes de un objetivo **comunes** matan a un Seeker de un impacto con cualquier tirada y a un Phantasm de tres (un Lancet I necesita un cuarto con su tirada más baja); son los cohetes de todos los días de los primeros sectores. Los **raros** son para el Bulwark y el Goombah: siete cohetes Lancet II se llevan un Bulwark en unos 20 segundos de temporizador. Los **épicos** de un objetivo matan a un Goombah con ocho (Rivet III) a once (Lancet III). Las explosiones valen su precio cuando hay varios alienígenas juntos: un Scatter III que estalla sobre una manada de cinco Phantasms (todos a menos de 250 unidades del objetivo al que apuntaste) causa unos 21.000 de daño repartidos entre la manada de un solo lanzamiento.
- Un derribo solo con cohetes es un gasto de verdad, no una forma de hacerse rico: un cohete de un objetivo cuesta entre el 15 % (un Rivet II contra un Phantasm) y el 95 % (un Lancet I contra un Crystalys) de lo que paga el derribo (créditos, y Thulium a 200 créditos cada uno), y las explosiones débiles contra los alienígenas fuertes cuestan más de lo que paga el derribo (un Ember I contra un Bulwark: el 120 %). Derribar al **Crystalys** con un solo tipo requiere de 56 a 369 cohetes y casi tres minutos de temporizador; una reserva llena de 500 cohetes épicos alcanza para entre cuatro y ocho de estos derribos. El alienígena más fuerte necesita un plan: tus láseres con munición x2, un cohete de gama media cada 3 segundos desde el primer segundo, y los cohetes grandes de más abajo como ráfaga.
- La paga de un derribo es la misma sea como sea que se haya hecho (consulta [el Crystalys](/wiki/04-Aliens/Crystalys.md) para el mayor), así que un derribo con cohetes compensa cuando te ahorra tiempo y cuesta menos de lo que paga.
- **Los alienígenas también disparan cohetes.** El Pirate Boss, la Dormant Force y las Pulses de los [enjambres](/wiki/05-Swarms/Swarms.md) y los Siege Wardens de los [clanes](/wiki/03-Mechanics/Clans.md#clan-wardens) lanzan cohetes Rivet rectos contra el piloto que los atacó, con temporizadores propios (5 segundos los enjambres, de 8 a 24 los Siege Wardens) que tu formación no cambia. **El cohete de un alienígena no se sortea ni usa los intervalos de arriba**: causa un daño fijo de 2.500 (Rivet I), 5.000 (Rivet II) o 7.500 (Rivet III), más en Beta y Gamma, donde los alienígenas son 1,5 y 2 veces más fuertes (el cohete de un Clan Warden es el mismo en todos los mundos). Una nave que no deja de moverse los esquiva. Los jefes de los enjambres también sueltan cohetes en sus cajas.

## Los cohetes que solo se fabrican {#the-craft-only-rockets}

Dos cohetes no están en la tienda. Los fabrica **Ensamblaje**, y siguen todas las reglas de más abajo (el temporizador compartido, las zonas seguras, tu corporación). Los dos son cohetes rectos: vuelan hacia el punto que hay bajo tu cursor, como todo cohete recto (el juego envía la dirección del cursor sea cual sea lo que tengas seleccionado; solo un cliente antiguo 0.4.3, que no envía dirección, hace que el servidor los haga volar hacia el objetivo seleccionado; si no hay, hacia el punto bajo su cursor; y si tampoco, hacia donde apunta la nave). Sacan entre el **90 % y el 100 %** de su cifra máxima, una banda más estrecha que la de los doce, así que lo que destruyen de un impacto más abajo vale también con la tirada más baja.

| Nombre | Tipo | Rareza | Daño | Penetración de escudo | Radio de explosión | Alcance | Velocidad | Máximo que puedes llevar | Se fabrica con |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **N.U.K.E.** | Recto · explosión en área | Legendario | 45.000–50.000 | – | 900 | 1.200 | 300 | 10 | 1 N.U.K.E. por fabricación: 150.000 créditos, 3.000 Thulium, 6 Scatter III, 4 Power Core, 10 Reinforced Hull Plate, 40 Ship Fragment, 80 Cataclysite |
| **N.I.K.E.** | Recto · un objetivo | Mítico | 67.500–75.000 | 35 % | – | 4.050 | 900 | 20 | 5 N.I.K.E. por fabricación: 100.000 créditos, 1.500 Thulium, 20 Ship Fragment, 4 Reinforced Hull Plate, 40 Cataclysite |

- **N.U.K.E.**: la mayor explosión del juego. Una explosión de 900 unidades, el doble del alcance de las 400 del Scatter III y cinco veces su área: de 45.000 a 50.000 a toda nave que esté dentro, en el centro, y baja a la mitad, de 22.500 a 25.000, en el borde. Es lenta (cuatro segundos en el aire). Una N.U.K.E. aniquila a todos los Seekers y Phantasms de toda su explosión y a un Bulwark a menos de 830 unidades del estallido (934 con la mejor tirada), casi en toda la explosión; se lleva más de la mitad de un Goombah y un noveno de un Crystalys. Contra pilotos es el mayor golpe que existe: consulta las reglas de más abajo. El anillo del mapa es su alcance exacto.
- **N.I.K.E.**: un cohete de un objetivo como un Rivet I, con un daño de 67.500 a 75.000 y una penetración de escudo del 35 %: **golpea la primera nave que toca y se gasta en ella.** Es también el cohete que produce [Dark Matter](/wiki/03-Mechanics/Black-Hole.md): disparado contra el agujero negro del centro del sector de peligro 4, el agujero se lo traga cuando cruza el horizonte de sucesos, y devuelve Dark Matter. Vuela 4.050 unidades en 4,5 segundos: dispáralo desde cualquier punto entre el borde de la radiación y 4.380 unidades del centro. Desde más lejos se queda corto y se desperdicia. Cinco N.I.K.E. producen unas diez unidades de Dark Matter.
- **La trampa.** Una N.I.K.E. que se encuentra por el camino una nave, un rival que espera en la línea de tiro o cualquier otra cosa que pueda dañar, la golpea con 67.500 a 75.000 y desaparece: el agujero negro no recibe nada, y tú tampoco. No hay nada más rondando dentro del anillo del agujero con lo que pueda chocar por accidente (los alienígenas y los pilotos de corporación se mantienen fuera): solo los pilotos que entraron a por Dark Matter, o que te esperan en el borde. Atraviesa a tu propia corporación, a las naves en una zona segura y a las naves a las que todavía no puedes dañar. Si sales del mapa después de dispararlo, sigue volando sin dañar a nadie y aun así produce tu Dark Matter.
- Ensamblaje no inicia una fabricación que te dejaría con más del *máximo que puedes llevar* de un cohete, contando lo que tienes en cola.

## Disparo {#firing}

1. Compra cohetes en la tienda (la categoría **Cohetes**), hasta el *máximo que puedes llevar* de cada uno: créditos para los comunes y raros, Thulium para los épicos.
2. Abre **Cohetes** encima de la barra rápida y arrastra los que quieras a las ranuras. El selector muestra una columna por tipo y una fila por gama, con lo que llevas de cada uno. Debajo hay una fila propia, **Especiales · solo Ensamblaje**, para la N.U.K.E. y la N.I.K.E. (un pequeño martillo marca la que no llevas).
3. Pulsa la tecla de la ranura. Hacer clic en la ranura de un cohete **guiado** lo dispara contra tu objetivo seleccionado; hacer clic en la ranura de un cohete **recto** lo arma, y tu siguiente clic en el espacio lo dispara allí. La tecla **Disparar cohete** (`R` por defecto, reasignable en Configuración › Controles) dispara el cohete que disparaste por última vez, o el primero de la barra.
4. Un barrido circular cubre **todas** las ranuras de cohete durante los 3 segundos hasta el siguiente lanzamiento (4,1 tras un N.U.K.E., 4,6 tras un N.I.K.E.), con los segundos que quedan en el centro. Una pulsación antes de eso solo te dice que los cohetes se están recargando (una pulsación en la última décima de segundo todavía dispara). Una formación de drones puede dejar la espera entre 2,19 y 4,05 segundos (ver abajo).

Pasa el cursor por una ranura de cohete para ver sus cifras (su daño más bajo y más alto; la tienda y el hangar dicen lo mismo) y, en el mundo, su anillo de fijación (verde cuando el objetivo seleccionado está al alcance) o su línea y su círculo de explosión. Un cohete fijado en **ti** hace parpadear en rojo el borde de tu pantalla.

La **N.U.K.E.** dibuja su explosión en el mapa antes de que dispares (el círculo de 900 unidades en el punto apuntado) y, cuando estalla, un destello blanco sobre la vista, un anillo que se expande hasta el alcance exacto en aproximadamente un segundo y permanece dos más, una nube que se eleva como un hongo y una sacudida de la cámara que es más fuerte cuanto más cerca estás. **Reducir temblor de pantalla** elimina la sacudida, y **Reducir movimiento** acorta el destello a un tercio de segundo con menos de la mitad de su luz (las dos están en Configuración, en Gráficos); una calidad de partículas más baja aclara la nube y suprime las chispas, nunca el destello ni el anillo. La **N.I.K.E.** se apunta como un Rivet I, con la línea que va de tu nave al cursor, y el juego nunca lo rechaza por estar lejos del agujero negro o en un mapa que no tiene ninguno: a dónde va, lo juzgas tú. Su tarjeta dice **Agujero negro: Produce Dark Matter** junto a su daño. Deja una estela violeta con chispas que la rodean en espiral; una nave que encuentra recibe el golpe como con cualquier cohete, y cuando cruza el horizonte en cambio, el agujero destella.

## Formaciones de drones y cohetes {#drone-formations-and-rockets}

Una [formación de drones](/wiki/03-Mechanics/Formations.md) puesta es lo único que cambia un cohete. Todas las cifras de daño de esta página son para una nave sin formación.

- **Daño.** La bonificación de cohetes de Ballista (+55 %), Bodkin (+29 %) y Asterism (+24 %) multiplica el daño de los 14 cohetes, incluidos el N.U.K.E. y el N.I.K.E. El coste de todo el daño de Testudo cuenta en los cohetes, y el daño a alienígenas de Culler cuenta en un cohete que alcanza a un alienígena. Todos los factores de un cohete juntos se detienen en ×1,59. La bonificación cuenta contra un [asteroide](/wiki/03-Mechanics/Asteroid-Mining.md#breaking-one) igual que contra una nave, y el blindaje del asteroide se resta después.
- **Recarga.** Asterism alarga el temporizador compartido un 35 % (4,05 segundos), Cordon un 11 % (3,33) y Redoubt lo acorta un 27 % (2,19), pero nunca por debajo del vuelo del cohete más un instante. Con Redoubt, los cohetes rápidos (Lancet I, Rivet I y II, Ember I, Scatter I y II) esperan los 2,19 segundos, un Rivet III espera 2,3, un Lancet III 2,9 y un Ember III los 3 completos; el N.U.K.E. y el N.I.K.E. esperan 4,1 y 4,6 segundos, lleves lo que lleves. La espera se fija al disparar, así que cambiar de formación después no la acorta, y el barrido sobre las ranuras de cohete la sigue.
- **Los límites de los dos grandes se mantienen.** Con la mejor formación un N.I.K.E. golpea con hasta 116.250, lo que un Paragon intacto (128.000) sobrevive, y un N.U.K.E. con hasta 77.500, lo que sobrevive un Goombah (80.000).
- **Evasión.** El 7 % de evasión de Asterism da a un cohete directo que te alcanza un 7 % de probabilidad de no causar ningún daño, y sobre tu nave aparece un «Fallo» flotante; una explosión de área no apunta y nunca se esquiva.
- **Penetración.** Gemini y Stiletto suman sus puntos a la penetración de escudo de un cohete directo (una explosión no tiene), hasta un 40 % en total. Un impacto láser llega hasta el 50 % ([Láseres y munición](/wiki/06-Items/Lasers.md#shield-penetration-of-a-laser-hit)).

## Reglas {#rules}

- **No necesitas ningún láser instalado** para disparar un cohete, y tus láseres no cambian lo que causa ni hasta dónde llega: un cohete guiado fija un objetivo dentro de su propio alcance de fijación, uno recto vuela su propia distancia. Sin ningún láser instalado, la casilla Alcance del hangar muestra un guion, y solo disparan tus cohetes.
- Se gasta un cohete por lanzamiento, acierte o no.
- Los cohetes siguen las reglas de los láseres: nada dentro de una **zona segura** sufre daño, ningún piloto sufre daño antes de que termine el **Protocolo de paz** ni donde un sector prohíbe el PvP, y **tu propia corporación y tu propio grupo nunca sufren daño** por tus cohetes, directo o en explosión.
- Lanzar un cohete termina al instante tu propia protección de zona segura. Es un disparo: también termina tu propio **camuflaje**, y la Cloaking CPU se recarga entonces durante un minuto, como después de cualquier fin de camuflaje. Camuflado o no, un lanzamiento te impide camuflarte durante los 10 segundos siguientes (consulta [Extras](/wiki/06-Items/Extras.md)).
- Una nave **camuflada** o dentro de los **3 segundos de su EMP** no se puede fijar: un cohete guiado es rechazado, y uno que ya vuela hacia ella pierde la fijación y sigue recto. Un cohete recto de un objetivo atraviesa una nave así. Una **explosión en área** no necesita fijación, así que daña a las naves que cubre, camufladas o no, y termina un camuflaje (consulta [Extras](/wiki/06-Items/Extras.md)).
- **Nada limita lo que un cohete le hace a un piloto.** La nave de otro piloto recibe todo el daño: primero el escudo (su absorción menos la penetración de escudo del cohete), luego el casco. Las naves pequeñas no aguantan. Con los núcleos de escudo de serie (Light, 45 % de absorción), una N.I.K.E. destruye con cualquier tirada una Protos, una Kitefin o una Ostirion nuevas de un solo impacto (una Paragon pierde del 47 al 53 % de su casco, una Wraith alrededor de una quinta parte), y una N.U.K.E. destruye una Protos en cualquier punto de su explosión, una Kitefin a menos de unas 50 unidades del estallido (220 con la mejor tirada) y nada más grande en una sola explosión. Dos cohetes Lancet III o dos Rivet III destruyen una Protos con cualquier tirada; una Wraith aguanta entre 45 y 70 de ellos. El Protocolo de paz, las zonas seguras y tu corporación son lo único que se interpone entre un piloto y un cohete. Estas cifras son para una nave sin formación; una formación de cohetes las aumenta hasta un 55 % (consulta [Formaciones de drones y cohetes](#drone-formations-and-rockets)).
- Solo el **impacto directo** de un cohete reclama a un alienígena (consulta [Combate](/wiki/03-Mechanics/Combat.md)); el borde de una explosión puede dañar a un alienígena reclamado sin quitárselo a su dueño. Todo alienígena al que daña una explosión, también uno dormido, se vuelve contra ti, como con un impacto láser (un Seeker o un Goombah, que solo contraatacan, incluidos); el que la explosión no alcanza sigue dormido.
- El temporizador es tuyo: sobrevive a un salto, a una reconexión, a un cambio de nave y a una nave destruida.

Los doce cohetes de la primera tabla se compran (créditos los comunes y raros, Thulium los épicos); la N.U.K.E. y la N.I.K.E. se fabrican.

Consulta también: [Láseres y munición](/wiki/06-Items/Lasers.md), [Combate](/wiki/03-Mechanics/Combat.md), [El agujero negro](/wiki/03-Mechanics/Black-Hole.md).
