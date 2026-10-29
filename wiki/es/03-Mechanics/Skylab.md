<!-- wiki-i18n source: 938d06a6843abb63 -->
<!-- wiki-i18n title: Skylab -->
# Skylab

El Skylab es tu instalación orbital personal. Construye y mejora módulos que producen créditos y Thulium, extraen mineral, forjan las placas que el Ensamblaje convierte en los mejores láseres y, desde el nivel 10 del Núcleo, investigan las tecnologías que necesita el Ensamblaje. Trabaja para ti incluso cuando no estás conectado.

En el nivel 10 del Núcleo, el Skylab además crece: un **puente** une el Núcleo con un segundo Núcleo de seis ranuras más para módulos, y a él se acoplan tres módulos más: la **Impresora de munición** y la **Fábrica de cohetes**, que fabrican munición y cohetes de la nada, y la **Bahía de mineral**, que pasa al Almacén de recursos el mineral que llevas contigo (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2) y [Bahía de mineral](#ore-bay)).

En el nivel 15 del Núcleo, el Skylab vuelve a crecer y aprende a volar: un **segundo puente** une el Núcleo con un tercer Núcleo, el **Núcleo 3**, de cuatro ranuras más, y los cuatro módulos de la **Expedición** las ocupan: el **Módulo de motores**, el **Módulo de defensa**, el **Módulo de radar** y la **Bahía de trofeos**. Con motores, láseres y munición de tu Impresora de munición, el Skylab recorre un **mapa del universo** propio, caza a los alienígenas de las celdas a las que llega mientras estás fuera y trae el botín a casa (consulta [El segundo puente y el Núcleo 3](#the-second-bridge-and-core-3) y [Expediciones](#expeditions)).

> [!NOTE]
> **Qué cambió en 0.4.10.** Cada módulo del Skylab tiene ahora su propia tabla de producción, precios y tiempos, nivel por nivel. Conservaste tus niveles: no se cobró nada ni se devolvió nada por la diferencia. Lo que tus granjas y colectores tenían en sus tolvas cuando llegó la actualización se pagó **una sola vez, a la tarifa antigua**: los créditos y el Thulium fueron a tu cuenta, el mineral a tu Almacén de recursos, y las tolvas empezaron de nuevo vacías.
>
> Hay dos reglas nuevas. **Solar produce solo el 25 % de su energía mientras se mejora**, así que en la mayoría de las estaciones todas las granjas y colectores se detienen hasta que termina la mejora (consulta el [módulo Solar](#solar-module) y [Cómo planificar una mejora de Solar](#timing-a-solar-upgrade)). **El Almacén de recursos tiene un límite propio para cada mineral**: un día de la producción del colector en el nivel 1, cuatro días en el nivel 20.

> [!NOTE]
> **Qué cambió en 0.4.15.** El paso del Núcleo del nivel 9 al nivel 10 cuesta ahora **2.000 de Thulium** más, y cuando termina aparecen un **puente** y un segundo Núcleo, el **Núcleo 2**, con seis ranuras nuevas para módulos. Solar se traslada al Núcleo 2. A él se acoplan dos módulos nuevos: la **Impresora de munición** y la **Fábrica de cohetes**. Además, Solar produce más energía desde el nivel 7, para que una estación completa siga cubierta. No pierdes nada de lo que construiste: un Núcleo que ya está en el nivel 10 o más tiene el puente enseguida y no paga nada.

> [!NOTE]
> **Qué cambió en 0.4.21.** El paso del Núcleo del nivel 14 al nivel 15 cuesta ahora **4.000 de Thulium** más, y cuando termina aparecen un segundo **puente** y el **Núcleo 3** con cuatro ranuras nuevas. Solar se traslada al Núcleo 3 y produce más energía desde el nivel 15, de modo que una estación completa sigue cubierta. Cuatro módulos nuevos ocupan las ranuras: el **Módulo de motores**, el **Módulo de defensa**, el **Módulo de radar** y la **Bahía de trofeos**, y con ellos tu Skylab vuela por el **mapa del universo**, caza por su cuenta y trae su botín a casa (consulta [Expediciones](#expeditions)). Cada módulo tiene ahora un **peso**, y el peso de la estación y de sus motores decide a qué velocidad vuela (consulta [Peso y velocidad](#weight-and-speed)). La **Bahía de mineral** pasa tres veces más mineral por hora y guarda tres veces más cupo. No se pierde nada de lo que construiste: un Núcleo que ya está en el nivel 15 o más tiene el Núcleo 3 de inmediato y no paga nada.

![The Skylab of a Core 20 with the second bridge: Core 3 carries the Engine, Defense and Radar Modules and the Trophies Bay](../../img/wiki-img/shots/skylab-core3.jpg)
![The Rocket Factory's sheet: the rocket it makes, the room to carry and its storage](../../img/wiki-img/shots/skylab-factory.jpg)
![The Ore Bay's sheet: the ores it moves and banks for you and how much it holds](../../img/wiki-img/shots/skylab-orebay.jpg)
![The Ammo Printer's Build sheet: its price in Credits, Thulium and Ship Fragments](../../img/wiki-img/shots/skylab-printer-build.jpg)
![The Ammo Printer's sheet: its mode, rate, storage and what the next level gives](../../img/wiki-img/shots/skylab-printer.jpg)
![The Skylab station fully grown, seen from the side as the page opens: three Cores in a row with their bridges, every module with its name tag, the Labels switch at the bottom left](../../img/wiki-img/shots/skylab-station.jpg)
![The Resource Storage card of the Skylab](../../img/wiki-img/shots/skylab-storage.jpg)
![The Skylab table of modules: level, production, storage, power and status of every module, from the Core to the Trophies Bay](../../img/wiki-img/shots/skylab-table.jpg)
![The Skylab hunting in a cell of the Universe map: its hull and kills, the cell, the Defense and Engine Modules and the Trophies Bay filling, and Recall](../../img/wiki-img/shots/skylab-trip.jpg)
![The Trophies Bay's sheet: its level and the capacity the trophies of a trip are kept in](../../img/wiki-img/shots/skylab-trophies.jpg)
![The Universe map: 150 hexagonal cells, the ports, the cells you know and the cells the Radar can still scan, marked with a question mark](../../img/wiki-img/shots/skylab-universe.jpg)

## En un minuto {#in-one-minute}

- Construye primero **Solar**: sin su energía, nada en el Skylab funciona. La Granja de créditos no cuesta nada construirla, y la Granja de Thulium cuesta 5.000 créditos y 500 Thulium.
- Las granjas y los colectores llenan una **tolva** (de 72 horas) mientras estás fuera. **Recoger** la pasa a tu cuenta (créditos, Thulium) o a tu Almacén de recursos (mineral).
- La **Granja de Thulium** es tu principal fuente de Thulium: 40 por hora en el nivel 1, 1.280 en el nivel 20. La Granja de créditos produce 2.250 créditos por hora en el nivel 1 y 225.000 en el nivel 20.
- El **Núcleo** marca el ritmo: ningún módulo pasa de él, y su propia subida dura unos 16 días y medio.
- En el **nivel 10 del Núcleo**, un **puente** construye el **Núcleo 2**, con seis ranuras más para módulos, y la **Impresora de munición**, la **Fábrica de cohetes** y la **Bahía de mineral** se acoplan a él. El paso al nivel 10 cuesta 2.000 de Thulium más.
- En el **nivel 15 del Núcleo**, un segundo puente construye el **Núcleo 3**, y el **Módulo de motores**, el **Módulo de defensa**, el **Módulo de radar** y la **Bahía de trofeos** ocupan sus ranuras: con ellos el Skylab vuela por el mapa del universo y caza por su cuenta. El paso al nivel 15 cuesta 4.000 de Thulium más. [Consulta Expediciones](#expeditions).
- **Solar produce solo el 25 % de su energía mientras se mejora**, así que tus granjas y colectores se detienen hasta que termina. [Planifícalo](#timing-a-solar-upgrade).

## Resumen {#overview}

El Skylab funciona con su propio reloj, aparte de tu nave: los módulos producen y forjan mientras estás fuera. Lo tuyo es construir, mejorar, mantener la energía en equilibrio y recoger. La página tiene cuatro vistas de la misma estación: **Estación** (la estación en 3D, con una etiqueta sobre cada módulo; haz clic en una para abrir su ventana, o pulsa **1** a **9**), **Lista** (una ficha por módulo), **Tabla** (los números de todos los módulos en una tabla) e **Investigación** (la pantalla propia del Centro de investigación, consulta [Investigación](/wiki/03-Mechanics/Research.md)). Si pasas el cursor sobre **Construir** o **Mejorar**, ves qué cambia el siguiente nivel, cuánto cuesta y cuánto tarda. El botón **Universo** de la cabecera de la página abre el mapa de la Expedición (consulta [Expediciones](#expeditions)).

Dieciséis módulos forman la estación:

| Módulo | Qué produce o hace | Se construye desde |
| :--- | :--- | :--- |
| **Núcleo** | Fija el nivel máximo de todos los demás módulos | Siempre presente |
| **Solar** | Produce energía | Cualquier nivel del Núcleo |
| **Granja de créditos** | Produce [créditos](/wiki/01-General/Getting-Started.md) | Cualquier nivel del Núcleo |
| **Granja de Thulium** | Produce [Thulium](/wiki/01-General/Getting-Started.md) | Cualquier nivel del Núcleo |
| **Colector de Velkonite** | Extrae mineral de Velkonite | Núcleo de nivel 5 |
| **Colector de Orvium** | Extrae mineral de Orvium | Núcleo de nivel 5 |
| **Almacén de recursos** | Guarda el mineral | Núcleo de nivel 5 |
| **Forja** | Forja el mineral en placas | Núcleo de nivel 5 |
| **Centro de investigación** | Convierte recursos en ciencia e investiga [tecnologías](/wiki/03-Mechanics/Research.md) | Núcleo de nivel 10 |
| **Impresora de munición** | Imprime munición x2, x3 o x4 de la nada | Núcleo de nivel 10, en el Núcleo 2 |
| **Fábrica de cohetes** | Fabrica cohetes de la tienda de la nada | Núcleo de nivel 10, en el Núcleo 2 |
| **Bahía de mineral** | Pasa al Almacén de recursos el Velkonite y el Orvium que llevas contigo | Núcleo de nivel 10, en el Núcleo 2 |
| **Módulo de motores** | Aloja los motores que hacen volar el Skylab | Núcleo de nivel 15, en el Núcleo 3 |
| **Módulo de defensa** | Aloja los láseres y el cargador que combaten en una expedición | Núcleo de nivel 15, en el Núcleo 3 |
| **Módulo de radar** | Escanea la niebla del mapa del universo | Núcleo de nivel 15, en el Núcleo 3 |
| **Bahía de trofeos** | Guarda lo que traen las expediciones | Núcleo de nivel 15, en el Núcleo 3 |

Los dos **puentes**, el **Núcleo 2** y el **Núcleo 3** no son módulos: el primer puente y el Núcleo 2 aparecen cuando el Núcleo llega al nivel 10, el segundo puente y el Núcleo 3 en el nivel 15, y ninguno de los dos Núcleos tiene nivel propio (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2) y [El segundo puente y el Núcleo 3](#the-second-bridge-and-core-3)).

**Misiones para el Skylab.** Diez [misiones de la estación](/wiki/03-Mechanics/Quests.md#station-missions) en Mission Control te guían por el Skylab: construir Solar, una Granja de créditos y una Granja de Thulium, subir el Núcleo y Solar, recoger tus primeros 50.000 créditos y abrir la cadena de suministro, y pagan un poco por cada paso. La primera está abierta desde el nivel 1.

## La estación en cada nivel {#the-station-at-every-level}

Esta es la vista Estación del Skylab en cada nivel del 1 al 20, todas desde el mismo ángulo, con todos los módulos en el mismo nivel. La vista encaja toda la estación en la imagen, así que la escala no es la misma en todas: salta cuando la forma crece. La estación crece por etapas: su forma cambia en los **niveles 1, 5, 10, 15 y 20**, y entre medias cada nivel enciende **una luz más** en el collar de cada módulo (el número de luces encendidas es el nivel, y el anillo de veinte luces del Núcleo se llena del mismo modo).

Estas imágenes muestran el **primer Núcleo** y lo que cuelga de él, con Solar a su lado, tal como era la estación antes de los puentes. La estación sigue más allá, y las imágenes no muestran esa parte: desde el nivel 10, más allá hay un puente, el Núcleo 2 y la Impresora de munición, la Fábrica de cohetes y la Bahía de mineral, y Solar pasa al extremo lejano (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2)); desde el nivel 15, más allá de eso hay un segundo puente, el Núcleo 3 y los cuatro módulos de la Expedición (consulta [El segundo puente y el Núcleo 3](#the-second-bridge-and-core-3)). La vista Estación de la página muestra la estación entera.

**Niveles 1 a 4.** Los cuatro primeros módulos alrededor del Núcleo: Solar, la Granja de créditos, la Granja de Thulium y la bahía de atraque que aloja tu nave. La cadena de suministro todavía no se puede construir.

![Nivel 1](../../img/skylab/wiki/level-01.jpg)
![Nivel 2](../../img/skylab/wiki/level-02.jpg)
![Nivel 3](../../img/skylab/wiki/level-03.jpg)
![Nivel 4](../../img/skylab/wiki/level-04.jpg)

**Niveles 5 a 9.** Con el Núcleo en el nivel 5 se puede construir la cadena de suministro: los dos colectores en sus estructuras sobre la estación, el Almacén de recursos en el puerto noreste del Núcleo y la Forja en su puerto noroeste (aquí se muestran ya construidos).

![Nivel 5](../../img/skylab/wiki/level-05.jpg)
![Nivel 6](../../img/skylab/wiki/level-06.jpg)
![Nivel 7](../../img/skylab/wiki/level-07.jpg)
![Nivel 8](../../img/skylab/wiki/level-08.jpg)
![Nivel 9](../../img/skylab/wiki/level-09.jpg)

**Niveles 10 a 14.** El Núcleo luce su anillo, las granjas y los colectores adoptan su forma más grande y la Granja de Thulium recibe su propio anillo.

![Nivel 10](../../img/skylab/wiki/level-10.jpg)
![Nivel 11](../../img/skylab/wiki/level-11.jpg)
![Nivel 12](../../img/skylab/wiki/level-12.jpg)
![Nivel 13](../../img/skylab/wiki/level-13.jpg)
![Nivel 14](../../img/skylab/wiki/level-14.jpg)

**Niveles 15 a 19.** Las granjas se llenan de cajas y cristales, la bahía de atraque ilumina su aproximación y la matriz Solar le crece la parte superior. En el nivel 15 la estación también crece más allá de la imagen, con un segundo puente y el Núcleo 3.

![Nivel 15](../../img/skylab/wiki/level-15.jpg)
![Nivel 16](../../img/skylab/wiki/level-16.jpg)
![Nivel 17](../../img/skylab/wiki/level-17.jpg)
![Nivel 18](../../img/skylab/wiki/level-18.jpg)
![Nivel 19](../../img/skylab/wiki/level-19.jpg)

**Nivel 20.** La cima de la escalera: la corona del Núcleo y las torres plenamente desarrolladas de las granjas y la cadena de suministro.

![Nivel 20](../../img/skylab/wiki/level-20.jpg)

**Las fichas de los nueve módulos.** La vista Lista de la misma estación en el nivel 20: los cuatro módulos de la primera versión, el Colector de Velkonite, el Colector de Orvium, el Almacén de recursos y la Forja que llegaron con la cadena de suministro, y el Centro de investigación. Cada ficha muestra el nivel del módulo, su producción, su energía y su interruptor. Todas las fichas marcan el nivel 20 salvo la del Centro de investigación: tiene los niveles 1 a 10, así que su ficha marca el nivel 10, el máximo. Las fichas de la Impresora de munición, la Fábrica de cohetes y la Bahía de mineral están en la misma vista y se describen [más abajo](#the-bridge-and-core-2), y también las cuatro fichas de los módulos de la Expedición, en [El segundo puente y el Núcleo 3](#the-second-bridge-and-core-3).

![La vista Lista en el nivel 20: las tarjetas del Núcleo, Solar, la Granja de créditos, la Granja de Thulium, el Colector de Velkonite, el Colector de Orvium, el Almacén de recursos, la Forja y el Centro de investigación](../../img/skylab/wiki/modules.jpg)

## Los cuatro primeros módulos {#the-first-four-modules}

### Módulo Núcleo {#core-module}

El corazón de tu Skylab. El nivel del Núcleo fija el nivel máximo de todos los demás módulos: ningún módulo se puede mejorar por encima de tu Núcleo. El Núcleo llega al nivel 20 y, desde el **nivel 5**, abre la cadena de suministro de más abajo. Sus mejoras cuestan créditos, el paso al **nivel 10** cuesta **2.000 de Thulium** más y construye el puente y el Núcleo 2 (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2)), y el paso al **nivel 15** cuesta **4.000 de Thulium** más y construye un segundo puente y el Núcleo 3 (consulta [El segundo puente y el Núcleo 3](#the-second-bridge-and-core-3)). En total hacen falta 112.326 créditos hasta el nivel 10 y 6.647.504 hasta el nivel 20, más esos 6.000 de Thulium, y unos 16,5 días (consulta [Tiempos de mejora](#upgrade-times)).

### Módulo Solar {#solar-module}

La energía es el alma del Skylab. El módulo Solar produce la energía que usan todos los demás módulos.

- **Importancia**: si tu consumo de energía es mayor que la energía que produces, tus granjas y colectores se apagan.
- **Energía producida**: un módulo Solar de nivel N produce lo suficiente para **todos los demás módulos en el nivel N**, y alrededor de una décima parte más: 255 en el nivel 1, 965 en el nivel 7, 18.575 en el nivel 20. Solar de nivel 7 alimenta una estación entera en el nivel 7 (consulta Gestión de la energía para ver todos los niveles).
- **Precio**: construir Solar cuesta **500 créditos y 50 Thulium**. Sus mejoras cuestan lo mismo y duran lo mismo que las de la Forja: desde 8.000 créditos y 25 Thulium para el nivel 2 (5 minutos) hasta 9.000.000 de créditos y 10.000 Thulium para el nivel 20 (24 horas).
- **Mejora**: mientras se mejora, Solar produce solo el **25 %** de la energía de su nivel actual, y la del nivel nuevo desde que termina la mejora. Una estación que consume más que eso se detiene: todas las granjas y colectores dejan de producir y la Forja no empieza ningún lote nuevo hasta que termina la mejora. En casi todas las estaciones ocurre así: solo sigue funcionando durante la mejora si todos los demás módulos están al menos cinco niveles por debajo de Solar (seis niveles desde el nivel 10 de Solar). Planifica una mejora de Solar como un apagón de tus granjas (consulta Construcción y mejora).
- **Lugar**: Solar está en el extremo lejano de la estación: en el Núcleo 2 desde el nivel 10 del Núcleo y en el Núcleo 3 desde el nivel 15 (consulta [El puente y el Núcleo 2](#the-bridge-and-core-2) y [El segundo puente y el Núcleo 3](#the-second-bridge-and-core-3)).

### Granja de créditos y Granja de Thulium {#credit-farm-and-thulium-farm}

- **Granja de créditos**: produce créditos con el tiempo: **2.250 por hora en el nivel 1, 225.000 en el nivel 20** (nivel 5: 11.250; nivel 10: 33.750; nivel 15: 76.500). Construirla no cuesta nada.
- **Granja de Thulium**: produce Thulium con el tiempo: **40 por hora en el nivel 1, 1.280 en el nivel 20** (nivel 5: 144; nivel 10: 360; nivel 15: 760). Construirla cuesta 5.000 créditos y 500 Thulium.
- Ambas necesitan energía, y cada una almacena 72 horas de lo que produce hasta que lo recoges.
- Una [Philosopher's Stone](/wiki/06-Items/Special-Items.md#philosophers-stone) hace que las dos granjas produzcan el doble durante 10 horas, y un [Workforce Contract](/wiki/06-Items/Special-Items.md#workforce-contract) contratado como **Foreman** hace lo mismo con cada productor durante 1 hora. Lo extra va a la tolva, así que recoge antes de que se llene.

## La cadena de suministro {#the-supply-chain}

Cuatro módulos convierten el tiempo que pasas lejos del teclado en las placas para tus mejores láseres. El mineral proviene **únicamente** de los colectores (todos los materiales y monedas están en la página [Recursos](/wiki/06-Items/Resources.md)): los alienígenas no lo sueltan y la tienda no lo vende. (Una [excavadora gigante](/wiki/03-Mechanics/Giant-Excavator.md) también suelta algo de Velkonite y Orvium en cajas, pero ese mineral va a tu carga, y solo la [Bahía de mineral](#ore-bay) lo pasa al Almacén de recursos, de donde lo toman la Forja y el Centro de investigación.)

1. Un **colector** extrae mineral, una cantidad por hora, en su propia tolva (72 horas de producción).
2. **Recoger** pasa el mineral de la tolva al **Almacén de recursos**, la reserva, donde cada mineral se guarda por separado.
3. La **Forja** toma de la reserva el mineral que necesita cuando empieza un lote y hace placas, a 10 segundos por placa, un lote a la vez.
4. **Recoger placas** pasa las placas terminadas a tu inventario (tu nave debe estar aterrizada). El [Ensamblaje](/wiki/06-Items/Lasers.md) las convierte en un Quantum Laser III, un Starfire-III o un Helios Beam y, una de cada con 5 Dark Matter, en una Dark Matter Plate, que piden [la Forja de Ensamblaje](/wiki/06-Items/Forge.md) y el último nivel de cada cadena de mejora.

### Colector de Velkonite y Colector de Orvium {#velkonite-collector-and-orvium-collector}

- **Mineral**: el Colector de Velkonite extrae **10 Velkonite por hora** en el nivel 1 y el Colector de Orvium **10 Orvium por hora**, y cada nivel tiene su propio ritmo: hasta 80 Velkonite y 40 Orvium por hora en el nivel 20 (nivel 5: 18 y 14 por hora; nivel 10: 32 y 24).
- **Tolva**: cada uno almacena 72 horas de su mineral y deja de extraer cuando se llena.
- **Recoger**: pasa el mineral al Almacén de recursos, hasta donde haya sitio. Sin almacén construido, o con la reserva de ese mineral llena, no hay dónde ponerlo y el botón dice por qué. El resto se queda en la tolva.
- **Energía**: 20 (Velkonite) y 30 (Orvium) en el nivel 1, con un aumento del 15 % por nivel.

### Almacén de recursos {#resource-storage}

- **Reserva**: guarda el Velkonite y el Orvium por separado y almacena una cantidad distinta de cada uno: **240 de cada uno en el nivel 1**, hasta 7.680 de Velkonite y 3.840 de Orvium en el nivel 20 (nivel 5: 720 y 560; nivel 10: 1.920 y 1.440).
- **Límite**: un día de la producción de su colector en el nivel 1, hasta cuatro días en el nivel 20. La tolva de un colector guarda tres días, así que desde el nivel 13 la reserva guarda al menos una tolva llena.
- **Por encima del límite**: si una reserva guarda más que su límite (el pago de la actualización 0.4.10 pudo dejarla así), no se quita nada, pero Recoger no añade más de ese mineral hasta que hayas gastado algo.
- El mineral entra al recoger de un colector o, desde tu inventario, por la [Bahía de mineral](#ore-bay), y sale solo hacia la Forja y el Centro de investigación. Nunca vuelve a tu inventario.
- **El mineral guardado se conserva** tras el reinicio de la temporada, y no ocupa sitio en el [Alijo de Transporte](/wiki/03-Mechanics/Wipe-Timeline.md#transport-cache-travel-capsule-).
- **Energía**: 10 en el nivel 1, con un aumento del 10 % por nivel. No se puede apagar.

### Forja {#forgery}

- **Placas**: la Forja hace una **Velkonite Reinforced Plate** a partir de Velkonite y una **Orvium Reinforced Plate** a partir de Orvium: **40 Velkonite** u **80 Orvium** por placa en el nivel 1, y baja con cada nivel hasta 30 y 60 en el nivel 20 (nunca por debajo del 75 %).
- **Lotes**: un lote de un solo tipo de placa a la vez, de **10 placas en el nivel 1** y 5 más por cada nivel superior. El mineral sale del Almacén de recursos en el momento en que empieza el lote, y cada placa tarda **10 segundos**. Las placas se hacen una tras otra, también mientras estás fuera.
- **Recoger placas**: pasa las placas terminadas a tu inventario mientras tu **nave está aterrizada**, y el resto del lote sigue en marcha. Se puede empezar un lote nuevo cuando la Forja está vacía.
- Un lote en marcha termina aunque apagues la Forja o la mejores. Un lote **nuevo** necesita que la Forja esté encendida, que no se esté mejorando y que la energía del Skylab esté en equilibrio.
- **Energía**: 30 en el nivel 1, con un aumento del 15 % por nivel.
- **No comercializable**: las placas que fabrica la Forja no se pueden vender en la [Subasta](/wiki/03-Mechanics/Auction.md#marketable-items); si no, serían el mayor producto de su Mercado. Siguen sirviendo como material para el Ensamblaje y la Forja.

### Construirlos {#building-them}

Los dos colectores cuestan **10 Ship Fragments, 20.000 créditos y 500 de Thulium** cada uno, el Almacén de recursos **10 Ship Fragments, 5.000 créditos y 250 de Thulium** y la Forja **10 Ship Fragments, 5.000 créditos y 500 de Thulium**; los cuatro necesitan el Núcleo en el nivel 5.

- Los Ship Fragments se toman de tu inventario (no del Alijo de Transporte) y tu nave debe estar aterrizada. La ficha de construcción muestra lo que tienes frente a lo que hace falta, y lo que te falta.
- Consumen energía. Antes de construir, la ficha muestra tu balance de energía ahora y después: **construir puede dejar una estación en déficit** cuando su Solar va por detrás de los demás módulos, y un déficit detiene todas las granjas y colectores. Apaga un módulo o mejora primero Solar.
- Los dos colectores cuelgan de estructuras sobre la estación, el Almacén de recursos está en el puerto noreste del Núcleo y la Forja en su puerto noroeste.

## El Centro de investigación {#the-research-centre}

El noveno módulo convierte recursos en ciencia e investiga las tecnologías que Ensamblaje necesita antes de fabricar nada nuevo. Se construye desde el nivel 10 del Núcleo, tiene los niveles 1 a 10, consume energía y no se puede apagar. Sus números, lo que quema como combustible, el impulso y todo el árbol de tecnologías están en la página [Investigación](/wiki/03-Mechanics/Research.md). Las tecnologías más altas necesitan además Dark Matter, que añades al Centro: [Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md) explica cómo conseguirlo. Los niveles del Módulo de motores, del Módulo de defensa y del Módulo de radar también son tecnologías, y se investigan aquí (consulta [Investigación](/wiki/03-Mechanics/Research.md#module-technologies)).

## El puente y el Núcleo 2 {#the-bridge-and-core-2}

La mejora del Núcleo al **nivel 10** construye un **puente** y un segundo Núcleo. El puente se acopla al puerto norte del Núcleo, donde estaba Solar, y lo une en el extremo lejano con el **Núcleo 2**.

- **Coste**: el paso del nivel 9 al nivel 10 cuesta **2.000 de Thulium** además de sus 38.443 créditos, y dura lo mismo que antes, 1 h 20 min. El puente y el Núcleo 2 no cuestan nada más y no tardan tiempo propio. Una mejora que ya estaba en marcha conserva el precio con el que empezó, y un Núcleo en el nivel 10 o más no paga nada.
- **El Núcleo 2 no tiene nivel**: no hay nada que mejorar ni que pagar. Da a tu estación **seis ranuras más para módulos**, y la ficha del Núcleo muestra cuántas están libres.
- **Solar se traslada**: Solar deja el puerto norte del Núcleo, que ahora ocupa el puente, y pasa al puerto norte del Núcleo 2, en el extremo lejano de la estación. Su nivel, su energía y una mejora en curso quedan intactos.
- **Una regla, no una obra**: dónde está cada módulo depende solo del nivel del Núcleo. El puente aparece en el momento en que termina la mejora del Núcleo al nivel 10 (un sonido suave y un mensaje te lo dicen), y un Skylab cuyo Núcleo ya está en el nivel 10 o más lo tiene en la siguiente visita. No se pierde ni se borra ningún módulo, y solo Solar cambia de sitio.
- **Ranuras**: la **Impresora de munición** ocupa la ranura noreste del Núcleo 2, la **Fábrica de cohetes** la noroeste y la **Bahía de mineral** su estructura este; las otras tres quedan libres para módulos futuros. Las tres solo se pueden construir cuando el Núcleo 2 ya existe: antes, el botón de construir dice «Requiere Núcleo 2».
- **Niveles**: un módulo del Núcleo 2 sigue el nivel del Núcleo como cualquier otro módulo: ninguno pasa del Núcleo, así que el Núcleo 2 añade ranuras, no niveles.

### Impresora de munición {#ammo-printer}

La Impresora de munición imprime munición láser de la nada, de un tipo cada vez: sin mineral y sin créditos, solo energía. Tiene los niveles 1 a 20.

- **Producción**: **x2** (Advanced Plasma) **100 por hora en el nivel 1, 2.000 en el nivel 20** (100 más por cada nivel); **x3** (Ultra Core) la mitad, de 50 a 1.000; **x4** (Experimental Fusion Core) una cuarta parte, de 25 a 500.
- **Modo**: eliges x2, x3 o x4 en su ficha o su ventana. Un cambio conserva las horas ya almacenadas y las cuenta desde entonces a la tasa del nuevo modo.
- **Almacenamiento**: un día, 24 horas de producción al nivel y en el tipo que estén en uso (2.400 de x2 en el nivel 1, 48.000 en el nivel 20). El tiempo sin conexión cuenta, y un almacén lleno simplemente se detiene.
- **Recoger**: pasa las unidades enteras a tu inventario mientras tu **nave está aterrizada**. La munición no tiene límite de carga, y la parte de una unidad se queda y sigue contando.
- **Energía**: 40 en el nivel 1, con un aumento del 20 % por nivel. Con un déficit de energía se detiene como las granjas y los colectores, y lo que guarda se queda y se puede recoger.
- **Construcción**: 20.000 créditos, 500 de Thulium y 10 Ship Fragments (de tu inventario, con la nave aterrizada), solo en el Núcleo 2. Sus mejoras cuestan desde 21.000 créditos y 140 de Thulium hasta 5.600.000 créditos y 11.000 de Thulium, y duran lo mismo que las de la Forja, de 5 minutos a 24 horas y 5 d 13 h en total (consulta las tablas de más abajo).
- **No comercializable**: lo que imprime no se puede vender en la [Subasta](/wiki/03-Mechanics/Auction.md#marketable-items).

### Fábrica de cohetes {#rocket-factory}

La Fábrica de cohetes fabrica cohetes de la tienda de la nada, de un tipo cada vez. Tiene los niveles 1 a 20.

- **Qué fabrica**: uno solo de los doce cohetes de la tienda, el que elijas: Lancet, Rivet, Scatter o Ember, gamas I, II y III. El N.U.K.E. y el N.I.K.E. no se fabrican nunca.
- **Producción**: la gama III **0,5 por hora en el nivel 1, 10 en el nivel 20** (0,5 más por cada nivel), la gama II 1,25 veces eso y la gama I el doble. Solo cuentan los cohetes enteros: la parte de uno se queda y sigue contando.
- **Almacenamiento**: un día, 24 horas de producción al nivel y con el cohete en uso (240 de la gama III en el nivel 20). El tiempo sin conexión cuenta, un almacén lleno simplemente se detiene, y un cambio de cohete conserva las horas ya almacenadas.
- **Recoger**: pasa los cohetes a tu inventario mientras tu **nave está aterrizada**, tantos como puedas llevar: como máximo 5.000 de la gama I, 2.000 de la gama II y 500 de la gama III, el límite de la propia tienda. Lo que no cabe se queda en la fábrica.
- **Energía**: 24 en el nivel 1, con un aumento del 15 % por nivel. Con un déficit de energía se detiene como la impresora.
- **Construcción**: 20.000 créditos, 500 de Thulium y 15 Ship Fragments (de tu inventario, con la nave aterrizada), solo en el Núcleo 2. Sus mejoras cuestan una cuarta parte de las de la impresora, desde 5.300 créditos y 35 de Thulium hasta 1.400.000 créditos y 2.800 de Thulium, y duran lo mismo: 5 d 13 h en total.
- **No comercializable**: lo que fabrica no se puede vender en la [Subasta](/wiki/03-Mechanics/Auction.md#marketable-items).

### Bahía de mineral {#ore-bay}

La Bahía de mineral pasa al Almacén de recursos el mineral que llevas contigo. Una [excavadora gigante](/wiki/03-Mechanics/Giant-Excavator.md) suelta Velkonite y Orvium en cajas que van a tu carga, donde ningún módulo los usa; la Bahía de mineral es el camino desde allí hasta el banco, de donde lo toman la Forja y el Centro de investigación. Tiene los niveles 1 a 20.

- **Qué mueve**: **Velkonite y Orvium**, los dos minerales que guarda el Almacén de recursos. La Cataclysite y el Quorvium son combustible que el Centro de investigación y [la Forja de Ensamblaje](/wiki/06-Items/Forge.md) toman directamente de tu inventario, y el Thulium va a tu cuenta al recogerlo.
- **En un solo sentido**: de tu inventario al Almacén de recursos, nunca de vuelta. Solo se mueve el mineral suelto de tu inventario, nunca el del Alijo de Transporte.
- **Cómo**: tu **nave debe estar aterrizada**. Una transferencia es instantánea: en la hoja de la Bahía de mineral elige el mineral, escribe una cantidad o pulsa Máx. y pulsa **Mover**. La hoja muestra lo que llevas y lo que guarda el banco frente a su capacidad.
- **Cupo**: el nivel fija cuánto mineral mueve por hora, **30 en el nivel 1, 960 en el nivel 20**, y guarda hasta un día de ello (720 en el nivel 1, 23.040 en el nivel 20). Una Bahía nueva empieza con un día entero, y una mejora conserva lo almacenado. Una transferencia se corta en el mineral que llevas, en el espacio que le queda al Almacén de recursos y en el cupo, y la hoja dice cuál. Un día de cupo equivale a unas tres veces lo que el Almacén de recursos guarda de un mineral en el mismo nivel, así que casi siempre es el espacio lo que detiene una transferencia; el cupo solo cuenta si haces pasar mineral por el almacén una y otra vez en un mismo día.
- **Hauler**: un [Workforce Contract](/wiki/06-Items/Special-Items.md#workforce-contract) contratado como **Hauler** levanta el cupo durante 1 hora. La Bahía mueve entonces todo lo que permitan tu carga y el sitio del Almacén de recursos, y el cupo que tenía guardado queda como estaba.
- **Energía**: 15 en el nivel 1, con un aumento del 10 % por nivel (92 en el nivel 20). Se puede apagar. Con un déficit de energía, mientras está apagada y mientras se mejora, no mueve nada.
- **Construcción**: 5.000 créditos, 250 de Thulium y 10 Ship Fragments (de tu inventario, con la nave aterrizada), solo en el Núcleo 2. Sus mejoras cuestan lo que las del Almacén de recursos y tardan lo mismo (consulta las tablas de más abajo).
- **No es un camino a más mineral**: mueve mineral que ya tienes. Una tanda de la excavadora se limita en su origen, y la capacidad del Almacén de recursos limita el banco.

## El segundo puente y el Núcleo 3 {#the-second-bridge-and-core-3}

La mejora del Núcleo al **nivel 15** construye un **segundo puente** y un tercer Núcleo, y los cuatro módulos de la Expedición ocupan allí sus ranuras. El puente II se acopla al puerto norte del Núcleo 2, donde estaba Solar, y lo une en el extremo lejano de la estación con el **Núcleo 3**: el mismo esquema del nivel 10, una vez más.

- **Coste**: el paso del nivel 14 al nivel 15 cuesta **4.000 de Thulium** además de sus créditos, y dura lo mismo que antes, 14 h. El puente II y el Núcleo 3 no cuestan nada más y no tardan tiempo propio. Una mejora que ya estaba en marcha conserva el precio con el que empezó, y un Núcleo en el nivel 15 o más no paga nada.
- **El Núcleo 3 no tiene nivel**: no hay nada que mejorar ni que pagar. Da a tu estación **cuatro ranuras más para módulos**, y la ficha del Núcleo muestra cuántas están libres.
- **Solar se traslada otra vez**: Solar deja el puerto norte del Núcleo 2, que ahora ocupa el puente II, y pasa al puerto norte del Núcleo 3, en el extremo lejano de la estación. Su nivel, su energía y una mejora en curso quedan intactos.
- **Una regla, no una obra**: dónde está cada módulo depende solo del nivel del Núcleo. El Núcleo 3 aparece en el momento en que termina la mejora del Núcleo al nivel 15, y un Skylab cuyo Núcleo ya está en el nivel 15 o más lo tiene en la siguiente visita. No se pierde ningún módulo, y solo Solar cambia de sitio.
- **Ranuras**: el **Módulo de defensa** ocupa la ranura noreste del Núcleo 3, el **Módulo de radar** la noroeste, la **Bahía de trofeos** su estructura este y el **Módulo de motores** su estructura oeste. Sus dos puertos del sur miran a los módulos del Núcleo 2 y quedan vacíos. Los cuatro solo se pueden construir cuando el Núcleo 3 ya existe: antes, el botón de construir está bloqueado y dice que requiere el Núcleo de nivel 15.
- **Niveles**: un módulo del Núcleo 3 sigue el nivel del Núcleo como cualquier otro: ninguno pasa del Núcleo. Los módulos de motores y de defensa llegan al nivel 5, el de radar al nivel 3 y la Bahía de trofeos al nivel 20.
- **Qué pide una construcción**: además de créditos y Thulium, **Ship Fragments** y, para los módulos de motores, de defensa y de radar, **Dark Matter Plates** de tu inventario (no del Alijo de Transporte), tomadas con la nave aterrizada, y la **tecnología** del nivel, investigada en el Centro de investigación. Un paso que pide placas las pide del mismo modo.

**Las tecnologías.** Cada nivel de los módulos de motores, de defensa y de radar es una tecnología de la familia Skylab en la vista Investigación, se investiga por orden y hace falta antes de poder construir ese nivel o mejorar hasta él. Los tres módulos comparten los tiempos (el módulo de radar llega al nivel 3):

| Nivel | Tiempo de investigación | Dark Matter |
| :--- | ---: | ---: |
| 1 | 3 h | 0 |
| 2 | 10 h | 5 |
| 3 | 1 d | 10 |
| 4 | 2 d | 15 |
| 5 | 3 d | 20 |

Las tecnologías de los tres módulos piden 115 Dark Matter y 14 d 15 h de investigación a la velocidad normal (consulta [Investigación](/wiki/03-Mechanics/Research.md#module-technologies)).

### Módulo de motores {#engine-module}

El Módulo de motores aloja los motores que hacen volar tu Skylab. Tiene los niveles 1 a 5, y cada nivel admite un motor más. Los motores que montes y el peso de toda la estación deciden a qué velocidad vuela (consulta [Peso y velocidad](#weight-and-speed)).

- **Qué se monta**: objetos [Engine](/wiki/06-Items/Propulsion.md) con sus propulsores dentro, de tu inventario: un Engine I, II o III. Un Adaptive Core no encaja: su bonificación de velocidad es cosa de una nave. Un motor conserva sus propulsores y sus mejoras de la Forja cuando lo sacas otra vez.
- **Cómo**: tu **nave debe estar aterrizada** y el Skylab no puede estar de viaje. La ficha del motor de la ventana Universo enumera tus motores sueltos: arrastra uno a una ranura libre o haz clic en él, y haz clic en un motor montado para sacarlo. La ficha muestra además el empuje, el peso, la velocidad y cuánto dura un salto.
- **Un viaje exige**: el módulo construido, encendido, sin estar en mejora y con al menos un motor.
- **Investigación**: cada nivel necesita su propia tecnología, Módulo de motores I a V (consulta la tabla de arriba).
- **Energía**: 60 en el nivel 1, con un aumento del 25 % por nivel. Se puede apagar, pero no mientras el Skylab está de viaje.
- **Construcción**: 375.000 créditos, 1.500 de Thulium, 20 Ship Fragments y 1 Dark Matter Plate, solo en el Núcleo 3.
- **Mejora**: el módulo está desconectado mientras se mejora. La mejora del Módulo de motores espera al final del viaje, porque la velocidad de un viaje queda fijada al salir.

| Nivel | Motores | Créditos | Thulium | Placas | Tiempo |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 (la construcción) | 1 | 375.000 | 1.500 | 1 | – |
| 2 | 2 | 825.000 | 3.300 | 2 | 2 h |
| 3 | 3 | 1.825.000 | 7.300 | 3 | 6 h |
| 4 | 4 | 4.000.000 | 16.000 | 5 | 1 d |
| 5 | 5 | 8.750.000 | 35.000 | 8 | 2 d |

Las placas son Dark Matter Plates, y el tiempo es el de la mejora hasta el nivel. En total, los cinco niveles cuestan 15.775.000 créditos, 63.100 de Thulium, 19 placas y 3 d 8 h de mejora.

### Módulo de defensa {#defense-module}

El Módulo de defensa combate por tu Skylab. Aloja los láseres que disparan a los alienígenas de las celdas a las que vuela tu Skylab y el cargador del que disparan. Tiene los niveles 1 a 5, y su nivel decide cuántos láseres admite, cuántos disparos, cuánto puede ganar por hora y cuán peligrosa puede ser una celda en la que entre.

- **Qué se monta**: objetos [Laser](/wiki/06-Items/Lasers.md) con sus amplificadores dentro, de tu inventario: un Quantum Laser I, II o III, un Starfire-III o un Helios Beam. Todos los láseres disparan a la vez, uno por segundo cada uno. Los amplificadores cuentan como en una nave (daño, probabilidad de crítico y daño crítico); un Penetration Amp no aporta nada aquí.
- **El cargador** guarda disparos de los tipos de la Impresora de munición y se llena **solo desde la Impresora de munición**, nunca desde tu inventario (consulta [Montaje y munición](#fits-and-ammunition)).
- **La puerta**: una celda de dificultad 3, por ejemplo, solo la puede pisar un Skylab cuyo Módulo de defensa esté en el nivel 3 o más. Un Skylab sin Módulo de defensa solo puede cruzar el espacio vacío y su puerto.
- **El presupuesto de bajas** es lo máximo que el Skylab puede ganar por hora: 108 puntos de recompensa en el nivel 1 y 630 en el nivel 5 (consulta [Lo que paga un viaje](#what-a-trip-pays)).
- **El casco** crece con el nivel (consulta [El casco, la destrucción y la reparación](#the-hull-and-repair)).
- **Investigación**: cada nivel necesita su propia tecnología, Módulo de defensa I a V (consulta la tabla de arriba).
- **Energía**: 80 en el nivel 1, con un aumento del 25 % por nivel. Se puede apagar, pero no mientras el Skylab está de viaje. Un módulo apagado, en mejora o sin energía está oscuro: el Skylab no combate nada y pasa por las celdas sin luchar.
- **Construcción**: 500.000 créditos, 2.000 de Thulium, 25 Ship Fragments y 1 Dark Matter Plate, solo en el Núcleo 3.

| Nivel | Láseres | Cargador (disparos) | Presupuesto de bajas (puntos por hora) | Dificultad máxima |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 1 | 1.300 | 108 | 1 |
| 2 | 2 | 3.600 | 293 | 2 |
| 3 | 3 | 14.000 | 476 | 3 |
| 4 | 4 | 23.000 | 548 | 4 |
| 5 | 5 | 35.000 | 630 | 5 |

| Nivel | Créditos | Thulium | Placas | Tiempo |
| :--- | ---: | ---: | ---: | ---: |
| 1 (la construcción) | 500.000 | 2.000 | 1 | – |
| 2 | 1.150.000 | 4.600 | 2 | 3 h |
| 3 | 2.750.000 | 11.000 | 4 | 9 h |
| 4 | 6.000.000 | 24.000 | 7 | 1 d 12 h |
| 5 | 14.000.000 | 56.000 | 12 | 3 d |

En total, los cinco niveles cuestan 24.400.000 créditos, 97.600 de Thulium, 26 placas y 5 d de mejora.

### Módulo de radar {#radar-module}

El Módulo de radar disipa la niebla del mapa del universo (consulta [Niebla y escaneo](#fog-and-scanning)). Tiene los niveles 1 a 3, y un nivel más alto escanea una celda más rápido.

- **Qué hace**: escanea **una celda cada vez**, entre las celdas contiguas a una que conoces, y mantiene una **cola de tres**: la primera se está escaneando y las otras esperan. Cuando un escaneo termina, conoces la celda y tu Skylab puede volar allí.
- **Tiempo**: 90 minutos por celda en el nivel 1, 40 en el nivel 2 y 15 en el nivel 3. Un escaneo corre con el reloj del servidor, también mientras estás fuera y mientras el Skylab vuela. Se detiene, y el tiempo no se recupera, mientras el módulo está apagado, en mejora o sin energía y mientras el Skylab está destruido. Un escaneo cuesta tiempo y nada más.
- **Cartografiarlo todo**: cartografiar las 131 celdas que no conoces al principio, una tras otra, lleva 8 d 4 h en el nivel 1, 3 d 15 h en el nivel 2 y 1 d 9 h en el nivel 3.
- **Investigación**: cada nivel necesita su propia tecnología, Módulo de radar I a III (consulta la tabla de arriba).
- **Energía**: 40 en el nivel 1, con un aumento del 30 % por nivel. Se puede apagar, pero no mientras el Skylab está de viaje.
- **Construcción**: 250.000 créditos, 1.000 de Thulium y 15 Ship Fragments, solo en el Núcleo 3.

| Nivel | Tiempo de escaneo | Créditos | Thulium | Placas | Tiempo |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 (la construcción) | 90 min | 250.000 | 1.000 | 0 | – |
| 2 | 40 min | 750.000 | 3.000 | 1 | 4 h |
| 3 | 15 min | 2.250.000 | 9.000 | 3 | 1 d |

En total, los tres niveles cuestan 3.250.000 créditos, 13.000 de Thulium, 4 placas y 1 d 4 h de mejora.

### Bahía de trofeos {#trophies-bay}

La Bahía de trofeos guarda lo que traen las bajas de tu Skylab hasta que lo recojas. Tiene los niveles 1 a 20 y no necesita tecnología.

- **Qué guarda**: créditos, Thulium, experiencia, honor y el botín de las bajas.
- **La capacidad** se cuenta en **puntos de recompensa**: una baja suma la recompensa de su alienígena, créditos divididos entre 200 más Thulium, sea lo que sea lo que suelte (las cifras de Alpha en todos los mundos). Guarda 650 puntos en el nivel 1 y 45.000 en el nivel 20.
- **Llena**: una bahía llena hace que el Skylab **deje de disparar**: no se mata, ni se paga, ni se cuenta nada y no se gasta munición hasta que recojas (el casco sigue recuperándose). Un mensaje, un aviso emergente, una etiqueta ámbar **Bahía llena** en la barra de la estación, un aviso en la página del Skylab y el aviso de la fila del Skylab en la barra lateral te lo dicen.
- **Recoger** en la ventana Universo, con la nave aterrizada: los créditos y el Thulium van a tu cuenta, la experiencia y el honor a tu piloto y el botín a tu inventario. Dos recogidas a la vez pagan una sola vez.
- **El botín** se tira para cada baja a partir de lo que suelta el alienígena, nunca Dark Matter, Ancient Control Units, N.I.K.E. ni N.U.K.E. **No es comercializable**: no se puede vender en la [Subasta](/wiki/03-Mechanics/Auction.md#marketable-items).
- **Energía**: 20 en el nivel 1, con un aumento del 10 % por nivel. Se puede apagar, pero no mientras el Skylab está de viaje.
- **Construcción**: 100.000 créditos, 400 de Thulium y 10 Ship Fragments, solo en el Núcleo 3. Sus mejoras cuestan desde 117.500 créditos y 470 de Thulium (15 minutos) hasta 2.325.000 créditos y 9.300 de Thulium (1 d 13 h): 14.722.500 créditos y 58.890 de Thulium en total, y 6 d 8 h.

| Nivel | Capacidad (puntos) | Créditos | Thulium | Tiempo |
| :--- | ---: | ---: | ---: | ---: |
| 1 (la construcción) | 650 | 100.000 | 400 | – |
| 2 | 810 | 117.500 | 470 | 15 min |
| 5 | 1.600 | 195.000 | 780 | 34 min |
| 10 | 4.800 | 450.000 | 1.800 | 2 h 18 min |
| 15 | 15.000 | 1.025.000 | 4.100 | 9 h 14 min |
| 20 | 45.000 | 2.325.000 | 9.300 | 1 d 13 h |

Cuánto tarda en llenarse una bahía cuando el Skylab gana todo el presupuesto de bajas de su nivel de defensa (una bahía más pequeña se llena antes, un presupuesto menor tarda más):

| Nivel de defensa | Bahía nivel 1 | Bahía nivel 5 | Bahía nivel 10 | Bahía nivel 15 | Bahía nivel 20 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 | 6 h 1 min | 14 h 49 min | 1 d 20 h | 5 d 19 h | 17 d 9 h |
| 2 | 2 h 13 min | 5 h 28 min | 16 h 23 min | 2 d 3 h | 6 d 10 h |
| 3 | 1 h 22 min | 3 h 22 min | 10 h 5 min | 1 d 8 h | 3 d 22 h |
| 4 | 1 h 11 min | 2 h 55 min | 8 h 46 min | 1 d 3 h | 3 d 10 h |
| 5 | 1 h 2 min | 2 h 32 min | 7 h 37 min | 23 h 49 min | 2 d 23 h |

## Peso y velocidad {#weight-and-speed}

Cada módulo pesa algo, en **unidades de masa (MU)**, y una estación más pesada vuela más despacio. Un módulo pesa más con cada nivel, uno sin construir no pesa nada y uno en mejora pesa el nivel que tiene. Los motores y láseres que montas no cuentan: el peso del módulo ya los incluye.

| Módulo | Nivel 1 | Nivel 5 | Nivel 10 | Nivel 15 | Nivel máximo |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Núcleo | 100 | 148 | 208 | 268 | 328 |
| Solar | 60 | 84 | 114 | 144 | 174 |
| Granja de créditos | 60 | 84 | 114 | 144 | 174 |
| Granja de Thulium | 80 | 118 | 166 | 214 | 262 |
| Colector de Velkonite | 70 | 92 | 120 | 148 | 176 |
| Colector de Orvium | 70 | 92 | 120 | 148 | 176 |
| Almacén de recursos | 70 | 92 | 120 | 148 | 176 |
| Forja | 80 | 112 | 152 | 192 | 232 |
| Centro de investigación | 60 | 89 | 125 | – | 125 |
| Impresora de munición | 60 | 84 | 114 | 144 | 174 |
| Fábrica de cohetes | 60 | 84 | 114 | 144 | 174 |
| Bahía de mineral | 40 | 53 | 69 | 85 | 101 |
| Módulo de motores | 80 | 144 | – | – | 144 |
| Módulo de defensa | 100 | 180 | – | – | 180 |
| Módulo de radar | 30 | – | – | – | 39 |
| Bahía de trofeos | 50 | 60 | 73 | 85 | 98 |
| **La estación entera: todos los módulos que hay a ese nivel del Núcleo, a ese nivel** | 300 | 824 | 1.537 | 2.353 | 2.734 |

El nivel máximo es 20, salvo para el Centro de investigación (10), los módulos de motores y de defensa (5) y el módulo de radar (3). La estación entera pesa 2.353 MU con el Núcleo en el nivel 15 y 2.734 MU en el nivel 20.

- **El empuje** es la aritmética de motores de las naves, sin velocidad base: un motor aporta su velocidad base más la velocidad fija de sus propulsores, multiplicada por sus multiplicadores; los motores se ordenan del mejor al peor y los cuatro primeros cuentan al 100 % y el quinto al 85 % (el módulo admite cinco como máximo); y encima se suman las cuatro mejores bonificaciones de velocidad. Una estación sin motor no tiene empuje.
- **La velocidad** es 60 veces el empuje dividido entre el peso de la estación, en unidades por segundo, y un salto entre dos celdas vecinas son 15.000 unidades. Bajo la energía, la página del Skylab muestra la línea «Peso 2.353 MU, velocidad 7,8 unidades/s, un salto 32 min».
- **Fijada al salir**: la velocidad de un viaje se calcula al salir, con el peso y el empuje de ese momento. Una mejora que termina por el camino, o un motor que cambias mientras el Skylab está estacionado, cuenta para el siguiente viaje.

Lo que hacen los motores en una estación con todos los módulos en el nivel 15 (el Módulo de motores en el nivel que aloja los motores):

| Motores montados | Peso (MU) | Empuje | Velocidad (unidades por segundo) | Un salto | A través del mapa (14 saltos) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 Engine I (Módulo de motores nivel 1) | 2.289 | 2,0 | 0,05 | 3 d 6 h | 45 d 11 h |
| 3 Engine II, cada uno con 2 Impulse Thruster II (nivel 3) | 2.321 | 73,6 | 1,90 | 2 h 11 min | 1 d 7 h |
| 5 Engine III, cada uno con 3 Impulse Thruster IV (nivel 5) | 2.353 | 305,5 | 7,79 | 32 min | 7 h 29 min |

Con el Núcleo en el nivel 20 la estación pesa un 16 % más, y los mejores motores tardan 37 minutos en un salto y 8 h 42 min en cruzar el mapa.

## Expediciones {#expeditions}

Una **expedición** es un viaje de tu Skylab por el **mapa del universo**. Vuela a una celda, caza allí a los alienígenas con los láseres de su Módulo de defensa y llena la Bahía de trofeos con lo que traen las bajas. Todo corre con el reloj del servidor, así que continúa mientras no estás conectado, y ningún jugador puede atacar al Skylab: lo único que le hace daño es el peligro de la celda (consulta [El casco, la destrucción y la reparación](#the-hull-and-repair)). Planeas un viaje en la ventana **Universo**, que abre el botón Universo de la cabecera de la página del Skylab.

Qué hace falta: un Núcleo en el nivel 15, una corporación (su puerto es el puerto base de tu Skylab) y un mundo; para un viaje, un Módulo de motores con un motor montado; para ganar algo, un Módulo de defensa con un láser y munición de tu Impresora de munición, y una Bahía de trofeos donde guardarlo. Todo lo demás sigue mientras el Skylab está fuera: las granjas, los colectores, la Forja, la Impresora, la Fábrica, la Bahía de mineral y el Centro de investigación funcionan con sus propios relojes, y tu nave se puede pilotar como siempre.

### El mapa del universo {#the-universe-map}

El mapa es la **capa propia** del Skylab, no los sectores del juego ni una vista de ellos: sus celdas no son mapas del juego, las puertas de salto no están en él, nada en él se pilota en tiempo real y sus alienígenas son solo una cantidad y un peligro. Se toca con el resto del juego a través de lo que paga: créditos, Thulium, experiencia, honor, botín y bajas para las misiones.

- **El campo**: 15 columnas y 10 filas de celdas hexagonales, **150 en total**. Una celda tiene un código, la letra de la columna y el número de la fila (A1 a O10), y, cuando la conoces, un nombre y un tipo.
- **Puertos**: cada corporación tiene un **puerto**, una celda de dificultad 0: el de Mars es H3, el de Terra D8 y el de Galactic L8. Tu Skylab empieza en el puerto de tu corporación y vuelve allí tras un reinicio. En un puerto no se caza nada y nada ataca al Skylab.
- **La dificultad** va de 1 a 5 y crece con la distancia al puerto más cercano: las seis celdas junto a un puerto son siempre de dificultad 1, y cada salto más lejos suma uno, hasta 5. Aproximadamente una quinta parte de las celdas es un grado más fácil de lo que dice su distancia y una cuarta parte un grado más difícil, y unas pocas son **espacio vacío**, dificultad 0.
- **Tipos**: un **nido** guarda a todos los alienígenas de su dificultad y una **deriva**, la mayoría de las celdas, tres quintas partes de ellos. El espacio vacío no guarda nada ni a nadie, y un Skylab puede cruzarlo sin Módulo de defensa alguno.
- **Un mapa por mundo**: todos los pilotos de un mundo ven el mismo mapa, cada mundo tiene el suyo y cada temporada (el reinicio) hace uno nuevo.

Los alienígenas de un nido, por dificultad (una deriva guarda tres quintas partes de ellos, redondeadas):

| Dificultad | Alienígenas |
| :--- | :--- |
| 1 | 30 [Seekers](/wiki/04-Aliens/Seeker.md) |
| 2 | 20 Seekers y 10 [Phantasms](/wiki/04-Aliens/Phantasm.md) |
| 3 | 20 Phantasms, 10 [Bulwarks](/wiki/04-Aliens/Bulwark.md) y 5 [Goombahs](/wiki/04-Aliens/Goombah.md) |
| 4 | 20 Bulwarks, 10 Goombahs y 5 [Crystalys](/wiki/04-Aliens/Crystalys.md) |
| 5 | 6 [Slumbering Voids](/wiki/03-Mechanics/Dormant-Swamp.md), 3 [Dormant Pulses](/wiki/05-Swarms/Dormant-Swarm.md) y 1 Dormant Force |

### Niebla y escaneo {#fog-and-scanning}

Solo ves las celdas que conoces.

- **Al empezar una temporada** conoces tu puerto y los dos anillos de celdas que lo rodean: **19 celdas**, las mismas para toda corporación.
- **Una celda pasa a ser conocida** cuando tu Skylab la atraviesa o se detiene en ella, y cuando el radar termina de escanearla.
- **Una celda que no conoces** no muestra nada de sí misma: ni su tipo, ni su dificultad, ni su nombre, ni sus alienígenas. Una celda contigua a una conocida se marca con un **?** y se puede escanear; cualquier otra celda desconocida está oscura.
- **Una celda conocida** muestra en su panel su código, tipo, dificultad, nombre y alienígenas.
- **Se vuela** solo a celdas conocidas.
- **Escanear**: elige una celda **?** y pulsa **Escanear esta celda**. El radar escanea una celda cada vez y mantiene una cola de tres; una celda se puede sacar de la cola otra vez, y **Cancelar todo** la vacía. El tiempo de un escaneo está en el [Módulo de radar](#radar-module).

### El viaje {#the-trip}

Haz clic en una celda conocida del mapa: el panel de la celda muestra la **vista previa** del viaje, que el servidor planifica con tu Skylab tal como está ahora, y **Partir** envía allí al Skylab. Vuela salto a salto a la velocidad de sus motores, llega a la celda y **caza allí hasta que des otra orden**. **Llamar de vuelta** lo envía a su puerto por el camino conocido más corto.

- **La ruta** es la de menos saltos por celdas que conoces y cuya dificultad permite el nivel de tu Módulo de defensa. Entre rutas de la misma longitud se elige una, siempre la misma.
- **El reloj** es el del servidor: la llegada queda fijada cuando el Skylab sale, y un viaje continúa mientras no estás conectado. Una orden nueva dada por el camino surte efecto en la siguiente celda: el salto en curso se termina.
- **Qué detiene una orden**: ningún Módulo de motores, o uno apagado o en mejora; ningún motor montado; energía insuficiente; un Skylab destruido; la celda en la que ya está; una celda que no conoces; una celda demasiado difícil para tu Módulo de defensa; ninguna ruta conocida.
- **De viaje**, los cuatro módulos de la Expedición no se pueden apagar ni encender, el Módulo de motores no se puede mejorar y no se puede montar ni sacar nada. Por el camino se encuentra con los alienígenas de las celdas que atraviesa a la mitad del ritmo que tendría si se quedara allí.
- **Avisos**: un mensaje te dice cuándo llega el Skylab, cuándo lo destruyen o lo reparan y cuándo se llena su bahía, y los cuatro llevan además un sonido discreto propio.

Lo que dice la vista previa, en el orden de sus filas (cada cifra es la del servidor, para el equipo que tiene ahora tu Skylab):

| Fila | Qué dice |
| :--- | :--- |
| **Trayecto** | los saltos y el tiempo del viaje |
| **Llegada** | el momento en que llegaría, según tu reloj |
| **En el camino** | aproximadamente cuántos alienígenas encuentra en las celdas que atraviesa |
| **Bajas por hora** | cuántas bajas hace la estancia por hora y qué límite manda: los alienígenas que pasan, el presupuesto de bajas, el daño de tus láseres o tu munición |
| **Recompensa por hora** | lo que valen esas bajas, en puntos de recompensa |
| **Tu daño** | lo que hacen tus láseres por segundo con la mejor munición del cargador |
| **La celda exige** | el daño con el que la regeneración del casco aguanta justo la celda al ritmo que paga: con menos, el casco cae |
| **Casco** | Aguanta, o Destruido tras un tiempo |
| **Munición** | cuánto dura el cargador, o que alcanza para toda la estancia |
| **Bahía de trofeos** | cuánto tarda en llenarse, o que no se llena a este ritmo |

Sobre las filas, una **advertencia** dice cuándo el viaje no rendiría nada: nada que combatir en la celda, ningún láser montado, un cargador vacío que nada alimenta, ninguna Bahía de trofeos o un Módulo de defensa oscuro.

### Lo que paga un viaje {#what-a-trip-pays}

Una baja paga lo que paga su alienígena en tu mundo: sus créditos, su Thulium, su experiencia y su honor multiplicados por el pago del mundo (1, 2 y 3 en Alpha, Beta y Gamma), y su botín. No se añade nada: ningún potenciador, ningún premium, ninguna bonificación de formación, ningún impulso de clan y ninguna experiencia para tus drones.

Las bajas por hora son el menor de tres límites: los alienígenas que pasan, el **presupuesto de bajas** del nivel de tu Módulo de defensa, y lo que pueden hacer tus láseres y tu munición. El presupuesto es lo que mantiene a un Skylab desatendido como complemento de las granjas y no como segundo empleo: 108, 293, 476, 548 y 630 puntos de recompensa por hora en los niveles de defensa 1 a 5, donde un punto es 1 de Thulium o 200 créditos. **Una celda paga según su nivel**: a un Skylab se le paga el menor entre el presupuesto de su nivel de defensa y el presupuesto de la dificultad de la celda, así que un Skylab de Defensa 5 en una celda de dificultad 1 hace allí lo que uno de Defensa 1.

Lo máximo que paga un día en una celda (Alpha; Beta y Gamma pagan 1,6 y 2 veces más):

| Dificultad | Puntos de recompensa por hora | Bajas por día | Thulium por día | Créditos por día |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 108 | 288 | 1.152 | 288.000 |
| 2 | 293 | 469 | 3.124 | 780.911 |
| 3 | 476 | 224 | 5.524 | 1.181.375 |
| 4 | 548 | 86 | 5.503 | 1.528.510 |
| 5 | 630 | 32 | 5.255 | 1.972.329 |

Un día en una celda vale unas dos horas de cazar esa celda a mano (3,4 horas en dificultad 4). Desde la dificultad 3 es aproximadamente un 30 % de lo que una Granja de Thulium con el Núcleo en el nivel 15 hace en Thulium (18.240 por día) y de 0,6 a 1,1 veces lo que una Granja de créditos de ese nivel hace en créditos (1.836.000 por día). Una deriva de dificultad 2 guarda menos alienígenas de los que paga su presupuesto y hace algo menos.

El **botín** de una baja se tira a partir de lo que suelta su alienígena: Ship Fragments, minerales, Reinforced Hull Plates y Power Cores, y, desde la dificultad 5, munición Ultra Core y Experimental Fusion Core.

### El casco, la destrucción y la reparación {#the-hull-and-repair}

El Skylab tiene un **casco**, una reserva de puntos de vida, que **se recupera un 5 % de sí mismo por hora**, también bajo fuego. Los alienígenas con los que combate lo dañan en proporción a cuántos combate, lo fuertes que son y lo que dura la lucha: la vista previa dice si el casco aguanta y, si no, tras cuánto tiempo queda destruido el Skylab. Tiene 4.000.000 con el Núcleo en el nivel 15 y el Módulo de defensa en el nivel 1, un 12 % más por cada nivel del Núcleo por encima del 15 y más con un nivel de defensa más alto. Un Skylab sin Módulo de defensa tiene el casco del nivel 1 y no combate nada.

| Nivel de defensa | Núcleo nivel 15 | Núcleo nivel 20 |
| :--- | ---: | ---: |
| 1 | 4.000.000 | 7.049.367 |
| 2 | 4.800.000 | 8.459.240 |
| 3 | 6.000.000 | 10.574.050 |
| 4 | 8.800.000 | 15.508.607 |
| 5 | 11.200.000 | 19.738.227 |

- **Destruido**: cuando el casco se agota, el Skylab queda destruido donde estaba, en ese momento, y el viaje termina. Lo que guardaba la Bahía de trofeos se queda en ella. Todos los productores de la estación se detienen desde ese momento: las granjas, los colectores, la Impresora, la Fábrica y la Bahía de mineral no producen nada, la Forja no empieza ningún lote nuevo y el Centro de investigación ninguna investigación nueva (un lote o una investigación que ya están en marcha continúan), y los escaneos del radar se detienen.
- **Reparación**: pulsa **Reparar** en la ventana Universo. Es gratis y dura **60 segundos**; después el casco está entero y el Skylab vuelve a la celda en la que empezó su viaje. La producción se reanuda desde el final de la reparación. No se pierde nada, salvo el tiempo.
- **Avisos**: la página del Skylab muestra un aviso y una etiqueta en la barra de la estación mientras el Skylab está destruido o en reparación, y el aviso de la fila del Skylab en la barra lateral también lo dice.

### Montaje y munición {#fits-and-ammunition}

**Montaje.** Los motores van al Módulo de motores y los láseres al Módulo de defensa, uno por ranura, tomados de los objetos sueltos de tu inventario: no de una nave, no del Alijo de Transporte. Montar y sacar exigen tu **nave aterrizada** y el Skylab **sin estar de viaje**; un Skylab estacionado se puede reequipar, y las nuevas tasas cuentan desde ese momento. Un objeto montado conserva sus mejoras de la Forja y lo que lleva dentro (propulsores, amplificadores) y queda **reservado**: no se puede poner en una nave, borrar, poner en la Subasta, guardar en el Alijo de Transporte ni usar en la Forja y el Ensamblaje hasta que lo saques, y el Hangar, la hoja de venta de la Subasta y el Ensamblaje lo muestran atenuado.

**Munición.** El cargador guarda disparos de los tipos que fabrica la Impresora de munición y dispara primero el **multiplicador más alto**, un disparo por láser y segundo. Se llena **solo desde la Impresora de munición**, nunca desde tu inventario:

- **Alimentar desde la Impresora de munición** activado: lo que fabrica la Impresora va primero al cargador, hasta donde haya sitio; solo el resto espera en la tolva de la Impresora a que lo recojas.
- **Alimentar** desactivado: lo que fabrica la Impresora espera en su tolva, y **Cargar** pasa al cargador lo que contiene la tolva, con la nave aterrizada, hasta donde haya sitio.
- No se descarga: los disparos se disparan o se quedan.

Un Skylab sin láseres, sin munición o sin Bahía de trofeos no combate nada, y nada le hace daño tampoco.

### Bajas y misiones {#expedition-kills}

Las bajas de una expedición hacen avanzar un **paso de baja de tus misiones** solo cuando el paso **no nombra ningún sector**, hasta **250 bajas al día** (UTC) y solo las bajas del alienígena que nombra el paso. Una celda no es un sector, así que un paso que nombra uno (`x-1` a `x-4`, `DS-x` o `x-4` de otra corporación) nunca las cuenta, ni siquiera en una celda de la misma dificultad. En la práctica son las grandes cacerías de la línea de Desafíos cuyos alienígenas viven en una celda, y ninguna de las misiones de los niveles 1 a 8. Una misión con límite de tiempo, o un paso con límite de casco, tampoco las cuenta. Solo cuentan los pasos de baja: los objetos, las visitas y las estancias te necesitan a ti. La ficha del Skylab en la ventana Universo dice «Bajas de expedición hoy: N de 250».

Las bajas no dan puntos de reinicio y no cuentan para ninguna línea de clan, ninguna estadística de bajas ni puntos de clasificación (consulta [Misiones](/wiki/03-Mechanics/Quests.md#where-it-counts)).

### Tu clan lo ve {#clan-skylabs}

Los pilotos de tu clan ven dónde están los Skylabs de los demás: la columna **Skylab** de la lista de miembros da la celda («Atracado en H3», «H3, rumbo a K7 en 3 h 12 min», «Estacionado en K7», «Destruido en H3»), y la ventana Universo los dibuja como pequeños rombos dorados, con el nombre del piloto cuando señalas uno. Solo lo ve el clan, un camuflaje no oculta un Skylab y no hay interruptor para ocultarlo. Una destrucción solo se muestra al clan cuando su piloto ha vuelto a mirar el Skylab o le ha dado una orden (consulta [Clanes](/wiki/03-Mechanics/Clans.md#where-your-clan-mates-are)).

## Mecánicas {#mechanics}

### Construcción y mejora {#building-and-upgrading}

- **Construcción**: cada módulo se construye por separado. Un módulo está en el nivel 1 en el momento en que se construye, y mejorarlo aumenta su producción (o la energía que produce) y su almacenamiento, y también lo que consume de energía.
- **Tiempo y coste**: las mejoras cuestan créditos y Thulium y tardan, y cada módulo tiene su propio precio y su propio tiempo para cada nivel (pasa el cursor sobre **Mejorar** para ver el siguiente; los totales están más abajo). El precio se paga al empezar la mejora. El coste no depende del tiempo. Los módulos de motores, de defensa y de radar piden además Dark Matter Plates y la tecnología del nivel (consulta [El segundo puente y el Núcleo 3](#the-second-bridge-and-core-3)).
- **Temporizadores**: una mejora funciona con el reloj del servidor, así que termina mientras estás fuera, días después si hace falta. Empiézala, desconéctate, vuelve: el módulo está en su nuevo nivel cuando abres la página del Skylab.
- **Acelerar una mejora**: un [Magic Hammer](/wiki/06-Items/Special-Items.md#magic-hammer) termina al instante una mejora en marcha, y un [Workforce Contract](/wiki/06-Items/Special-Items.md#workforce-contract) contratado como **Engineer** hace que las mejoras avancen al doble de velocidad durante 1 hora. Ninguno devuelve ni cobra nada: el precio se pagó al empezar la mejora.
- **Tiempos de mejora**: los primeros niveles son rápidos y los últimos llevan hasta 37 horas, los del Núcleo hasta 6 días (consulta las tablas de más abajo). Cada módulo tiene su propio temporizador, así que puedes mejorar varios a la vez.
- **Pausa de producción**: mientras se mejora un módulo, está desconectado: no produce nada y no consume energía. Solar es la excepción: sigue produciendo una cuarta parte de su energía (consulta más abajo).
- **Solar produce solo el 25 % de su energía mientras se mejora**: Solar produce toda la energía del Skylab y, mientras se mejora (24 horas para el último nivel), produce una cuarta parte de la energía de su nivel **actual**; la del nivel nuevo toma el relevo en cuanto termina la mejora. Una estación completa consume alrededor del 90 % de lo que Solar produce en su propio nivel, así que una cuarta parte de eso solo sostiene una estación que esté cinco o seis niveles por debajo de Solar. Si no, todas las granjas y colectores se detienen durante toda la mejora, lo que tengas almacenado se conserva y se puede recoger, y la Forja no empieza ningún lote nuevo. Un módulo que se está mejorando o que está apagado no consume energía, así que subir las granjas a la vez que Solar no cuesta nada extra, y apagar módulos deja sitio a los demás; la Granja de Thulium es, con diferencia, la que más energía consume.

### Cuánto cuesta {#what-it-costs}

El precio de toda la subida, la construcción más cada mejora, hasta el nivel 10 y hasta el nivel 20. El Núcleo siempre está ahí y sus pasos cuestan créditos, con 2.000 de Thulium más en el paso al nivel 10 y 4.000 más en el paso al nivel 15; el Centro de investigación tiene los niveles 1 a 10 y sus números están en la página [Investigación](/wiki/03-Mechanics/Research.md). La Impresora de munición, la Fábrica de cohetes y la Bahía de mineral se construyen en el Núcleo 2, así que solo cuando el Núcleo está en el nivel 10, y su nivel 1 es la construcción. Los cuatro módulos de la Expedición se construyen en el Núcleo 3, así que solo cuando el Núcleo está en el nivel 15, y los módulos de motores, de defensa y de radar llegan al nivel 5, 5 y 3: sus dos cifras son toda la subida.

| Módulo | Créditos hasta el nivel 10 | Thulium hasta el nivel 10 | Créditos hasta el nivel 20 | Thulium hasta el nivel 20 |
| :--- | ---: | ---: | ---: | ---: |
| Núcleo | 112.326 | 2.000 | 6.647.504 | 6.000 |
| Solar | 1.219.500 | 1.600 | 35.039.500 | 36.850 |
| Granja de créditos | 840.000 | 109 | 26.240.000 | 2.399 |
| Granja de Thulium | 1.154.000 | 4.190 | 32.254.000 | 67.890 |
| Colector de Velkonite | 696.000 | 6.950 | 20.996.000 | 78.950 |
| Colector de Orvium | 696.000 | 6.950 | 20.996.000 | 78.950 |
| Almacén de recursos | 619.500 | 359 | 18.169.500 | 2.649 |
| Forja | 1.224.000 | 2.050 | 35.044.000 | 37.300 |
| Impresora de munición | 1.411.000 | 5.140 | 22.031.000 | 47.940 |
| Fábrica de cohetes | 377.300 | 1.674 | 5.547.300 | 12.494 |
| Bahía de mineral | 619.500 | 359 | 18.169.500 | 2.649 |
| Módulo de motores | 15.775.000 | 63.100 | 15.775.000 | 63.100 |
| Módulo de defensa | 24.400.000 | 97.600 | 24.400.000 | 97.600 |
| Módulo de radar | 3.250.000 | 13.000 | 3.250.000 | 13.000 |
| Bahía de trofeos | 2.372.500 | 9.490 | 14.722.500 | 58.890 |

Los primeros pasos son baratos y los últimos caros: el paso de la Granja de créditos del nivel 1 al 2 cuesta 5.000 créditos y 1 Thulium, y su paso del 19 al 20 cuesta 7.000.000 de créditos y 550 Thulium. Los de la Granja de Thulium cuestan 7.000 créditos y 45 Thulium, y después 8.500.000 créditos y 16.000 Thulium. Las mejoras de Solar cuestan en cada nivel lo mismo que las de la Forja, y los dos colectores cuestan lo mismo entre sí.

Los cuatro módulos de la Expedición piden más que créditos y Thulium: Ship Fragments para construir, Dark Matter Plates y una tecnología por cada nivel de los tres primeros:

| Módulo | Ship Fragments para construir | Placas en total | Investigación: Dark Matter | Investigación: tiempo |
| :--- | ---: | ---: | ---: | ---: |
| Módulo de motores | 20 | 19 | 50 | 6 d 13 h |
| Módulo de defensa | 25 | 26 | 50 | 6 d 13 h |
| Módulo de radar | 15 | 4 | 15 | 1 d 13 h |
| Bahía de trofeos | 10 | 0 | 0 | – |

Los cuatro juntos: 232.590 de Thulium, 58.147.500 créditos, 49 placas, 115 Dark Matter y 14 d 15 h de investigación. Las placas son Dark Matter Plates, y lo que cuesta una placa está en [Dark Matter y Dark Matter Plates](/wiki/03-Mechanics/Dark-Matter.md#how-to-get-a-plate).

### Tiempos de mejora {#upgrade-times}

<!-- upgrade-times:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Tiempos de mejora**, por módulo (la mejora desde el nivel de la primera columna):

| Nivel | Núcleo | Solar | Granja de créditos | Granja de Thulium | Almacén de recursos | Colector de Velkonite | Colector de Orvium | Forja | Centro de investigación |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 a 2 | 72 s | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 5 min | 78 s |
| 2 a 3 | 86 s | 15 min | 10 min | 15 min | 10 min | 15 min | 15 min | 15 min | 101 s |
| 3 a 4 | 104 s | 30 min | 15 min | 30 min | 15 min | 20 min | 20 min | 30 min | 132 s |
| 4 a 5 | 124 s | 45 min | 20 min | 45 min | 20 min | 30 min | 30 min | 45 min | 171 s |
| 5 a 6 | 149 s | 1 h | 30 min | 1 h | 30 min | 45 min | 45 min | 1 h | 223 s |
| 6 a 7 | 20 min | 1 h 15 min | 45 min | 1 h 30 min | 45 min | 50 min | 50 min | 1 h 15 min | 20 min |
| 7 a 8 | 30 min | 1 h 30 min | 1 h | 2 h | 1 h | 1 h | 1 h | 1 h 30 min | 30 min |
| 8 a 9 | 50 min | 2 h | 1 h 20 min | 3 h | 1 h 20 min | 1 h 15 min | 1 h 15 min | 2 h | 50 min |
| 9 a 10 | 1 h 20 min | 3 h | 1 h 40 min | 4 h | 1 h 40 min | 1 h 30 min | 1 h 30 min | 3 h | 1 h 20 min |
| 10 a 11 | 2 h 15 min | 4 h | 2 h | 5 h | 2 h | 2 h | 2 h | 4 h | – |
| 11 a 12 | 3 h 30 min | 5 h | 2 h 30 min | 6 h | 2 h 30 min | 3 h | 3 h | 5 h | – |
| 12 a 13 | 5 h 30 min | 6 h | 3 h | 8 h | 3 h | 4 h | 4 h | 6 h | – |
| 13 a 14 | 9 h | 8 h | 3 h 30 min | 10 h | 3 h 30 min | 6 h | 6 h | 8 h | – |
| 14 a 15 | 14 h | 10 h | 4 h | 11 h | 4 h | 8 h | 8 h | 10 h | – |
| 15 a 16 | 1 d | 12 h | 5 h | 12 h | 5 h | 10 h | 10 h | 12 h | – |
| 16 a 17 | 1 d 12 h | 16 h | 6 h | 14 h | 6 h | 12 h | 12 h | 16 h | – |
| 17 a 18 | 2 d 12 h | 18 h | 8 h | 18 h | 8 h | 16 h | 18 h | 18 h | – |
| 18 a 19 | 4 d | 20 h | 10 h | 1 d | 10 h | 20 h | 1 d | 20 h | – |
| 19 a 20 | 6 d | 1 d | 12 h | 1 d 12 h | 12 h | 1 d | 1 d 12 h | 1 d | – |
| **Total** | 16 d 13 h | 5 d 13 h | 2 d 14 h | 6 d 13 h | 2 d 14 h | 4 d 16 h | 5 d 10 h | 5 d 13 h | 3 h 12 min |
<!-- upgrade-times:end -->

<!-- upgrade-times-expedition:start -->
<!-- Generated from server/Resources/SkylabConfig.json by the test skylab::duration_tests::the_wiki_page_is_the_config (run it with SKYLAB_WIKI_WRITE=1 to rewrite this part). -->

**Tiempos de mejora** de los cuatro módulos de la Expedición (la mejora desde el nivel de la primera columna; un guion está más allá del nivel máximo del módulo):

| Nivel | Módulo de motores | Módulo de defensa | Módulo de radar | Bahía de trofeos |
| :--- | ---: | ---: | ---: | ---: |
| 1 a 2 | 2 h | 3 h | 4 h | 15 min |
| 2 a 3 | 6 h | 9 h | 1 d | 19 min |
| 3 a 4 | 1 d | 1 d 12 h | – | 26 min |
| 4 a 5 | 2 d | 3 d | – | 34 min |
| 5 a 6 | – | – | – | 45 min |
| 6 a 7 | – | – | – | 1 h |
| 7 a 8 | – | – | – | 1 h 19 min |
| 8 a 9 | – | – | – | 1 h 44 min |
| 9 a 10 | – | – | – | 2 h 18 min |
| 10 a 11 | – | – | – | 3 h 2 min |
| 11 a 12 | – | – | – | 4 h |
| 12 a 13 | – | – | – | 5 h 17 min |
| 13 a 14 | – | – | – | 6 h 59 min |
| 14 a 15 | – | – | – | 9 h 14 min |
| 15 a 16 | – | – | – | 12 h 11 min |
| 16 a 17 | – | – | – | 16 h 5 min |
| 17 a 18 | – | – | – | 21 h 14 min |
| 18 a 19 | – | – | – | 1 d 4 h |
| 19 a 20 | – | – | – | 1 d 13 h |
| **Total** | 3 d 8 h | 5 d | 1 d 4 h | 6 d 8 h |
<!-- upgrade-times-expedition:end -->

Una mejora que ya está en marcha cuando cambian los tiempos conserva la hora de fin que se le dio. Solo el Núcleo necesita unos **16,5 días** de mejora seguidos para ir del nivel 1 al nivel 20. Ningún módulo pasa del nivel del Núcleo, así que el último paso de cualquier otro módulo (de 12 a 37 horas) solo puede empezar cuando el Núcleo está en el nivel 20: con todos los temporizadores ocupados y los créditos y el Thulium a punto, toda la estación necesita unos **18 días**.

### Gestión de la energía {#power-management}

Tu Skylab tiene un presupuesto de energía limitado.

- **Balance**: mantén la producción de tu Solar por encima de la energía que usan todos los demás módulos. La página del Skylab muestra el balance y avisa antes de que una construcción lo deje por debajo de cero.
- **Solar sigue el ritmo**: un módulo Solar de nivel N produce la energía de **todos los demás módulos en el nivel N** (el Núcleo, las dos granjas, el Almacén de recursos, los dos colectores y la Forja, y desde el nivel 10 el Centro de investigación y la Bahía de mineral) y aproximadamente una décima parte más, así que una estación cuyos módulos están todos en el nivel 7 necesita Solar 7 y la tiene cubierta. Solar un nivel por debajo no basta para una estación completa (la última columna), de modo que Solar tiene que seguir subiendo con el resto. El Núcleo consume poco, así que puede ir por delante: Solar 5 o más cubre una estación completa a su nivel con el Núcleo en cualquier nivel. La tabla de más abajo cuenta también la Impresora de munición desde el nivel 7, la Fábrica de cohetes y la Bahía de mineral desde el nivel 10, y los módulos de motores, de defensa y de radar y la Bahía de trofeos desde el nivel 11 (se construyen desde el nivel 15 del Núcleo y cuentan cuatro niveles antes porque el Núcleo puede ir por delante de Solar), cada uno como mucho en su propio nivel máximo.
- **Estado activo**: puedes encender y apagar las granjas, los colectores y la Forja para gestionar la energía. El Núcleo, Solar, el Almacén de recursos y el Centro de investigación siempre funcionan. La Impresora de munición, la Fábrica de cohetes y la Bahía de mineral también se pueden encender y apagar, y los cuatro módulos de la Expedición también (no mientras hay un viaje en curso).
- **Apagón**: si el consumo de energía supera la producción, todas las granjas y colectores dejan de producir hasta que el balance vuelve. Lo que ya guardan se queda y todavía puedes recogerlo. La Forja no empieza ningún lote nuevo y el Centro de investigación no empieza ninguna investigación nueva (una investigación ya en marcha continúa). La Impresora de munición, la Fábrica de cohetes y la Bahía de mineral se detienen como las granjas y los colectores. El Módulo de defensa no combate nada, los escaneos del radar se detienen y no puede empezar ningún viaje (un viaje que ya está en marcha continúa).
- **Mejora de Solar**: mientras se mejora, Solar produce solo una cuarta parte de su energía, así que, si tus demás módulos no están muy por debajo, la estación entra en déficit y las granjas y los colectores se detienen hasta que termina la mejora (consulta el [módulo Solar](#solar-module)).

La energía de Solar en cada nivel, frente a lo que consumen los demás módulos en el mismo nivel (todos los módulos en ese nivel, el Núcleo incluido, y el Centro de investigación y la Bahía de mineral desde el nivel 10, y los cuatro módulos de la Expedición desde el nivel 11):

<!-- skylab-power:start -->
<!-- Generated from server/Resources/SkylabConfig.json by docs/design/skylab-power-model.py --doc (--check fails while this part is behind). -->

| Nivel | Solar produce | Los demás módulos consumen | Sobrante | Con Solar un nivel por debajo |
| :--- | ---: | ---: | ---: | :--- |
| 1 | 255 | 230 | 25 | – |
| 2 | 310 | 278 | 32 | 255: faltan 23 |
| 3 | 375 | 337 | 38 | 310: faltan 27 |
| 4 | 455 | 410 | 45 | 375: faltan 35 |
| 5 | 555 | 501 | 54 | 455: faltan 46 |
| 6 | 680 | 615 | 65 | 555: faltan 60 |
| 7 | 965 | 875 | 90 | 680: faltan 195 |
| 8 | 1.185 | 1.076 | 109 | 965: faltan 111 |
| 9 | 1.460 | 1.327 | 133 | 1.185: faltan 142 |
| 10 | 2.035 | 1.849 | 186 | 1.460: faltan 389 |
| 11 | 2.995 | 2.721 | 274 | 2.035: faltan 686 |
| 12 | 3.565 | 3.241 | 324 | 2.995: faltan 246 |
| 13 | 4.285 | 3.893 | 392 | 3.565: faltan 328 |
| 14 | 5.185 | 4.713 | 472 | 4.285: faltan 428 |
| 15 | 6.325 | 5.748 | 577 | 5.185: faltan 563 |
| 16 | 7.765 | 7.055 | 710 | 6.325: faltan 730 |
| 17 | 9.585 | 8.711 | 874 | 7.765: faltan 946 |
| 18 | 11.895 | 10.812 | 1.083 | 9.585: faltan 1.227 |
| 19 | 14.835 | 13.483 | 1.352 | 11.895: faltan 1.588 |
| 20 | 18.575 | 16.885 | 1.690 | 14.835: faltan 2.050 |
<!-- skylab-power:end -->

La tabla cuenta todos los módulos en el mismo nivel. La Granja de Thulium consume arriba más de dos tercios (11.695 en el nivel 20, frente a 16.885 de los quince), así que una estación con esa granja muy por delante del resto necesita más Solar de lo que sugiere su Núcleo.

### Recogida {#collecting}

Cada granja y cada colector tiene una tolva para unas 72 horas de lo que produce. La recogida es manual.

- **Capacidad**: cuando una tolva se llena, deja de producir hasta que recoges.
- **Granjas**: los créditos y el Thulium recogidos van directamente a tu cuenta.
- **Colectores**: el mineral va al Almacén de recursos, hasta donde haya sitio.
- **Forja**: las placas van a tu inventario, cuando tu nave está aterrizada.
- **Impresora de munición y Fábrica de cohetes**: la munición y los cohetes pasan a tu inventario, cuando tu nave está aterrizada. Cada una guarda solo 24 horas de producción (consulta [Impresora de munición](#ammo-printer) y [Fábrica de cohetes](#rocket-factory)).
- **Bahía de mineral**: nada que recoger. Pasa el mineral de tu inventario al Almacén de recursos cuando pulsas **Mover**, con tu nave aterrizada, hasta su cupo (consulta [Bahía de mineral](#ore-bay)).
- **Bahía de trofeos**: se recoge en la ventana Universo, con la nave aterrizada: los créditos y el Thulium van a tu cuenta, la experiencia y el honor a tu piloto y el botín a tu inventario. Guarda lo que contiene hasta que la recojas, pero una bahía llena hace que el Skylab deje de disparar (consulta [Bahía de trofeos](#trophies-bay)).
- **Recoger todo** toma todo a la vez, también de módulos apagados o en mejora, pero no la Bahía de trofeos, que recoges en la ventana Universo.
- Una insignia **(!)** señala una tolva llena que puedes vaciar y las placas que esperan en la Forja, en la página del Skylab y en la fila del Skylab de la barra lateral.

### El reinicio {#the-wipe}

El Skylab nunca se reinicia: los módulos conservan sus niveles, el Almacén de recursos conserva su mineral y el Centro de investigación conserva sus tecnologías, su depósito de ciencia, el Dark Matter que contiene y una investigación en curso. Las placas de tu inventario son objetos como cualquier otro, así que siguen las [reglas del reinicio](/wiki/03-Mechanics/Wipe-Timeline.md). La Impresora de munición y la Fábrica de cohetes conservan sus niveles, lo que tienen configurado fabricar y lo que guardan, y la Bahía de mineral conserva su nivel y su cupo. Los cuatro módulos de la Expedición conservan también sus niveles, con sus tecnologías, y lo mismo el cargador y el interruptor de la alimentación. El mineral de tu inventario se reinicia como cualquier objeto: pásalo antes al Almacén de recursos.

Una **expedición** se liquida hasta el reinicio: un viaje en curso termina, la Bahía de trofeos paga sus créditos, su Thulium, su experiencia y su honor y se vacía (su botín se borra como cualquier objeto suelto; los créditos y el Thulium llegan a tu cartera antes de que se apliquen los [topes](/wiki/03-Mechanics/Wipe-Timeline.md#the-caps)), y el Skylab empieza la nueva temporada en casa, en el puerto de tu corporación, con un mapa del universo nuevo, las 19 celdas iniciales conocidas y la cola del radar vacía. Los motores y láseres montados en los módulos de motores y de defensa son objetos sueltos como los demás: sácalos y guárdalos en el Alijo de Transporte para conservarlos.

## Planifica tu Skylab {#planning-your-skylab}

El Skylab tarda semanas en crecer, así que un poco de planificación compensa. Las cifras son las de las tablas de arriba.

### Qué mejorar primero {#what-to-upgrade-first}

1. **Solar, y luego la Granja de créditos.** Solar cuesta 500 créditos y 50 Thulium y sin él nada funciona; la Granja de créditos no cuesta nada. Las diez [misiones de la estación](/wiki/03-Mechanics/Quests.md#station-missions) te guían en estos primeros pasos y te pagan por ellos 52.000 créditos y 610 Thulium, como base: tu mundo, tus potenciadores y las bonificaciones de tu clan la multiplican.
2. **Después la Granja de Thulium: es tu principal fuente de Thulium.** En el nivel 10 produce 360 Thulium por hora, 8.640 al día, aproximadamente tanto como pagan 43 bajas de un [Crystalys](/wiki/04-Aliens/Crystalys.md) en Alpha (200 cada una). Llegar al nivel 10 cuesta 1.154.000 créditos y 4.190 Thulium, con la construcción incluida. En el nivel 15 la granja produce 18.240 al día y en el nivel 20, 30.720. Su tolva guarda 72 horas, así que vuelve al menos cada tres días. Lo que se compra con Thulium está en la página [Recursos](/wiki/06-Items/Resources.md#thulium).
3. **La Granja de créditos es el ingreso estable de segundo plano.** En el nivel 10 produce 33.750 créditos por hora, 810.000 al día, por 840.000 créditos y 109 Thulium. Los niveles altos se amortizan en días: el paso del nivel 9 al 10 cuesta 300.000 créditos por 4.500 más por hora, es decir, 67 horas. Mejórala cuando te sobren créditos.
4. **Mantén ocupado el Núcleo.** Nada pasa del Núcleo, y el Núcleo solo tarda unos 16 días y medio en llegar al nivel 20. No hay cola, así que empieza su siguiente paso cada vez que vuelvas.
5. **Construye la cadena de suministro como un conjunto.** Los colectores, el Almacén de recursos y la Forja se abren en el nivel 5 del Núcleo. Un colector solo puede guardar mineral en un Almacén de recursos, y la reserva guarda un día de la producción de su colector en el nivel 1 y cuatro días en el nivel 20, así que mejora el Almacén junto con los colectores o el mineral esperará en sus tolvas.
6. **Ten 2.000 de Thulium listos para el nivel 10 del Núcleo.** El paso del Núcleo del nivel 9 al nivel 10 los pide, y construye el puente y el Núcleo 2, donde se construyen la [Impresora de munición](#ammo-printer), la [Fábrica de cohetes](#rocket-factory) y la [Bahía de mineral](#ore-bay).
7. **Ten 4.000 de Thulium listos para el nivel 15 del Núcleo.** El paso del Núcleo del nivel 14 al nivel 15 los pide, y construye el segundo puente y el Núcleo 3, donde se construyen los cuatro módulos de la Expedición. Los módulos en sí piden mucho más, 232.590 de Thulium y 49 Dark Matter Plates en total (consulta [Cuánto cuesta](#what-it-costs)): empieza por el Módulo de motores y el Módulo de defensa en el nivel 1.
8. **Construye la Expedición en este orden.** Un motor en el Módulo de motores, un láser en el Módulo de defensa con una Impresora de munición que lo alimente, y la Bahía de trofeos para guardar lo que traen las bajas: un viaje no rinde nada hasta que están los tres. El Módulo de radar puede esperar: con Defensa 1 tu Skylab llega al menos a las seis celdas junto a su puerto, y las 19 celdas que conoces al empezar incluyen celdas de hasta dificultad 3.

### Cómo planificar una mejora de Solar {#timing-a-solar-upgrade}

Mientras Solar se mejora produce una cuarta parte de su energía, y una estación casi siempre consume más que eso. Las granjas y los colectores se detienen entonces durante toda la mejora: lo que guardan se queda, pero lo que habrían producido se pierde. La tabla da, para cada paso de Solar, su tiempo, la estación más grande que todavía lo supera (todos los módulos en el mismo nivel, el Núcleo y la cadena de suministro incluidos; una estación más pequeña cabe algo más) y lo que una Granja de créditos y una Granja de Thulium de ese nivel habrían producido en ese tiempo. Por ejemplo, Solar del nivel 10 al 11 tarda 4 horas, y granjas de nivel 10 habrían producido en ellas 135.000 créditos y 1.440 de Thulium. La tabla cuenta también la Impresora de munición desde el nivel 7, la Fábrica de cohetes y la Bahía de mineral desde el nivel 10 y los cuatro módulos de la Expedición desde el nivel 15.

| Mejora de Solar | Tiempo | Estación que sigue funcionando, hasta el nivel | La Granja de créditos produce entretanto | La Granja de Thulium produce entretanto |
| :--- | ---: | ---: | ---: | ---: |
| 1 a 2 | 5 min | ninguna | 188 | 3 |
| 2 a 3 | 15 min | ninguna | 1.125 | 16 |
| 3 a 4 | 30 min | ninguna | 3.375 | 44 |
| 4 a 5 | 45 min | ninguna | 6.750 | 84 |
| 5 a 6 | 1 h | ninguna | 11.250 | 144 |
| 6 a 7 | 1 h 15 min | ninguna | 19.688 | 230 |
| 7 a 8 | 1 h 30 min | 1 | 30.375 | 336 |
| 8 a 9 | 2 h | 2 | 49.500 | 528 |
| 9 a 10 | 3 h | 3 | 87.750 | 912 |
| 10 a 11 | 4 h | 5 | 135.000 | 1.440 |
| 11 a 12 | 5 h | 6 | 202.500 | 2.200 |
| 12 a 13 | 6 h | 7 | 297.000 | 3.120 |
| 13 a 14 | 8 h | 7 | 468.000 | 4.800 |
| 14 a 15 | 10 h | 8 | 675.000 | 6.800 |
| 15 a 16 | 12 h | 9 | 918.000 | 9.120 |
| 16 a 17 | 16 h | 10 | 1.440.000 | 14.080 |
| 17 a 18 | 18 h | 11 | 1.944.000 | 18.000 |
| 18 a 19 | 20 h | 12 | 2.610.000 | 22.400 |
| 19 a 20 | 1 d | 13 | 3.780.000 | 28.800 |

- **Sube las granjas a la vez que Solar.** Un módulo en mejora no produce nada y no consume energía de todos modos, así que el tiempo que una granja pasa mejorándose durante la pausa no cuesta nada extra.
- **Mantén bajos los demás módulos si no puedes permitirte una pausa.** Una estación solo sigue funcionando durante una mejora de Solar si todos sus demás módulos están al menos cinco niveles por debajo de Solar (seis desde el nivel 10 de Solar), y una estación completa necesita algo más, como muestra la tabla.
- **Apaga lo que puedas dejar sin usar.** Un módulo apagado no consume energía, así que apagar la Granja de Thulium, la que más consume (80 en el nivel 1 y un 30 % más por nivel), deja sitio a los demás.
