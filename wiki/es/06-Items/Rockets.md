<!-- wiki-i18n source: 2599ac53be69ec9b -->
<!-- wiki-i18n title: Cohetes -->
# Cohetes {#rockets}

Los cohetes son una segunda arma junto a tus láseres: un disparo cada pocos segundos que golpea mucho más fuerte que una andanada láser. Doce cohetes en cuatro tipos, tres gamas cada uno, dos más que solo fabrica Ensamblaje, y **un único temporizador de recarga de 5 segundos que comparten todos**, sea cual sea el que dispares. Los cohetes comunes y raros se compran con **créditos**; los cuatro cohetes épicos se compran con **Thulium**.

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
- Un cohete de **un solo objetivo** golpea la primera nave que puede golpear (uno guiado, solo a su objetivo). Una **explosión en área** estalla junto a la primera nave que encuentra, en el punto al que la apuntaste, o donde termina su vuelo, y daña a toda nave dentro de su **radio de explosión**: daño completo en el centro, menos hacia el borde. El anillo que la explosión dibuja en el mapa es su alcance exacto.

## Los doce cohetes {#the-twelve-rockets}

Cada cohete tiene **su propio daño, que se sortea al dispararlo**: entre el **80 % y el 100 %** de su cifra máxima, y la tabla muestra el más bajo y el más alto. Es el mismo lo dispare quien lo dispare: no depende de tu nave, de tus láseres, de tus Damage Amps, de tus potenciadores, de tu munición ni de tus drones, y un cohete nunca es crítico. Un cohete de un objetivo causa el daño que sacó a la nave que golpea; una explosión sortea una sola vez y lo causa a **toda nave dentro de ella**, el número completo en el centro y menos hacia el borde. La *penetración de escudo* se resta de la absorción de tu objetivo en ese impacto (la absorción de una nave es la parte de un impacto que se llevan sus escudos, consulta [Mecánicas de los escudos](/wiki/03-Mechanics/Shields.md#shield-penetration)): el 35 % de un Lancet III deja a los escudos de una nave con 80 % el 45 % del impacto y manda el otro 55 % al casco. Una explosión no tiene.

| Nombre | Tipo | Rareza | Daño | Penetración de escudo | Radio de explosión | Alcance de fijación | Alcance | Velocidad | Precio | Máximo que puedes llevar |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **Lancet I** | Guiado · un objetivo | Común | 1.600–2.000 | 10 % | – | 700 | 1.040 | 520 | 500 créditos | 5.000 |
| **Lancet II** | Guiado · un objetivo | Raro | 3.200–4.000 | 25 % | – | 1.000 | 1.584 | 660 | 800 créditos | 2.000 |
| **Lancet III** | Guiado · un objetivo | Épico | 4.800–6.000 | 35 % | – | 1.300 | 2.296 | 820 | 5 Thulium | 500 |
| **Rivet I** | Recto · un objetivo | Común | 2.000–2.500 | 5 % | – | – | 1.080 | 900 | 500 créditos | 5.000 |
| **Rivet II** | Recto · un objetivo | Raro | 4.000–5.000 | 25 % | – | – | 1.120 | 700 | 800 créditos | 2.000 |
| **Rivet III** | Recto · un objetivo | Épico | 6.000–7.500 | 35 % | – | – | 1.100 | 500 | 5 Thulium | 500 |
| **Ember I** | Guiado · explosión en área | Común | 1.120–1.400 | – | 170 | 700 | 1.000 | 500 | 500 créditos | 5.000 |
| **Ember II** | Guiado · explosión en área | Raro | 2.240–2.800 | – | 230 | 920 | 1.500 | 600 | 800 créditos | 2.000 |
| **Ember III** | Guiado · explosión en área | Épico | 3.360–4.200 | – | 300 | 1.150 | 2.030 | 700 | 5 Thulium | 500 |
| **Scatter I** | Recto · explosión en área | Común | 1.400–1.750 | – | 210 | – | 1.088 | 640 | 500 créditos | 5.000 |
| **Scatter II** | Recto · explosión en área | Raro | 2.800–3.500 | – | 290 | – | 1.080 | 540 | 800 créditos | 2.000 |
| **Scatter III** | Recto · explosión en área | Épico | 4.200–5.250 | – | 400 | – | 1.092 | 420 | 5 Thulium | 500 |

Cuanto más cara es la gama, más fuerte golpea un cohete, más lejos llega, más penetración de escudo tiene y menos puedes llevar; los caros también dan el mayor daño por lo que cuestan. Un cohete recto causa un **25 % más** que el cohete guiado de su gama y tipo por el mismo precio, porque hay que apuntarlo. Una explosión causa el 70 % del cohete de un objetivo de su gama, a toda nave que cubre. El daño de una explosión es máximo en su centro; cae a entre el 25 y el 35 % en el borde. Un disparo causa de media el 90 % de su cifra máxima, y la tabla de más abajo, que cuenta cohetes, usa ese valor.

## Lo que cuestan {#what-they-cost}

Un cohete común cuesta 500 créditos, uno raro 800 créditos y uno épico 5 Thulium, en todos los tipos. Disparados en cada temporizador, son 6.000 créditos por minuto con un cohete común, 9.600 con uno raro y 60 Thulium con uno épico, frente a los 1.800 créditos por minuto que gastan los tres láseres de una Ostirion con munición x1. Una reserva llena son 5.000 cohetes comunes (2.500.000 créditos), 2.000 raros (1.600.000 créditos) o 500 épicos (2.500 Thulium): puedes comprar tantos como quieras hasta ese límite, y el *máximo que puedes llevar* de un cohete es el único límite de cuántos tienes. Los cohetes no pesan nada: no ocupan sitio en el Alijo de Transporte. Un cohete cada 5 segundos son solo doce por minuto, así que un cohete es la ráfaga que se suma a tus láseres: los baratos para los alienígenas débiles, los caros para los grandes combates.

La tienda lista los cohetes un tipo tras otro, cada uno bajo su nombre, con el cohete común primero y el épico al final; el hangar, el Alijo de Transporte y el selector de Cohetes usan el mismo orden.

## Contra los alienígenas {#against-the-aliens}

Los cohetes que hacen falta para matar a un alienígena, con un solo tipo de cohete cada vez (Alpha; los alienígenas de Beta y de Gamma son 1,5 y 2 veces más fuertes). Una explosión cuenta como la recibe la nave junto a la que estalla, algo por debajo del centro. El escudo de un alienígena se lleva el 80 % de un impacto, menos la penetración de escudo del cohete. Aquí cada cohete saca la media. Con la tirada más baja un derribo requiere entre un 10 y un 15 % más de cohetes de los que dice la tabla (un Lancet I necesita 50 para un Goombah, no 45); con la mejor, un 10 % menos (40). Un Rivet II mata a un Phantasm de un impacto solo con una tirada del 89 % o más, y con menos necesita dos.

| Cohetes para matar | Seeker (1.600) | Phantasm (5.200) | Bulwark (26.000) | Goombah (80.000) | Crystalys (416.000) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Lancet I** | 1 | 3 | 15 | 45 | 232 |
| **Lancet II** | 1 | 2 | 8 | 20 | 116 |
| **Lancet III** | 1 | 1 | 5 | 11 | 78 |
| **Rivet I** | 1 | 3 | 12 | 36 | 185 |
| **Rivet II** | 1 | 1 | 6 | 16 | 93 |
| **Rivet III** | 1 | 1 | 4 | 9 | 62 |
| **Ember I** | 2 | 5 | 25 | 77 | 399 |
| **Ember II** | 1 | 3 | 13 | 37 | 193 |
| **Ember III** | 1 | 2 | 8 | 25 | 128 |
| **Scatter I** | 2 | 4 | 20 | 60 | 311 |
| **Scatter II** | 1 | 2 | 10 | 29 | 151 |
| **Scatter III** | 1 | 2 | 7 | 20 | 100 |

- Los cohetes de un objetivo **comunes** matan a un Seeker de un impacto con cualquier tirada y a un Phantasm de tres (un Lancet I necesita un cuarto con su tirada más baja); son los cohetes de todos los días de los primeros sectores. Los **raros** son para el Bulwark y el Goombah: ocho cohetes Lancet II se llevan un Bulwark en unos 35 segundos de temporizador. Los **épicos** matan a un Phantasm de un impacto con cualquier tirada y a un Goombah con nueve a once. Las explosiones valen su precio cuando hay varios alienígenas juntos: un Scatter III que estalla sobre una manada de cinco Phantasms causa unos 18.000 de daño repartidos entre la manada de un solo lanzamiento.
- Un derribo solo con cohetes es un gasto de verdad, no una forma de hacerse rico: para el alienígena al que está destinado, un cohete de un objetivo cuesta entre aproximadamente una séptima parte y tres cuartas partes de lo que paga el derribo (créditos, y Thulium a 200 créditos cada uno), y los cohetes débiles contra los alienígenas fuertes cuestan más de lo que paga el derribo. Derribar al **Crystalys** con un solo tipo requiere de 62 a 399 cohetes y al menos cinco minutos de temporizador; una reserva llena de 500 cohetes épicos alcanza para entre cuatro y ocho de estos derribos. El alienígena más fuerte necesita un plan: tus láseres con munición x2, un cohete de gama media cada 5 segundos desde el primer segundo, y los cohetes grandes de más abajo como ráfaga.
- La paga de un derribo es la misma sea como sea que se haya hecho (consulta [el Crystalys](/wiki/04-Aliens/Crystalys.md) para el mayor), así que un derribo con cohetes compensa cuando te ahorra tiempo y cuesta menos de lo que paga.
- **Los alienígenas también disparan cohetes.** El Pirate Boss, la Dormant Force y las Pulses de los [enjambres](/wiki/05-Swarms/Swarms.md) lanzan cohetes Rivet rectos contra el piloto que los atacó, con el mismo temporizador de 5 segundos. Una nave que no deja de moverse los esquiva. Los jefes de los enjambres también sueltan cohetes en sus cajas.

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
4. Un barrido circular cubre **todas** las ranuras de cohete durante los 5 segundos hasta el siguiente lanzamiento, con los segundos que quedan en el centro. Una pulsación antes de eso solo te dice que los cohetes se están recargando (una pulsación en la última décima de segundo todavía dispara).

Pasa el cursor por una ranura de cohete para ver sus cifras (su daño más bajo y más alto; la tienda y el hangar dicen lo mismo) y, en el mundo, su anillo de fijación (verde cuando el objetivo seleccionado está al alcance) o su línea y su círculo de explosión. Un cohete fijado en **ti** hace parpadear en rojo el borde de tu pantalla.

La **N.U.K.E.** dibuja su explosión en el mapa antes de que dispares (el círculo de 900 unidades en el punto apuntado) y, cuando estalla, un destello blanco sobre la vista, un anillo que se expande hasta el alcance exacto en aproximadamente un segundo y permanece dos más, una nube que se eleva como un hongo y una sacudida de la cámara que es más fuerte cuanto más cerca estás. **Reducir temblor de pantalla** elimina la sacudida, y **Reducir movimiento** acorta el destello a un tercio de segundo con menos de la mitad de su luz (las dos están en Configuración, en Gráficos); una calidad de partículas más baja aclara la nube y suprime las chispas, nunca el destello ni el anillo. La **N.I.K.E.** se apunta como un Rivet I, con la línea que va de tu nave al cursor, y el juego nunca lo rechaza por estar lejos del agujero negro o en un mapa que no tiene ninguno: a dónde va, lo juzgas tú. Su tarjeta dice **Agujero negro: Produce Dark Matter** junto a su daño. Deja una estela violeta con chispas que la rodean en espiral; una nave que encuentra recibe el golpe como con cualquier cohete, y cuando cruza el horizonte en cambio, el agujero destella.

## Reglas {#rules}

- **No necesitas ningún láser instalado** para disparar un cohete, y tus láseres no cambian lo que causa ni hasta dónde llega: un cohete guiado fija un objetivo dentro de su propio alcance de fijación, uno recto vuela su propia distancia. Sin ningún láser instalado, la casilla Alcance del hangar muestra un guion, y solo disparan tus cohetes.
- Se gasta un cohete por lanzamiento, acierte o no.
- Los cohetes siguen las reglas de los láseres: nada dentro de una **zona segura** sufre daño, ningún piloto sufre daño antes de que termine el **Protocolo de paz** ni donde un sector prohíbe el PvP, y **tu propia corporación y tu propio grupo nunca sufren daño** por tus cohetes, directo o en explosión.
- Lanzar un cohete termina al instante tu propia protección de zona segura. Es un disparo: también termina tu propio **camuflaje**, y la Cloaking CPU se recarga entonces durante un minuto, como después de cualquier fin de camuflaje. Camuflado o no, un lanzamiento te impide camuflarte durante los 10 segundos siguientes (consulta [Extras](/wiki/06-Items/Extras.md)).
- Una nave **camuflada** o dentro de los **3 segundos de su EMP** no se puede fijar: un cohete guiado es rechazado, y uno que ya vuela hacia ella pierde la fijación y sigue recto. Un cohete recto de un objetivo atraviesa una nave así. Una **explosión en área** no necesita fijación, así que daña a las naves que cubre, camufladas o no, y termina un camuflaje (consulta [Extras](/wiki/06-Items/Extras.md)).
- **Nada limita lo que un cohete le hace a un piloto.** La nave de otro piloto recibe todo el daño: primero el escudo (su absorción menos la penetración de escudo del cohete), luego el casco. Las naves pequeñas no aguantan. Con los núcleos de escudo de serie (Light, 45 % de absorción), una N.I.K.E. destruye con cualquier tirada una Protos, una Kitefin o una Ostirion nuevas de un solo impacto (una Paragon pierde del 47 al 53 % de su casco, una Wraith alrededor de una quinta parte), y una N.U.K.E. destruye una Protos en cualquier punto de su explosión, una Kitefin a menos de unas 50 unidades del estallido (220 con la mejor tirada) y nada más grande en una sola explosión. Dos cohetes Lancet III o dos Rivet III destruyen una Protos con cualquier tirada; una Wraith aguanta entre 48 y 75 de ellos. El Protocolo de paz, las zonas seguras y tu corporación son lo único que se interpone entre un piloto y un cohete.
- Solo el **impacto directo** de un cohete reclama a un alienígena (consulta [Combate](/wiki/03-Mechanics/Combat.md)); el borde de una explosión puede dañar a un alienígena reclamado sin quitárselo a su dueño. Todo alienígena al que daña una explosión, también uno dormido, se vuelve contra ti, como con un impacto láser (un Seeker o un Goombah, que solo contraatacan, incluidos); el que la explosión no alcanza sigue dormido.
- El temporizador es tuyo: sobrevive a un salto, a una reconexión, a un cambio de nave y a una nave destruida.

Los doce cohetes de la primera tabla se compran (créditos los comunes y raros, Thulium los épicos); la N.U.K.E. y la N.I.K.E. se fabrican.

Consulta también: [Láseres y munición](/wiki/06-Items/Lasers.md), [Combate](/wiki/03-Mechanics/Combat.md), [El agujero negro](/wiki/03-Mechanics/Black-Hole.md).
